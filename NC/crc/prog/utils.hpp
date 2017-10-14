#ifndef UTIL_HPP
#define UTIL_HPP


#include <ostream>
#include <vector>
#include <array>


namespace Utils
{
    template <typename T>
    std::ostream& write_vec(const std::vector<T>& to_write, std::ostream& out, char sep = ' ', bool endline = false);

    template <typename T, size_t N>
    std::ostream& write_vec(const std::array<T,N>& to_write, std::ostream& out, char sep = ' ', bool endline = false);

    template <typename T, typename U=T>
    std::ostream& write_vec(const std::vector<std::vector<T> >& to_write, std::ostream& out, char sep = ' ', bool endline = true, bool additional_endline = false);

    template <typename T, size_t N, typename U=T>
    std::ostream& write_vec(const std::array<std::vector<T>,N>& to_write, std::ostream& out, char sep = ' ', bool endline = true, bool additional_endline = false);
}

template <typename T>
std::ostream& Utils::write_vec(const std::vector<T>& to_write, std::ostream& out, char sep, bool endline)
{
    for(const T& it : to_write)
    {
        out<<it<<sep;
        if(endline)
            out<<std::endl;
    }
    return out;
}

template <typename T, size_t N>
std::ostream& Utils::write_vec(const std::array<T,N>& to_write, std::ostream& out, char sep, bool endline)
{
    for(const T& it : to_write)
    {
        out<<it<<sep;
        if(endline)
            out<<std::endl;
    }
    return out;
}

template <typename T, typename U>
std::ostream& Utils::write_vec(const std::vector<std::vector<T> >& to_write, std::ostream& out, char sep, bool endline, bool additional_endline)
{
    for(const std::vector<T>& v : to_write)
    {
        for(const T& it : v)
            out<<(U)it<<sep;
        if(endline)
            out<<std::endl;
    }
    if(additional_endline)
        out<<std::endl;
    return out;
}

template <typename T, size_t N, typename U>
std::ostream& Utils::write_vec(const std::array<std::vector<T>,N>& to_write, std::ostream& out, char sep, bool endline, bool additional_endline)
{
    for(const std::vector<T>& v : to_write)
    {
        for(const T& it : v)
            out<<(U)it<<sep;
        if(endline)
            out<<std::endl;
    }
    if(additional_endline)
        out<<std::endl;
    return out;
}


template <typename T>
std::ostream& operator << (std::ostream& out, const std::vector<T>& to_write)
{
    return Utils::write_vec(to_write, out);
}

template <typename T, size_t N>
std::ostream& operator << (std::ostream& out, const std::array<T,N>& to_write)
{
    return Utils::write_vec(to_write, out);
}


#endif
