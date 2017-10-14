import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.PrintStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.imageio.ImageIO;

public class Spread
{
  private static void usage()
  {
    System.err.println("***********************************************************************\nUsage:\n\tjava Spreader stegomessage key\n\nCaractères permis dans le stégomessage: majuscules, minuscules, chiffres, espace.\nLa clé peut être n'importe quoi.\nLe résultat est au format PNG.\nUtilisez l'entrée et la sortie standard.\nExemples:\n\tjava Spread          \"hi world\" ü63RS739z°r <input.jpg >output.png\n\tjava -jar  Spread.jar ...\n\nTODO: implémenter le décodage.\n************************************************************************\n");

    System.exit(0);
  }

  private static void error(Exception e, String txt)
  {
    e.printStackTrace();
    error(txt);
  }

  private static void error(String txt)
  {
    System.err.println("\n" + txt);
    System.exit(1);
  }

  public static void main(String[] args)
  {
    if (args.length != 2) {
      usage();
    }
    try
    {
      String msgString = args[0];
      String keyString = args[1];
      BufferedImage image = ImageIO.read(System.in);
      if (image == null) {
        error("Format d'image non-reconnu ?");
      }
      MessageDigest md = MessageDigest.getInstance("MD5");
      Spreader spr = new Spreader(keyString, image, md);
      spr.compute_array();
      //spr.smart_bruteforce(3, 10);
      //spr.smart_bruteforce_with_key(3, 15, "AAb");
      spr.smart_bruteforce_with_key(3, 20, "pli"); //p0odleB4rk

      //ImageIO.write(image, "PNG", System.out);
    }
    catch (NoSuchAlgorithmException e)
    {
      error(e, "Votre système n'implémente pas MD5.");
    }
    catch (IOException e)
    {
      error(e, "Échec de lecture/écriture de l'image.");
    }
  }
}
