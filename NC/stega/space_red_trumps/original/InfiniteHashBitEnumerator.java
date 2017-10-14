/*    */ import java.security.MessageDigest;
/*    */ 
/*    */ class InfiniteHashBitEnumerator extends BitEnumerator
/*    */ {
/*    */   MessageDigest md;
/*    */   int curBit;
/*    */   int hashCount;
/*    */   
/*    */   InfiniteHashBitEnumerator(byte[] paramArrayOfByte, MessageDigest paramMessageDigest) {
/* 10 */     super(paramMessageDigest.digest(paramArrayOfByte), 8);
/* 11 */     this.md = paramMessageDigest;
/* 12 */     this.hashCount = 0;
/*    */   }
/*    */   
/*    */   public int next()
/*    */   {
/* 17 */     this.curBit = super.next();
/* 18 */     if (this.curBit == -1)
/*    */     {
/* 20 */       this.md.update(Long.toString(this.hashCount).getBytes());
/* 21 */       this.hashCount += 1;
/* 22 */       this.toEnum = this.md.digest(this.toEnum);
/* 23 */       this.curBit = super.next();
/*    */     }
/* 25 */     return this.curBit;
/*    */   }
/*    */ }


/* Location:              M:\shared_for_vm\repository\challs\NC\stega\space_red_trumps\tmp\!\InfiniteHashBitEnumerator.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */