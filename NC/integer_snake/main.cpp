#include "request_manager.h"
#include "thread.hpp"
//#include "c_socket.h"
#include "util.hpp"
#include "state.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <chrono>
#include <cmath>
#include <map>



float weight(const State& s)
{
    //auto start = std::chrono::steady_clock::now();
    float res = 1.0/(float)(100000+rand()%100000);
    /*auto end = std::chrono::steady_clock::now();
    auto diff = end - start;
    std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (4)"<<std::endl;*/

    //start = std::chrono::steady_clock::now();
    int tot = s.total_score();
    if(tot>0)
    {
        if((int)Log_table::log_table.size()>tot)
            res -= 8*Log_table::log_table[tot];
        else
            res -= 8*log(tot);
    }
    //end = std::chrono::steady_clock::now();
    //diff = end - start;
    //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (5)"<<std::endl;
    //start = std::chrono::steady_clock::now();
    res += s.differential();
    //end = std::chrono::steady_clock::now();
    //diff = end - start;
    //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (6)"<<std::endl;
    return res;
}


//static std::mutex global_mutex;

inline void analyse(std::map<float, State>* next_states, State& cur_state, State& tmp)
{
    //std::cout<<"Examining "<<counter<<std::endl;
    int nb_allowed;
    bool little_random = false, random = false, big_random = false;
    char* allowed = cur_state.allowed(nb_allowed);
    if(nb_allowed>5)
        random = true;
    else if(nb_allowed>3)
        little_random = true;
    /*else if(nb_allowed>2)
        little_random = true;
    else if(nb_allowed==2)
        little_random = rand()%5>3;
    */
    //std::cout<<s.score()<<" "<<nb_allowed<<std::endl;
    int a=0;
    for(int i=0;i<nb_allowed;i++)
    {
        if(random||big_random)
            a = rand()%2;
        if((!random&&!big_random)||a)
        {
            //auto start = std::chrono::steady_clock::now();
            cur_state.next_state(2*allowed[i], tmp);
            //auto end = std::chrono::steady_clock::now();
            //auto diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (4)"<<std::endl;
            //start = std::chrono::steady_clock::now();
            float w = weight(tmp);
            //end = std::chrono::steady_clock::now();
            //diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (5)"<<std::endl;
            //start = std::chrono::steady_clock::now();
            //global_mutex.lock();
            (*next_states)[w] = tmp;
            //global_mutex.unlock();
            //end = std::chrono::steady_clock::now();
            //diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (6)"<<std::endl;
        }
        if((!random&&!big_random)||!a)
        {
            //start = std::chrono::steady_clock::now();
            //weight(tmp);
            //end = std::chrono::steady_clock::now();
            //diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (3)"<<std::endl;
            cur_state.next_state(1+2*allowed[i], tmp);
            float w = weight(tmp);
            //global_mutex.lock();
            (*next_states)[w] = tmp;
            //global_mutex.unlock();
        }

        if(big_random)
            i += (6+rand()%12);
        else if(random)
            i += (3+rand()%6);
        else if(little_random)
            i += (1+rand()%4);
        else if(little_random)
            i += (rand()%5>=2);
    }
}

void analyse_global(std::map<float, State>* next_states, const std::vector<State*>& states, int size, State& tmp)
{
    for(int i=0; i<size; i++)
        analyse(next_states, *states[i], tmp);
}


#define LIMIT 750
#define MIN_TO_PRINT 20
#define N_THREADS 1


/*static C_socket sock;

void get_seeds(int& seed1, int& seed2, int& seed3)
{
    sock.send_message("a");
    std::istringstream iss(sock.recv_message());
    iss>>seed1>>seed2>>seed3;
}

void update_answer(bool send, const std::string& s="")
{
    if(send)
    {
        sock.send_message("1");
        sock.send_message(s);
    }
    else
        sock.send_message("0");
}*/


int str_to_int(const std::string& s)
{
    std::istringstream ss(s);
    int ret;
    ss>>ret;
    return ret;
}

template<typename Out>
void split(const std::string &s, char delim, Out result)
{
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim))
        *(result++) = item;
}


Request_manager query_seeds;
Request_manager send_answer;

void get_seeds(int& seed1, int& seed2, int& seed3)
{
    std::vector<std::string> seeds;

    while(seeds.size()<4)
    {
        seeds.clear();
        query_seeds.perform();
        std::string body = query_seeds.body();
        std::cout<<"Current body : "<<body<<std::endl;
        split(body, '\n', std::back_inserter(seeds));

        if(seeds.size() != 4)
            usleep(2000000);
        else
        {
            std::vector<std::string> tmp;
            for(int i=0; i<3; i++)
                split(seeds[i+1], '=', std::back_inserter(tmp));

            seed1 = str_to_int(tmp[1]);
            seed2 = str_to_int(tmp[3]);
            seed3 = str_to_int(tmp[5]);
        }
    }
}

void update_answer(bool send, const std::string& s="")
{
    if(send)
    {
        send_answer.set_url("https://www.newbiecontest.org/epreuves/prog/verifprintegersnake.php?path="+s);
        send_answer.perform();
        std::cout<<"Result :"<<std::endl;
        std::cout<<send_answer.header()<<std::endl;
        std::cout<<send_answer.body()<<std::endl;
    }
}


int limit_from_score(int score)
{
	if(score>29000)
		return LIMIT/7*3;
    else if(score>20000)
		return LIMIT/7*4;
	else if(score>14000)
		return LIMIT/7*5;
	else
		return LIMIT;
}

int main()
{
    query_seeds.set_url("https://www.newbiecontest.org/epreuves/prog/progintegersnake.php");
    query_seeds.set_cookie("SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1625593163%3Bi%3A3%3Bi%3A0%3B%7D; PHPSESSID=f0dfd2ecb5b8fd2fa2ea02606d7ade53");

    send_answer.set_cookie("SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1625593163%3Bi%3A3%3Bi%3A0%3B%7D; PHPSESSID=f0dfd2ecb5b8fd2fa2ea02606d7ade53");

    srand(time(NULL));
    Log_table::set_size(60000);

    std::vector<Thread*> threads;
    for(int i=0; i<N_THREADS-1; i++)
        threads.push_back(new Thread(i));
    State tmp_states[N_THREADS-1];

    int seed1=6818333, seed2=243209, seed3=8271387;

    int min_score = 32000;

    int scored=0, timed=0, failed=0;
    while(1)
    {
        get_seeds(seed1, seed2, seed3);
        std::cout<<"Seeds : "<<seed1<<" "<<seed2<<" "<<seed3<<std::endl;

        auto start = std::chrono::steady_clock::now();

        Random_generator::generator.reset(seed1, seed2, seed3);

        Mat<N, short> initial;
        for(int i=0;i<5;i++)
            for(int j=0;j<5;j++)
                initial[i][j] = Random_generator::generator.get_value(i*5+j);

        int initial_step = 25;
        State initial_state(initial_step);
        initial_state.reset(initial);
        initial_state.dump(std::cout);

        State final_state;

        std::vector<State> states(1, initial_state);
        int counter = 0, cur_limit = LIMIT;
        while(states.size())
        {
            int sizes[N_THREADS];
            std::vector<State*> split[N_THREADS];
            std::map<float,State> next_states[N_THREADS];

            //auto start = std::chrono::steady_clock::now();
            for(int i=0; i<N_THREADS; i++)
            {
                sizes[i] = 0;
                split[i].resize(states.size()/N_THREADS+2);
            }

            for(int i=0; i<(int)states.size(); i++)
            {
                split[i%N_THREADS][sizes[i%N_THREADS]] = &states[i];
                sizes[i%N_THREADS]++;
            }

            //auto end = std::chrono::steady_clock::now();
            //auto diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (1)"<<std::endl;
            //start = std::chrono::steady_clock::now();

            for(int i=0; i<N_THREADS-1; i++)
                Thread::add_to_thread_and_exec(i, std::bind(&analyse_global, &next_states[i+1], split[i+1], sizes[i+1], tmp_states[i]));
            State tmp;
            analyse_global(&next_states[0], split[0], sizes[0], tmp);

            for(int i=0; i<N_THREADS-1; i++)
                threads[i]->join();

            //end = std::chrono::steady_clock::now();
            //diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (2)"<<std::endl;
            //start = std::chrono::steady_clock::now();

            states.resize(cur_limit*N_THREADS);
            int cur = 0;
            for(int i=0; i<N_THREADS; i++)
            {
                if((int)next_states[i].size()>cur_limit)
                {
                    int a = 0;
                    for(auto it : next_states[i])
                    {
                        if(!a&&!(counter%100))
                        {
                            std::cout<<"First weight is "<<it.first<<" with "<<std::endl;
                            it.second.dump(std::cout);
                            std::cout<<"=> "<<it.second.differential()<<std::endl;
                            std::cout<<it.second.path()<<std::endl;
                        }
                        std::swap(states[cur], it.second);
                        cur++;
                        a++;
                        if(a>=cur_limit)
                        {
                            //std::cout<<"Limit is "<<i.first<<std::endl;
                            break;
                        }
                    }
                }
                else
                {
                    if(!next_states[i].size())
                        if(states[0].total_score()>final_state.total_score())
                            final_state = states[0];
                    //std::cout<<"Next states is sized : "<<next_states.size()<<std::endl;
                    for(auto it : next_states[i])
                    {
                        std::swap(states[cur], it.second);
                        /*if(!(counter%100))
                        {
                            std::cout<<"First weight is "<<it.first<<" with "<<std::endl;
                            states[a].dump(std::cout);
                            std::cout<<"=> "<<states[a].differential()<<std::endl;
                            std::cout<<states[a].path()<<std::endl;
                        }*/
                        cur++;
                    }
                }
            }
            //end = std::chrono::steady_clock::now();
            //diff = end - start;
            //std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms (3)"<<std::endl;
            states.resize(cur);

			if(states.size())
				cur_limit = limit_from_score(states[0].total_score());
			if(!(counter%100))
				std::cout<<"Current limit is "<<cur_limit<<std::endl;


            counter++;
        }

        auto end = std::chrono::steady_clock::now();
        auto diff = end - start;
        std::cout<<std::chrono::duration<double, std::milli>(diff).count()<<" ms"<<std::endl;

        State finished;
        final_state.finish(finished);
        finished.dump(std::cout);

        if(finished.total_score()>min_score)
            scored++;
        else if(std::chrono::duration<double, std::milli>(diff).count()<=4600)
            timed++;
        else
            failed++;

        if(finished.total_score()>min_score && std::chrono::duration<double, std::milli>(diff).count()<=4600)
        {
			update_answer(true, finished.online_path());

			std::cout<<finished.online_path()<<std::endl;
            int nb_allowed;
            char* allowed = finished.allowed(nb_allowed);
            std::cout<<"FOUND THE GRAAL ! (be sure no allowed more : "<<nb_allowed<<")"<<std::endl;
            min_score = finished.total_score();
			std::ofstream ofs("out.txt", std::ios::out|std::ios::trunc);
			ofs<<finished.online_path();
			return 0;
        }
        else
		{
			std::cout<<finished.online_path()<<std::endl;
            update_answer(false);
		}
        std::cout<<"And we have ratio scored timed failed : "<<scored<<" "<<timed<<" "<<failed<<std::endl;
    }

    for(int i=0; i<N_THREADS-1; i++)
        delete threads[i];

    //C_socket::end();

    std::cout<<"Ending with min score = "<<min_score<<std::endl;

    return 0;
}
