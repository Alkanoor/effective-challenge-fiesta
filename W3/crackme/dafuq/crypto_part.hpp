#include <openssl/evp.h>
#include <openssl/md5.h>
#include <string>
#include <cstdio>
#include <cmath>
#include <map>


void print_hex(const std::string& s)
{
    for(auto i : s)
        printf("%02x", (unsigned char)i);
    printf("\n");
}

void print_hex(unsigned char* a, size_t len)
{
    for(size_t i=0; i<len; i++)
        printf("%02x", a[i]);
    printf("\n");
}

double log2(double n)
{
    return log(n)/log(2);
}

double entropy(unsigned char* text, size_t len)
{
    std::map<char, int> frequencies;
    for(size_t i=0; i<len; i++)
        if(frequencies.count(text[i]))
            frequencies[text[i]]++;
        else
            frequencies[text[i]] = 1;

    double infocontent = 0;
    for(std::pair<char, int> p : frequencies)
    {
        double freq = static_cast<double>(p.second)/(double)len ;
        infocontent += freq * log2(freq);
    }
    infocontent *= -1;

    return infocontent/log2(len);
}

const unsigned char* ciphertext = (const unsigned char*)"\x82\x10\xBF\x7D\x6C\xF3\xF8\xFF\xD2\x8C\x79\x4F\x69\xC0\xFE\x55\x01\xC2\xBB\xFF\xD5\x45\x68\x65\xB2\xE1\x9E\x63\xC3\x4E\x43\xB0\x0D\x29\x9C\xB5\x07\xF1\x45\x98\x6A\x36\xBA\xF9\xB1\x4F\x0B\x48\x58\xE2\xFC\xB7\xE0\xDE\x0C\x04\x0B\xE2\x65\x56\x8D\x76\xDE\xD7\xA8\xEA\x5A\x97\x3F\x40\x13\x92\x74\x69\x63\x69\x71\x1C\x6B\x89\xCF\x0F\xC3\xE8\x80\xC5\x59\xF1\x1A\x20\xCF\x89\xA6\xCE\x2F\xF3\x5D\x53\x67\xAB\xDB\x10\xB1\xA6\xAC\xB8\x05\x4E\xC2\x4E\xA5\x73\x6C\xCD\xB2\x2D\xB2\xD6\x24\xAA\xCC\x5B\x50\x29\x3B\x0B\x9C\x4E\xA3\x21\xB4\xAA\x7D\x99\x7B\x33\x7F\x51\x18\x4D\x48\xD7\x98\xF3\x00\x51\x30\x12\xB0\x1D\x03\x76\x00\x12\x04\x60\x81\x7F\x33\x23\x00\xCE\xE6\xE6\xED\xA9\xE2\xEC\xF0\xA9\xA8\x83\x00\xCB\xE8\xED\xA9\xE2\xEC\xF0\xA7\x83\x00\x00";

double compute_entropy_from_string(const std::string& path)
{
    const char* tmp_hash = (const char*)MD5((const unsigned char*)path.c_str(), path.size(), NULL);
    print_hex(std::string(tmp_hash));

    auto sha = EVP_sha1();
    unsigned char key[32], iv[16];
    EVP_BytesToKey(EVP_aes_256_cbc(), sha, (const unsigned char*)"90\x00\x00\x31\xd4\x00\x00", (const unsigned char*)(tmp_hash), 16, 5, key, iv);
    print_hex(key, 32);
    print_hex(iv, 16);

    auto ctx = EVP_CIPHER_CTX_new();
    if(!ctx)
        std::cerr<<"Error"<<std::endl;

    if(1 != EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv))
        std::cerr<<"Error decrypt init ex"<<std::endl;

    int len;
    unsigned char plaintext[2000];
    if(1 != EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, 0xb4))
        std::cerr<<"Error decrypt update"<<std::endl;

    print_hex(plaintext, 0xb0);
    //std::cout<<entropy(plaintext, 0xb0)<<" "<<entropy((unsigned char*)"0", 1)<<" "<<entropy((unsigned char*)"000000", 6)<<" "<<entropy((unsigned char*)"abcdefg", 7)<<std::endl;

    return entropy(plaintext, 0xb0);
}
