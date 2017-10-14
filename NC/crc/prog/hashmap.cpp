#include "hashmap.hpp"


HashMap::HashMap(int size_pool, int max) :
    pool_size(size_pool),
    max_nb_pool(max),
    nb_pool(0)
{
    resize_pool();
    pools = new int*[max_nb_pool];
}

HashMap::~HashMap()
{
    for(int i=0;i<nb_pool;i++)
        delete pools[i];
    delete pools;
}

bool HashMap::add_and_check(unit64_t index)
{
    if(!type[index&(N-1)])
    {
        type[index&(N-1)] = 1;
        val[index&(N-1)] = (uint64_t*)(index>>offset);
    }
    else
    {
        cur_pool[cur++] = val[index&(N-1)];
        cur_pool[cur++] = nullptr;
        if(type[index&(N-1)]==1)
        {
            type[index&(N-1)] = 2;
            val[index&(N-1)] = (uint64_t*)&cur_pool[cur-1];
        }
        else
        {
            uint64_t* temp = val[index&(N-1)];
            while(*temp)
                temp = *temp;
            *temp = (uint64_t*)&cur_pool[cur-1]; 
        }

        if(cur>=pool_size)
            resize_pool();
    }
}

void HashMap::resize_pool()
{
    cur_pool = new int[pool_size];
    pools[nb_pool++] = cur_pool;
    if(nb_pool>=max_nb_pool)
    {
        std::cerr<<"Not enough pool allocated ... "<<std::endl;
        exit(-1);
    }
    cur = 0;
}
