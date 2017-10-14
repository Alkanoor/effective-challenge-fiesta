#include "Constants.h"

#include <cassert>


std::string Utils::clean(const std::string& msg)
{
    std::string ret;
    for(unsigned char c : msg)
        if((c>='A' && c<='Z') || (c>='a' && c<='z') ||(c>='0' && c<='9'))
            ret += c;
    return ret;
}

std::vector<int> Utils::convert_alpha_to_num(const std::string& m)
{
    std::vector<int> ret(m.size());
    for(unsigned int i=0; i<m.size(); i++)
        ret[i] = m[i]-'A';
    return ret;
}

std::string Utils::vigenere(const std::string& charset, const std::string& msg, const std::vector<int>& offsets, bool direction)
{
    std::string ret;
    auto corresp = map_from_charset(charset);
    unsigned int charset_size = charset.size();
    unsigned int offsets_size = offsets.size();
    for(unsigned int i=0; i<msg.size(); i++)
        if(direction)
            ret += charset[(((corresp[msg[i]]+offsets[i%offsets_size])%charset_size)+charset_size)%charset_size];
        else
            ret += charset[(((corresp[msg[i]]-offsets[i%offsets_size])%charset_size)+charset_size)%charset_size];
    return ret;
}

std::string Utils::permutation(const std::string& charset, const std::string& msg, const std::vector<int>& permut, bool direction)
{
    return "";
}

std::map<char, int> Utils::map_from_charset(const std::string& charset)
{
    std::map<char, int> ret;
    for(unsigned int i=0; i<charset.size(); i++)
        ret[charset[i]] = (int)i;
    return ret;
}

std::map<char, int> Utils::count(const std::string& msg)
{
    std::map<char, int> counter;

    for(unsigned int i=0;i<msg.size();i++)
        if(!counter.count(msg[i]))
            counter[msg[i]] = 1;
        else
            counter[msg[i]]++;

    return counter;
}

float Utils::IC(const std::string& msg)
{
    std::map<char, int> counter = count(msg);

    float ret = 0;
    for(std::map<char, int>::iterator it=counter.begin();it!=counter.end();it++)
        ret += it->second*(it->second-1);

    return ret/(float)(msg.size()*(msg.size()-1));
}

/** abcdefg =>
    vertical = true :    | vertical = false :
    |a d g|              | |a b c|
    |b e ?|              | |d e f|
    |c f ?|              | |g ? ?|
**/
Matrix Utils::convert_string_to_mat(const std::string& txt, const std::map<char, int>& convertion_map, unsigned int M, unsigned int N, bool vertical)
{
    Matrix ret(M, Vec(N, 0));

    if(vertical)
        for(unsigned int i=0; i<M; i++)
            for(unsigned int j=0; j<N; j++)
                ret[i][j] = convertion_map.at(txt[i+j*M]);
    else
        for(unsigned int i=0; i<M; i++)
            for(unsigned int j=0; j<N; j++)
                ret[i][j] = convertion_map.at(txt[j+i*N]);

    return ret;
}

std::string Utils::convert_mat_to_string(const Matrix& mat, const std::map<int, char>& convertion_map, bool vertical)
{
    if(!mat.size())
        return "";

    unsigned int M = mat.size();
    unsigned int N = mat[0].size();

    std::string ret;

    if(!vertical)
        for(unsigned int i=0; i<M; i++)
            for(unsigned int j=0; j<N; j++)
                ret += convertion_map.at(mat[i][j]);
    else
        for(unsigned int j=0; j<N; j++)
            for(unsigned int i=0; i<M; i++)
                ret += convertion_map.at(mat[i][j]);

    return ret;
}

int Utils::inverseMod36(int a)
{
    for(int i=0;i<36;i++)
        if((((a*i)%36)+36)%36==1)
            return i;
    return -1;
}

Matrix Utils::rescaleMod36(const Matrix& m)
{
    if(!m.size())
        return Matrix();

    Matrix ret = m;
    unsigned int M = ret.size();
    unsigned int N = ret[0].size();
    for(unsigned int i=0; i<M; i++)
        for(unsigned int j=0; j<N; j++)
            ret[i][j] = m[i][j]%36;
    return ret;
}

Matrix Utils::prod(const Matrix &m1, const Matrix &m2)
{
    if(!m1.size() || m1[0].size() != m2.size())
        return Matrix();

    unsigned int M = m1.size();
    unsigned int N = m1[0].size();
    unsigned int O = m2[0].size();

    Matrix m3(M, Vec(O, 0));

    for(unsigned int i=0;i<M;i++)
        for(unsigned int j=0;j<O;j++)
        {
            int s = 0;
            for(unsigned int k=0;k<N;k++)
                s += m1[i][k]*m2[k][j];
            m3[i][j] = s;
        }

    return m3;
}

int Utils::det(const Matrix &mat)
{
    assert(mat.size()==3 && mat[0].size()==3);

    int ret = 0;
    for(unsigned int i=0;i<3;i++)
    {
        int temp = mat[(i+1)%3][1]*mat[(i+2)%3][2]-mat[(i+2)%3][1]*mat[(i+1)%3][2];
        ret += mat[i][0]*temp;
    }

    return ret;
}

Matrix Utils::inverse(const Matrix &mat)
{
    assert(mat.size()==3 && mat[0].size()==3);

    int d = inverseMod36(det(mat));

    Matrix ret(3, Vec(3, 0));
    for(unsigned int i=0;i<3;i++)
        for(unsigned int j=0;j<3;j++)
            ret[j][i] = (((d*(mat[(i+1)%3][(j+1)%3]*mat[(i+2)%3][(j+2)%3]-mat[(i+2)%3][(j+1)%3]*mat[(i+1)%3][(j+2)%3]))%36)+36)%36;

    return ret;
}
