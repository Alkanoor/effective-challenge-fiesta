#ifndef LOG_TABLE_H
#define LOG_TABLE_H


#include <vector>


class Log_table
{
    public:
        static void set_size(int size);
        static std::vector<float> log_table;
};


#endif
