#include "util.hpp"


std::string clean(const std::string& base)
{
    std::string ret;
    for(int i=0; i<base.size(); i++)
        if(base[i]>=32&&base[i]<=128)
            ret += base[i];
    return ret;
}

std::map<unsigned char, int> count_alpha(const std::string& s, int& tot)
{
    std::map<unsigned char, int> ret;
    tot = 0;
    for(auto i : s)
        if(i>='A'&&i<='Z')
        {
            tot++;
            if(ret.count(i))
                ret[i] += 1;
            else
                ret[i] = 1;
        }
    return ret;
}

float IC(const std::string& s)
{
    int tot;
    std::map<unsigned char, int> tmp = count_alpha(s, tot);
    float score = 0;
    for(auto i : tmp)
        score += i.second*(i.second-1);
    float l = tot;
    if(l>1)
        return score/(l*(l-1));
    else
        return 0;
}
