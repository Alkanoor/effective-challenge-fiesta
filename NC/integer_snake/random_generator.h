#ifndef RANDOM_GENERATOR_H
#define RANDOM_GENERATOR_H


#include <vector>


class Random_generator
{
    public:
        Random_generator(int seed1=0, int seed2=0, int seed3=0, int min_size=1000);

        int next_seed(int min, int max, int& seed);
        int next_num(int &seed1, int &seed2, int &seed3);

        void reset(int seed1, int seed2, int seed3);

        int get_value(int index);
		int get_score_3(int index);
		int get_score_2(int index);

        static Random_generator generator;

    private:
        std::vector<int> values_;
		std::vector<int> scores2_;
		std::vector<int> scores3_;
        int seed1_, seed2_, seed3_;
        int min_size_;
};


#endif
