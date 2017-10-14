class BitEnumerator
{
  protected byte[] toEnum;
  private int byteIndex = 0;
  private int bitsPerByte;
  private int rightShift;
  
  BitEnumerator(byte[] paramArrayOfByte)
  {
    this(paramArrayOfByte, 8);
  }
  
  BitEnumerator(byte[] paramArrayOfByte, int paramInt)
  {
    this.toEnum = paramArrayOfByte;
    this.bitsPerByte = paramInt;
    this.rightShift = paramInt;
  }
  
  public int next()
  {
    if (--this.rightShift < 0)
    {
      if (++this.byteIndex >= this.toEnum.length)
      {
        this.byteIndex = -1;
        return -1;
      }
      this.rightShift = (this.bitsPerByte - 1);
    }
    return this.toEnum[this.byteIndex] >> this.rightShift & 0x1;
  }
}
