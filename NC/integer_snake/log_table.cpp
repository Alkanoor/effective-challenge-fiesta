#include "log_table.h"

#include <cmath>


std::vector<float> Log_table::log_table;


void Log_table::set_size(int size)
{
    int prev_size = (int)log_table.size();
    log_table.resize(size);
    if(!prev_size&&size)
    {
        prev_size = 1;
        log_table[0] = -1;
    }
    for(int i=prev_size; i<size; i++)
        log_table[i] = log(i);
}
