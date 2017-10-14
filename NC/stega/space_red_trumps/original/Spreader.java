/*     */ import java.awt.image.BufferedImage;
/*     */ import java.awt.image.WritableRaster;
/*     */ import java.io.PrintStream;
/*     */ import java.io.UnsupportedEncodingException;
/*     */ import java.security.MessageDigest;
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ class Spreader
/*     */ {
/*     */   private BufferedImage image;
/*     */   private WritableRaster raster;
/*     */   private byte[] msgBytes;
/*     */   private byte[] key;
/*     */   private int[][] noise;
/*     */   private int width;
/*     */   private int height;
/*  20 */   private final int bitsPerByte = 6;
/*     */   
/*     */   private MessageDigest md;
/*     */   
/*     */ 
/*     */   public void setImage(BufferedImage paramBufferedImage)
/*     */   {
/*  27 */     this.image = paramBufferedImage;
/*  28 */     this.raster = paramBufferedImage.getRaster();
/*  29 */     this.width = paramBufferedImage.getWidth();
/*  30 */     this.height = paramBufferedImage.getHeight();
/*     */   }
/*     */   
/*     */   public BufferedImage getImage() {
/*  34 */     return this.image;
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */   public Spreader(String paramString, BufferedImage paramBufferedImage, MessageDigest paramMessageDigest)
/*     */   {
/*     */     try
/*     */     {
/*  43 */       this.key = paramString.getBytes("utf8");
/*     */     }
/*     */     catch (UnsupportedEncodingException localUnsupportedEncodingException)
/*     */     {
/*  47 */       System.err.println("Votre système ne supporte pas utf8 oO?\nMais on fera comme si.");
/*     */       
/*  49 */       this.key = paramString.getBytes();
/*     */     }
/*     */     
/*  52 */     setImage(paramBufferedImage);
/*  53 */     this.md = paramMessageDigest;
/*     */   }
/*     */   
/*     */   private void setStegoBytes(String paramString) throws InvalidStegoMessageException
/*     */   {
/*  58 */     String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ";
/*  59 */     this.msgBytes = new byte[paramString.length() + 1];
/*  60 */     for (int i = 0; i < this.msgBytes.length - 1; i++)
/*     */     {
/*  62 */       this.msgBytes[i] = ((byte)str.indexOf(paramString.charAt(i)));
/*  63 */       if (this.msgBytes[i] == -1)
/*  64 */         throw new InvalidStegoMessageException();
/*     */     }
/*  66 */     this.msgBytes[(this.msgBytes.length - 1)] = 63;
/*     */   }
/*     */   
/*     */   private void buildNoiseMatrix()
/*     */   {
/*  71 */     BitEnumerator localBitEnumerator = new BitEnumerator(this.msgBytes, 6);
/*     */     
/*  73 */     InfiniteHashBitEnumerator localInfiniteHashBitEnumerator = new InfiniteHashBitEnumerator(this.key, this.md);
/*  74 */     this.noise = new int[this.width][this.height];
/*     */     
/*  76 */     for (int i = localBitEnumerator.next(); i != -1; i = localBitEnumerator.next())
/*     */     {
/*  78 */       for (int j = 0; j < this.height; j++) {
/*  79 */         for (int k = 0; k < this.width; k++) {
/*  80 */           this.noise[k][j] -= (i ^ localInfiniteHashBitEnumerator.next()) * 2 - 1;
/*     */         }
/*     */       }
/*     */     }
/*     */   }
/*     */   
/*     */   public void makeMark(String paramString, int paramInt, double paramDouble) throws InvalidStegoMessageException
/*     */   {
/*     */     try {
/*  89 */       setStegoBytes(paramString);
/*  90 */       buildNoiseMatrix();
/*  91 */       doMakeMark(paramInt, paramDouble);
/*     */     }
/*     */     catch (InvalidStegoMessageException localInvalidStegoMessageException)
/*     */     {
/*  95 */       throw localInvalidStegoMessageException;
/*     */     }
/*     */   }
/*     */   
/*     */ 
/*     */   private void doMakeMark(int paramInt, double paramDouble)
/*     */   {
/* 102 */     int i = this.raster.getNumBands();
/* 103 */     double[] arrayOfDouble1 = new double[i];
/* 104 */     double[] arrayOfDouble2 = new double[i];
/*     */     
/*     */ 
/* 107 */     for (int j = 0; j < this.height; j++) {
/* 108 */       for (int k = 0; k < this.width; k++)
/*     */       {
/* 110 */         arrayOfDouble1 = this.raster.getPixel(k, j, arrayOfDouble2);
/* 111 */         double d = Math.max(Math.min(this.noise[k][j], paramInt), -paramInt) * paramDouble;
/*     */         
/* 113 */         for (int m = 0; m < i; m++) {
/* 114 */           arrayOfDouble1[m] = Math.min(Math.max(arrayOfDouble1[m] + d, 0.0D), 255.0D);
/*     */         }
/* 116 */         this.raster.setPixel(k, j, arrayOfDouble1);
/*     */       }
/*     */     }
/*     */   }
/*     */ }


/* Location:              M:\shared_for_vm\repository\challs\NC\stega\space_red_trumps\tmp\!\Spreader.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */