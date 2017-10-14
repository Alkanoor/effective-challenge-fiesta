#include "enigma.hpp"


void Enigma::reset(const std::array<unsigned char, 3>& s, const std::array<int, 3>& ro, const std::array<unsigned char, 3>& ri, const std::map<unsigned char, unsigned char>& corresp, int reflector)
{
    settings = s;
    rotors = ro;
    ringstellung = ri;
    reflector_index = reflector;
    correspondances = corresp;
    //std::cout<<"Reseting "<<s<<" :: "<<ro<<" :: "<<ringstellung<<" with index "<<reflector_index<<std::endl;
}

unsigned char Enigma::apply_rotor(unsigned char c, int offset, const std::string& key)
{
    return subst(subst(c, offset, key), -offset);
}

unsigned char Enigma::reflect(unsigned char c)
{
    return subst(c, 0, reflectorkey[reflector_index]);
}

unsigned char Enigma::subst(unsigned char c, int offset, const std::string& key)
{
    return key[((c-'A')+offset+26*2)%26];
}

void Enigma::advance_rotor()
{
    for(int i=0; i<notch[rotors[1]].size(); i++)
        if(settings[1] == notch[rotors[1]][i])
        {
            settings[0] = subst(settings[0],1);
            settings[1] = subst(settings[1],1);
        }
    for(int i=0; i<notch[rotors[2]].size(); i++)
        if(settings[2] == notch[rotors[2]][i])
            settings[1] = subst(settings[1],1);
    settings[2] = subst(settings[2],1);
}

unsigned char Enigma::encipher_char(unsigned char c, bool debug)
{
    if(debug)
    {
        std::cout<<"offsets"<<std::endl;
    }
    if(correspondances.count(c))
        c = correspondances[c];
    advance_rotor();
    int offset = 0;
    for(int i=0;i<3;i++)
    {
        offset = settings[2-i]-ringstellung[2-i];
        if(debug)
        {
            std::cout<<offset<<std::endl;
            std::cout<<rotorkey[rotors[2-i]]<<std::endl;
        }
        c = apply_rotor(c, offset, rotorkey[rotors[2-i]]);
    }
    c = reflect(c);
    for(int i=0;i<3;i++)
    {
        offset = settings[i]-ringstellung[i];
        if(debug)
        {
            std::cout<<offset<<std::endl;
        }
        c = apply_rotor(c, offset, invrotor[rotors[i]]);
    }
    if(correspondances.count(c))
        c = correspondances[c];
    return c;
}

void Enigma::set_cipher(const std::string& c)
{cipher = c; clear.resize(c.size());}

const std::string& Enigma::cipher_decipher()
{
    unsigned char tm;
    for(int i=0; i<cipher.size(); i++)
        if(is_char_ok(cipher[i]))
        {
            tm = encipher_char(norm_ok(cipher[i]));
            clear[i] = tm;
        }
        else
            clear[i] = cipher[i];
    return clear;
}

bool Enigma::is_config_ok(const std::array<unsigned char, 3>& setting, int offset)
{
    for(unsigned char c='A'; c<='Z'; c++)
    {
        settings = setting;
        unsigned char res1 = encipher_char(c);
        for(int i=1; i<offset; i++)
            advance_rotor();
        unsigned char res2 = encipher_char(res1);
        if(res2==c)
            return true;
    }
    return false;
}

bool Enigma::is_char_ok(unsigned char c)
{
    if(c>='A'&&c<='Z')
        return true;
    if(c>='a'&&c<='z')
        return true;
    return false;
}

unsigned char Enigma::norm_ok(unsigned char c)
{
    if(c>='A'&&c<='Z')
        return c;
    else
        return c-'a'+'A';
}


std::array<std::string, 8> Enigma::rotorkey{"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                                            "VZBRGITYUPSDNHLXAWMJQOFECK", "JPGVOUMFYQBENHZRDKASXLICTW", "NZJHGRCXMYSWBOUFAIVLPEKQDT", "FKQHTLXOCBJSPDZRAMEWNIUYGV"};

std::array<std::string, 8> Enigma::invrotor{"UWYGADFPVZBECKMTHXSLRINQOJ", "AJPCZWRLFBDKOTYUQGENHXMIVS", "TAGBPCSDQEUFVNZHYIXJWLRKOM", "HZWVARTNLGUPXQCEJMBSKDYOIF",
                                            "QCYLXWENFTZOSMVJUDKGIARPHB", "SKXQLHCNWARVGMEBJPTYFDZUIO", "QMGYVPEDRCWTIANUXFKZOSLHJB", "QJINSAYDVKBFRUHMCPLEWZTGXO"};

std::array<std::string, 3> Enigma::reflectorkey{"EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"};

typedef std::vector<unsigned char> v;

std::array<std::vector<unsigned char>, 8> Enigma::notch{v({'Q'}),v({'E'}),v({'V'}),v({'J'}),v({'Z'}),v({'Z','M'}),v({'Z','M'}),v({'Z','M'})};
