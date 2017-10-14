import java.awt.image.BufferedImage;
import java.awt.image.WritableRaster;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Spreader
{
  private BufferedImage image;
  private WritableRaster raster;
  private byte[] msgBytes;
  private byte[] key;
  private int[][] noise;
  private double[] solved;
  private double[][] pixels;
  private int[][] current_grid;
  private int width;
  private int height;
  private String result;
  private final int bitsPerByte = 6;
  private MessageDigest md;

  public void setImage(BufferedImage paramBufferedImage)
  {
    this.image = paramBufferedImage;
    this.raster = paramBufferedImage.getRaster();
    this.width = paramBufferedImage.getWidth();
    this.height = paramBufferedImage.getHeight();
  }

  public BufferedImage getImage()
  {
    return this.image;
  }

  public Spreader(String paramString, BufferedImage paramBufferedImage, MessageDigest paramMessageDigest)
  {
    try
    {
      this.key = paramString.getBytes("utf8");
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
      System.err.println("Votre système ne supporte pas utf8 oO?\nMais on fera comme si.");

      this.key = paramString.getBytes();
    }
    setImage(paramBufferedImage);
    this.md = paramMessageDigest;
  }

  private void setStegoBytes(String paramString)
    throws InvalidStegoMessageException
  {
    String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ";
    this.msgBytes = new byte[paramString.length() + 1];
    for (int i = 0; i < this.msgBytes.length - 1; i++)
    {
      this.msgBytes[i] = ((byte)str.indexOf(paramString.charAt(i)));
      if (this.msgBytes[i] == -1) {
        throw new InvalidStegoMessageException();
      }
    }
    this.msgBytes[(this.msgBytes.length - 1)] = 63;
    System.out.println("Message :");
    System.out.println(new String(this.msgBytes));
    System.out.println(paramString);
  }

  public String convert_bits_to_string(String binary)
  {
      String ret = new String("");
      String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ";
      for(int i=0; i+5<binary.length(); i+=6)
      {
          int c = 0;
          for(int j=0; j<6; j++)
            if(binary.charAt(i+j) == '1')
                c += (1<<(5-j));
          ret += str.charAt(c);
      }
      return ret;
  }

  private float weight_cur()
  {
      List<Float> x = new ArrayList<Float>();
      List<Float> y = new ArrayList<Float>();
      float score = 0;
      for(int i=0; i<this.solved.length; i++)
      {
          if(this.solved[i]>0)
              x.add(new Float(this.solved[i]));
          else
              y.add(new Float(this.solved[i]));
      }

      for(Float a : x)
          score += a.floatValue();
      for(Float a : y)
          score -= a.floatValue();

      /*System.out.println("=================");
      System.out.println(score);
      System.out.println(x);
      System.out.println(y);*/
      return score;
  }

  public void compute_array()
  {
      this.pixels = new double[this.height][this.width];
      double moy = 0;
      int rgb = this.raster.getNumBands();
      double[] arrayOfDouble = new double[rgb];
      double[] arrayOfDouble2 = new double[rgb];
      for (int j = 0; j < this.height; j++) {
          for (int k = 0; k < this.width; k++)
          {
              arrayOfDouble = this.raster.getPixel(k, j, arrayOfDouble2);
              moy += arrayOfDouble[0];
          }
      }

      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++)
        {
          arrayOfDouble = this.raster.getPixel(k, j, arrayOfDouble2);
          this.pixels[j][k] = arrayOfDouble[0]-moy/(float)(this.height*this.width);
        }
      }
  }

  private float test(int length, String key)
  {
      int max = 20000;
      //int[][] G = new int[this.height*this.width][length];
      this.solved = new double[length];

      /*InfiniteHashBitEnumerator localInfiniteHashBitEnumerator = new InfiniteHashBitEnumerator(key.getBytes(), this.md);

      long startTime = System.currentTimeMillis();
      for (int i = 0; i < length; i++)
        for (int j = 0; j < this.height*this.width; j++)
          G[j][i] = localInfiniteHashBitEnumerator.next();
      System.out.println(System.currentTimeMillis()-startTime);*/

      //long startTime = System.currentTimeMillis();
      for (int i = 0; i < length; i++) {
        double summed = 0;
        int cur = 0;
        for (int j = 0; j < this.height; j++) {
          for (int k = 0; k < this.width; k++) {
            summed += this.current_grid[k+j*this.width][i]*this.pixels[j][k];
            //if(cur>max)
            //    break;
            cur++;
          }
          //if(cur>max)
            //  break;
        }
        this.solved[i] = summed;
      }
      //System.out.println(System.currentTimeMillis()-startTime);

      return this.weight_cur();
  }

  private String apply(int length, String key)
  {
      this.result = new String();
      for (int i = 0; i < length; i++) {
        double summed = 0;
        for (int j = 0; j < this.height; j++) {
          for (int k = 0; k < this.width; k++) {
            summed += this.current_grid[k+j*this.width][i]*this.pixels[j][k];
          }
        }
        if(summed>0)
            this.result += "1";
        else
            this.result += "0";
      }

      return this.result;
  }

  private void create_grid(String key, int max)
  {
      this.current_grid = new int[this.height*this.width][max];

      InfiniteHashBitEnumerator localInfiniteHashBitEnumerator = new InfiniteHashBitEnumerator(key.getBytes(), this.md);

      for (int i = 0; i < max; i++)
        for (int j = 0; j < this.height*this.width; j++)
          this.current_grid[j][i] = localInfiniteHashBitEnumerator.next();
  }

  public void smart_bruteforce(int lengthMin, int lengthMax)
  {
      String charset = "abcdefghijklmnopqrstuvwxyzFGHIJKLMNOPQRSTUVWXYZ0123456789+=- _{}ABCDE";

      int done = 0;
      float moy = 0, max_var = 0;
      for(int i=0; i<charset.length(); i++)
        for(int j=0; j<charset.length(); j++)
        {
            for(int k=0; k<charset.length(); k++)
            {
                String key = ""+charset.charAt(i)+charset.charAt(j)+charset.charAt(k);

                long startTime = System.currentTimeMillis();
                create_grid(key, 6);
                System.out.println("======================================");
                System.out.println(String.format("%d",System.currentTimeMillis()-startTime)+" millis to create grid for key "+key);

                startTime = System.currentTimeMillis();
                float res = test(6, key);
                System.out.println(System.currentTimeMillis()-startTime);
                System.out.println("Giving moy "+String.format("%f", moy)+" and var "+String.format("%f", max_var));
                if(done>10)
                    if((res-moy)*(res-moy)>10*max_var)
                    {
                        System.out.println("We may have found the key : "+key+" with length 1 and variance "+String.format("%f", (res-moy)*(res-moy)));
                        System.exit(0);
                    }
                    else
                    {
                        moy = (moy*(float)done+res)/(float)(done+1);
                        if((res-moy)*(res-moy)>max_var)
                            max_var = (res-moy)*(res-moy);
                    }
                else
                {
                    moy = (moy*(float)done+res)/(float)(done+1);
                    if(done>8)
                        if((res-moy)*(res-moy)>max_var)
                            max_var = (res-moy)*(res-moy);
                }
                done ++;
            }
        }
  }

  public void smart_bruteforce_with_key(int lengthMin, int lengthMax, String key)
  {
      String charset = "abcdefghijklmnopqrstuvwxyzFGHIJKLMNOPQRSTUVWXYZ0123456789+=- _{}ABCDE";

      long startTime = System.currentTimeMillis();
      create_grid(key, lengthMax*6);
      System.out.println("======================================");
      System.out.println(String.format("%d",System.currentTimeMillis()-startTime)+" millis to create grid for key "+key);

      for(int i=lengthMin; i<lengthMax; i++)
      {
        apply(6*i, key);
        System.out.println("For i = "+String.format("%d", i)+" we have the result : "+this.result+" => "+this.convert_bits_to_string(this.result));
      }
  }

  private void bruteforce(int lengthMin, int lengthMax)
  {
      String charset = "AaCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

      int done = 0;
      float moy = 0, max_var = 0;
      for(int l=lengthMin; l<lengthMax; l++)
      {
          System.out.println("======================================");
          System.out.println("Testing "+String.format("%d", l));
          moy = 0;
          max_var = 0;
          done = 0;
          for(int i=0; i<charset.length(); i++)
            for(int j=0; j<charset.length(); j++)
                for(int k=0; k<charset.length(); k++)
                {
                    String key = ""+charset.charAt(i)+charset.charAt(j)+charset.charAt(k);
                    long startTime = System.currentTimeMillis();
                    float res = test(l*6, key);
                    System.out.println(System.currentTimeMillis()-startTime);
                    System.out.println("Testing "+key+" with moy "+String.format("%f", moy)+" and var "+String.format("%f", max_var));
                    if(done>10)
                        if((res-moy)*(res-moy)>10*max_var)
                        {
                            System.out.println("We may have found the key : "+key+" with length "+String.format("%d", l)+" and variance "+String.format("%f", (res-moy)*(res-moy)));
                        }
                        else
                        {
                            moy = (moy*(float)done+res)/(float)(done+1);
                            if((res-moy)*(res-moy)>max_var)
                                max_var = (res-moy)*(res-moy);
                        }
                    else
                    {
                        moy = (moy*(float)done+res)/(float)(done+1);
                        if(done>8)
                            if((res-moy)*(res-moy)>max_var)
                                max_var = (res-moy)*(res-moy);
                    }
                    done ++;
                }
        }
  }

  /*private void test()
  {
      int length = this.msgBytes.length*6;
      int[][] G = new int[this.height*this.width][length];
      double[] dotduct = new double[length];

      InfiniteHashBitEnumerator localInfiniteHashBitEnumerator = new InfiniteHashBitEnumerator(new String("aba").getBytes(), this.md);

      for (int i = 0; i < length; i++) {
        for (int j = 0; j < this.height*this.width; j++) {
          G[j][i] = localInfiniteHashBitEnumerator.next();
        }
      }

      double moy = 0;
      int rgb = this.raster.getNumBands();
      double[] arrayOfDouble = new double[rgb];
      double[] arrayOfDouble2 = new double[rgb];
      for (int j = 0; j < this.height; j++) {
          for (int k = 0; k < this.width; k++)
          {
              arrayOfDouble = this.raster.getPixel(k, j, arrayOfDouble2);
              moy += arrayOfDouble[0];
          }
      }

      for (int i = 0; i < length; i++) {
        double summed = 0;
        for (int j = 0; j < this.height; j++) {
          for (int k = 0; k < this.width; k++)
          {
            arrayOfDouble = this.raster.getPixel(k, j, arrayOfDouble2);
            summed += G[k+j*this.width][i]*(arrayOfDouble[0]-moy/(float)(this.height*this.width));
          }
        }
        dotduct[i] = summed;
        System.out.print(dotduct[i]);
        System.out.print(", ");
      }
      System.out.println("");
  }*/

  private void buildNoiseMatrix()
  {
    BitEnumerator localBitEnumerator = new BitEnumerator(this.msgBytes, 6);

    int length = this.msgBytes.length*6;
    System.out.println("Key:");
    System.out.println(this.key);
    int[] w = new int[this.height*this.width];
    int[] w2 = new int[this.height*this.width];
    double[] w3 = new double[this.height*this.width];
    int[][] all = new int[this.height*this.width][length];
    int[][] G = new int[this.height*this.width][length];
    int cur = 0;
    InfiniteHashBitEnumerator localInfiniteHashBitEnumerator = new InfiniteHashBitEnumerator(this.key, this.md);
    this.noise = new int[this.width][this.height];
    for (int i = localBitEnumerator.next(); i != -1; i = localBitEnumerator.next()) {
      System.out.print(i);
      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++) {
          int tmp = localInfiniteHashBitEnumerator.next();
          this.noise[k][j] -= (i ^ tmp) * 2 - 1;
          G[k+j*this.width][cur] = tmp;
          w2[k+j*this.width] -= (i ^ tmp) * 2 - 1;
          if(i>0)
          {
            w[k+j*this.width] += tmp;
            all[k+j*this.width][cur] = tmp;
          }
          else
          {
            w[k+j*this.width] -= tmp;
            all[k+j*this.width][cur] = -tmp;
          }
        }
      }
      cur ++;
    }
    System.out.println("");

    for (int i = 0; i < length; i++) {
      double summed = 0;
      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++) {
          summed += all[k+j*this.width][i];
        }
      }
      System.out.print(summed);
      System.out.print(", ");
    }
    System.out.println("");

    for (int i = 0; i < length; i++) {
      double summed = 0;
      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++) {
          summed += w[k+j*this.width]*G[k+j*this.width][i];
        }
      }
      System.out.print(summed);
      System.out.print(", ");
    }
    System.out.println("");

    for (int i = 0; i < length; i++) {
      double summed = 0;
      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++) {
          summed += w2[k+j*this.width]*G[k+j*this.width][i];
        }
      }
      System.out.print(summed);
      System.out.print(", ");
    }
    System.out.println("");

    double moy1 = 0, moy2 = 0;
    int rgb = this.raster.getNumBands();
    double[] arrayOfDouble1 = new double[rgb];
    double[] arrayOfDouble2 = new double[rgb];
    for (int j = 0; j < this.height; j++) {
      for (int k = 0; k < this.width; k++)
      {
        arrayOfDouble1 = this.raster.getPixel(k, j, arrayOfDouble2);
        double d = Math.max(Math.min(this.noise[k][j], 4), -4) * 1.0D;
        w3[k+j*this.width] = Math.min(Math.max(arrayOfDouble1[0] + d, 0.0D), 255.0D);
        moy1 += arrayOfDouble1[0];
        for (int m = 0; m < rgb; m++) {
          arrayOfDouble1[m] = Math.min(Math.max(arrayOfDouble1[m] + d, 0.0D), 255.0D);
        }
        this.raster.setPixel(k, j, arrayOfDouble1);
      }
    }

    for (int i = 0; i < length; i++) {
      double summed = 0;
      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++) {
            arrayOfDouble1 = this.raster.getPixel(k, j, arrayOfDouble2);
            summed += (arrayOfDouble1[0]-moy1/(float)(this.width*this.height))*G[k+j*this.width][i];
        }
      }
      System.out.print(summed);
      System.out.print(", ");
    }
    System.out.println("");

    for (int i = 0; i < length; i++) {
      double summed = 0;
      for (int j = 0; j < this.height; j++) {
        for (int k = 0; k < this.width; k++) {
          summed += w3[k+j*this.width]*G[k+j*this.width][i];
        }
      }
      System.out.print(summed);
      System.out.print(", ");
    }
    System.out.println("");

    this.compute_array();
    //this.test(this.msgBytes.length*6, new String("aaa"));
    this.smart_bruteforce(this.msgBytes.length-1, this.msgBytes.length+3);
    System.exit(0);

  }

  public void makeMark(String paramString, int paramInt, double paramDouble)
    throws InvalidStegoMessageException
  {
    try
    {
      setStegoBytes(paramString);
      buildNoiseMatrix();
      doMakeMark(paramInt, paramDouble);
    }
    catch (InvalidStegoMessageException localInvalidStegoMessageException)
    {
      throw localInvalidStegoMessageException;
    }
  }

  private void doMakeMark(int paramInt, double paramDouble)
  {
    int i = this.raster.getNumBands();
    double[] arrayOfDouble1 = new double[i];
    double[] arrayOfDouble2 = new double[i];
    for (int j = 0; j < this.height; j++) {
      for (int k = 0; k < this.width; k++)
      {
        arrayOfDouble1 = this.raster.getPixel(k, j, arrayOfDouble2);
        double d = Math.max(Math.min(this.noise[k][j], paramInt), -paramInt) * paramDouble;
        for (int m = 0; m < i; m++) {
          arrayOfDouble1[m] = Math.min(Math.max(arrayOfDouble1[m] + d, 0.0D), 255.0D);
        }
        this.raster.setPixel(k, j, arrayOfDouble1);
      }
    }
  }
}
