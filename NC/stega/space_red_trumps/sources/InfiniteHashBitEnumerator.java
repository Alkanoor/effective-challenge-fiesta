import java.security.MessageDigest;

class InfiniteHashBitEnumerator
  extends BitEnumerator
{
  MessageDigest md;
  int curBit;
  int hashCount;
  
  InfiniteHashBitEnumerator(byte[] paramArrayOfByte, MessageDigest paramMessageDigest)
  {
    super(paramMessageDigest.digest(paramArrayOfByte), 8);
    this.md = paramMessageDigest;
    this.hashCount = 0;
  }
  
  public int next()
  {
    this.curBit = super.next();
    if (this.curBit == -1)
    {
      this.md.update(Long.toString(this.hashCount).getBytes());
      this.hashCount += 1;
      this.toEnum = this.md.digest(this.toEnum);
      this.curBit = super.next();
    }
    return this.curBit;
  }
}
