#include <stdexcept>

Polyalphabetic_Key::Polyalphabetic_Key(int key_length) :
    key_length_(key_length)
{
    correspondance.resize(key_length);
}

const std::array<std::vector<char>, 4>& Polyalphabetic_Key::get_forbidden_chars(int index, const std::string& cur_ngram) throw ()
{
    if(cur_ngram.size() != 4)
        throw std::runtime_error("Ngram is not a 4 gram in Polyalphabetic_Key");

    for(int i=0; i<4; i++)
    {
        if(cur_ngram[i]<'A'||cur_ngram[i]>'Z')
            throw std::runtime_error("Ngram is not caps locked : '"+cur_ngram[i]+"'");
        std::vector<char> tmp;
        if(correspondance[index%key_length].count(cur_ngram[i]))
        {
            tmp.resize(25);
            int o=0;
            for(int j=0; j<26; j++)
                if('A'+j != cur_ngram[i])
                {
                    tmp[o] = cur_ngram[i];
                    o++;
                }
        }
        forbidden[i] = tmp;
    }
    return forbidden;
}

char Polyalphabetic_Key::get_correspondance(int index, char cipher) const
{
    if(correspondance[index%key_length_].count(cipher))
        return correspondance[index%key_length_][cipher];
    return '?';
}

std::string Polyalphabetic_Key::decipher(const std::string& cipher, std::vector<bool>& ngrams_set)
{
    ngrams_set.resize(cipher.size()-3);
    std::string ret = cipher;
    int cur = 0;
    for(int i=0; i<(int)cipher.size(); i++)
    {
        if(correspondance[i%key_length_].count(cipher[i]))
        {
            ret[i] = correspondance[i%key_length_][cipher[i]];
            cur++;
        }
        else
            cur = 0;
        if(cur>=3)
            ngrams_set[i-3] = true;
        else
            ngrams_set[i-3] = false;
    }
    return ret;
}

Polyalphabetic_Key Polyalphabetic_Key::derive_add(int index, const std::string& 4gram_ciphered, const std::string& 4gram_plain) throw ()
{
    if(4gram_ciphered.size()!=4 || 4gram_plain.size()!=4)
        throw std::runtime_error("Ngrams are not 4grams in derivation process add");

    for(int i=0; i<4; i++)
        if(correspondance[(i+index)%key_length_].count(4gram_ciphered[i]) &&
           (correspondance[(i+index)%key_length_][4gram_ciphered[i]] != 4gram_plain[i] ||
           correspondance[(i+index)%key_length_][4gram_ciphered[i]] == '?'))
            throw std::runtime_error("Minimum match in correspondance not reached in add");
        else
            correspondance[(i+index)%key_length_][4gram_ciphered[i]] = 4gram_plain[i];
}

Polyalphabetic_Key Polyalphabetic_Key::derive_delete(int index, const std::string& 4gram_ciphered) throw ()
{
    if(4gram_ciphered.size()!=4)
        throw std::runtime_error("Ngram is not 4gram in derivation process delete");

    for(int i=0; i<4; i++)
        if(!correspondance[(i+index)%key_length_].count(4gram_ciphered[i]) ||
          correspondance[(i+index)%key_length_][4gram_ciphered[i]] != '?')
            throw std::runtime_error("Minimum match in correspondance not reached in delete");
        else
            correspondance[(i+index)%key_length_][4gram_ciphered[i]] = '?';
}
