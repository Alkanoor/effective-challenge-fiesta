/*    */ class BitEnumerator
/*    */ {
/*    */   protected byte[] toEnum;
/*  4 */   private int byteIndex = 0;
/*    */   private int bitsPerByte;
/*    */   private int rightShift;
/*    */   
/*    */   BitEnumerator(byte[] paramArrayOfByte)
/*    */   {
/* 10 */     this(paramArrayOfByte, 8);
/*    */   }
/*    */   
/*    */   BitEnumerator(byte[] paramArrayOfByte, int paramInt) {
/* 14 */     this.toEnum = paramArrayOfByte;
/* 15 */     this.bitsPerByte = paramInt;
/* 16 */     this.rightShift = paramInt;
/*    */   }
/*    */   
/*    */   public int next()
/*    */   {
/* 21 */     if (--this.rightShift < 0)
/*    */     {
/* 23 */       if (++this.byteIndex >= this.toEnum.length)
/*    */       {
/*    */ 
/*    */ 
/* 27 */         this.byteIndex = -1;
/* 28 */         return -1;
/*    */       }
/*    */       
/*    */ 
/* 32 */       this.rightShift = (this.bitsPerByte - 1);
/*    */     }
/* 34 */     return this.toEnum[this.byteIndex] >> this.rightShift & 0x1;
/*    */   }
/*    */ }


/* Location:              M:\shared_for_vm\repository\challs\NC\stega\space_red_trumps\tmp\!\BitEnumerator.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */