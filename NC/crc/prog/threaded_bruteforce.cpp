#include "threaded_bruteforce.hpp"


std::set<UINT64> Threaded_bruteforce::up;
std::set<UINT64> Threaded_bruteforce::down;
bool Threaded_bruteforce::up_accessed = false;
bool Threaded_bruteforce::down_accessed = false;
std::mutex Threaded_bruteforce::mutex_on_up;
std::mutex Threaded_bruteforce::mutex_on_down;
int Threaded_bruteforce::total_up = 0;
int Threaded_bruteforce::total_down = 0;

int Threaded_bruteforce::w = 0;
int Threaded_bruteforce::h = 0;
int Threaded_bruteforce::counter_id = 0;
std::vector<std::vector<char> > Threaded_bruteforce::T;
std::chrono::system_clock::time_point Threaded_bruteforce::begin;


Threaded_bruteforce::Threaded_bruteforce() :
    thread_id(counter_id),
    thread(0),
    has_admin_right_on_set(false)
{
    if(counter_id<=1)
        has_admin_right_on_set = true;
    chosen_path.push_back(counter_id);
    up_or_down = counter_id%2==0;
    counter_id++;
    assert(thread_id<w-2);
}

Threaded_bruteforce::~Threaded_bruteforce()
{
    if(thread)
        delete thread;
}

void Threaded_bruteforce::run()
{
    thread = new std::thread(std::bind(&Threaded_bruteforce::run,this));
}

void Threaded_bruteforce::run()
{
    if(up_or_down)
        itere(w-1, h-1, UINT64(0x4242424242424242));
    else
        itere(0, 0, 0);
}

char Threaded_bruteforce::itere(int x, int y, UINT64 cur_crc, int depth)
{
    if(up_or_down)
    {
        if(total_up%10000==0)
        {
            std::chrono::microseconds ms = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now()-begin);
            if(ms.count()>=1000000)
                return 1;
        }
        total_up++;
        y += 1;
        if(y>=w)
        {
            //reached the end
            return k;
        }

        crc = next_crc_going_up(crc, T[y][x]);

        UINT64 cpy = crc;
        if(depth<1||depth>(int)chosen_path.size()||x==chosen_path[depth-1])
        {
            char tmp = itere(x, y, cpy, depth+1);
            if(tmp>1)
                std::cout<<"YESS We FOUND IT ! "<<x<<" "<<y<<" "<<total_up<<std::endl;
            if(tmp)
                return tmp;
        }

        for(int x_new=x+1; x_new<(w-y); x_new++)
        {
            cpy = next_crc_going_up(cpy, T[y][x_new]);
            if(depth<1||depth>(int)chosen_path.size()||x_new==chosen_path[depth-1])
            {
                char tmp = itere(x_new, y, cpy, depth+1);
                if(tmp>1)
                    std::cout<<"YESS We FOUND IT ! "<<x<<" "<<y<<" "<<total_up<<std::endl;
                if(tmp)
                    return tmp;
            }
        }
        cpy = crc;
        for(int x_new=x-1; x_new>=0; x_new--)
        {
            cpy = next_crc_going_up(cpy, T[y][x_new]);
            if(depth<1||depth>(int)chosen_path.size()||x_new==chosen_path[depth-1])
            {
                char tmp = itere(x_new, y, cpy, depth+1);
                if(tmp>1)
                    std::cout<<"YESS We FOUND IT ! "<<x<<" "<<y<<" "<<total_up<<std::endl;
                if(tmp)
                    return tmp;
            }
        }
    }
    else
    {
        if(total_down%10000==0)
        {
            std::chrono::microseconds ms = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now()-begin);
            if(ms.count()>=1000000)
                return 1;
        }
        total_down++;
        x -= 1;
        if(x<=1)
        {
            //reached the end
            return k;
        }

        crc = next_crc_going_down(crc, T[y][x]);

        UINT64 cpy = crc;
        if(depth<1||depth>(int)chosen_path.size()||y==h-1-chosen_path[depth-1])
        {
            char tmp = itere(x, y, cpy, depth+1);
            if(tmp>1)
                std::cout<<"YESS We FOUND IT ! "<<x<<" "<<y<<" "<<total_down<<std::endl;
            if(tmp)
                return tmp;
        }

        for(int y_new=y+1; y_new<h; y_new++)
        {
            cpy = next_crc_going_down(cpy, T[y_new][x]);
            if(depth<1||depth>(int)chosen_path.size()||y_new==h-1-chosen_path[depth-1])
            {
                char tmp = itere(x, y_new, cpy, depth+1);
                if(tmp>1)
                    std::cout<<"YESS We FOUND IT ! "<<x<<" "<<y<<" "<<total_down<<std::endl;
                if(tmp)
                    return tmp;
            }
        }
        cpy = crc;
        for(int y_new=y-1; y_new>(h-x); y_new--)
        {
            cpy = next_crc_going_down(cpy, T[y_new][x]);
            if(depth<1||depth>(int)chosen_path.size()||y_new==h-1-chosen_path[depth-1])
            {
                char tmp = itere(x, y_new, cpy, depth+1);
                if(tmp>1)
                    std::cout<<"YESS We FOUND IT ! "<<x<<" "<<y<<" "<<total_down<<std::endl;
                if(tmp)
                    return tmp;
            }
        }
    }

    return 0;
}
