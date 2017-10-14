#include "utils.hpp"
#include "crc64.hpp"

#include <iostream>
#include <chrono>
#include <ctime>


int itere2(const std::vector<std::vector<int> >& taken, int n, int x, int y, int w, int h, uint64_t cur_crc, const std::vector<std::vector<char> >& T, const std::chrono::system_clock::time_point& begin, int& total, int& total_reached, bool going_down)
{
    if(total%10000==0)
    {
        std::chrono::microseconds ms = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now()-begin);
        if(ms.count()>=1000000)
            return 0;
    }

    total++;

    //std::vector<std::vector<int> > taken_cpy = taken;
    //taken_cpy[y][x] = n+1;
    if(going_down)
        y += 1;
    else
        y -= 1;

    if(y>=w)
    {
        total_reached++;
        if(rand()%10000==0)
        {
            //std::cout<<"Reached the end !! "<<n<<" "<<x<<" "<<y<<" "<<total<<std::endl;
            //Utils::write_vec(taken_cpy, std::cout);
        }
        return total_reached;
    }
    for(int x_new=0; x_new<(w-y); x_new++)
    {
        /*taken_cpy = taken;
        for(int i=x; i<=x_new; i++)
            taken_cpy[y-1][i] = n+1;
        for(int i=x; i>=x_new; i--)
            taken_cpy[y-1][i] = n+1;*/
        itere2(taken, n+1, x_new, y, w, h, cur_crc, T, begin, total, total_reached, going_down);
    }
}

int main()
{
    generate_table();

    UINT64 result = 0;
    result = next_crc_going_down(result, 0x16);
    result = next_crc_going_down(result, 0x1a);
    result = next_crc_going_down(result, 0x65);
    result = next_crc_going_down(result, 0x3b);
    result = next_crc_going_down(result, 0x38);
    printf("result0: %016I64X\n", result);

    UINT64 result2 = result;
    result2 = next_crc_going_up(result2, 0x38);
    result2 = next_crc_going_up(result2, 0x3b);
    result2 = next_crc_going_up(result2, 0x65);
    result2 = next_crc_going_up(result2, 0x1a);
    result2 = next_crc_going_up(result2, 0x16);
    printf("result0: %016I64X\n", result2);

    std::vector<std::vector<char> > T(20, std::vector<char>(20, 0));
    for(int i=0; i<20; i++)
        for(int j=0; j<20; j++)
            if(i+j!=0 && i+j!=38)
                T[i][j] = rand()%256;

    Utils::write_vec(T, std::cout);


    return 0;
}
