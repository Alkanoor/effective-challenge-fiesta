#include <stdint.h>

#define offset 32
#define N (1<<32)

class HashMap
{
    public:
        HashMap(int size_pool = 0x80000, int max = 10);
        ~HashMap();

        bool add_and_check(unit64_t index);

        void resize_pool();

    private:
        char type[N];
        uint64_t* val[N];

        int pool_size;
        int nb_pool;
        int* cur_pool;
        int** pools;
        int cur;
};
