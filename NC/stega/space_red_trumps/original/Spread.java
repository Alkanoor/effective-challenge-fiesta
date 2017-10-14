/*    */ import java.awt.image.BufferedImage;
/*    */ import java.io.IOException;
/*    */ import java.io.PrintStream;
/*    */ import java.security.MessageDigest;
/*    */ import java.security.NoSuchAlgorithmException;
/*    */ import javax.imageio.ImageIO;
/*    */ 
/*    */ 
/*    */ public class Spread
/*    */ {
/*    */   private static void usage()
/*    */   {
/* 13 */     System.err.println("***********************************************************************\nUsage:\n\tjava Spreader stegomessage key\n\nCaractères permis dans le stégomessage: majuscules, minuscules, chiffres, espace.\nLa clé peut être n'importe quoi.\nLe résultat est au format PNG.\nUtilisez l'entrée et la sortie standard.\nExemples:\n\tjava Spread          \"hi world\" ü63RS739z°r <input.jpg >output.png\n\tjava -jar  Spread.jar ...\n\nTODO: implémenter le décodage.\n************************************************************************\n");
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 27 */     System.exit(0);
/*    */   }
/*    */   
/*    */   private static void error(Exception e, String txt)
/*    */   {
/* 32 */     e.printStackTrace();
/* 33 */     error(txt);
/*    */   }
/*    */   
/*    */   private static void error(String txt) {
/* 37 */     System.err.println("\n" + txt);
/* 38 */     System.exit(1);
/*    */   }
/*    */   
/*    */   public static void main(String[] args)
/*    */   {
/* 43 */     if (args.length != 2)
/*    */     {
/* 45 */       usage();
/*    */     }
/*    */     
/*    */     try
/*    */     {
/* 50 */       String msgString = args[0];
/* 51 */       String keyString = args[1];
/* 52 */       BufferedImage image = ImageIO.read(System.in);
/* 53 */       if (image == null)
/* 54 */         error("Format d'image non-reconnu ?");
/* 55 */       MessageDigest md = MessageDigest.getInstance("MD5");
/* 56 */       Spreader spr = new Spreader(keyString, image, md);
/* 57 */       spr.makeMark(msgString, 4, 1.0D);
/* 58 */       ImageIO.write(image, "PNG", System.out);
/*    */     }
/*    */     catch (InvalidStegoMessageException e)
/*    */     {
/* 62 */       System.err.println("Le stégomessage contient des caractères interdits.\n");
/* 63 */       usage();
/*    */     }
/*    */     catch (NoSuchAlgorithmException e)
/*    */     {
/* 67 */       error(e, "Votre système n'implémente pas MD5.");
/*    */     }
/*    */     catch (IOException e)
/*    */     {
/* 71 */       error(e, "Échec de lecture/écriture de l'image.");
/*    */     }
/*    */   }
/*    */ }


/* Location:              M:\shared_for_vm\repository\challs\NC\stega\space_red_trumps\tmp\!\Spread.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */