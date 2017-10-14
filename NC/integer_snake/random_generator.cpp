#include "random_generator.h"


Random_generator Random_generator::generator;

Random_generator::Random_generator(int seed1, int seed2, int seed3, int min_size) :
    seed1_(seed1),
    seed2_(seed2),
    seed3_(seed3),
    min_size_(min_size)
{}

int Random_generator::next_seed(int min, int max, int& seed)
{
	seed = (seed*125)%2796203;
	return seed%(max-min+1)+min;
}

int Random_generator::next_num(int &seed1, int &seed2, int &seed3)
{
	int which=next_seed(0,1,seed1);
	if(which%2==0)
		return next_seed(1,3,seed2);
	else
		return next_seed(1,3,seed3);
}

void Random_generator::reset(int seed1, int seed2, int seed3)
{
    seed1_ = seed1;
    seed2_ = seed2;
    seed3_ = seed3;
}

int Random_generator::get_value(int index)
{
	int cur_size = (int)values_.size();
    while(index>=cur_size)
        for(int i=0; i<min_size_; i++)
		{
			int a = next_num(seed1_, seed2_, seed3_);
            values_.push_back(a);
			if(a%3)
			{
				if(cur_size)
				{
					scores2_.push_back(scores2_[cur_size-1]+a);
					scores3_.push_back(scores3_[cur_size-1]);
				}
				else
				{
					scores2_.push_back(a);
					scores3_.push_back(0);
				}
			}
			else
			{
				if(cur_size)
				{
					scores2_.push_back(scores2_[cur_size-1]);
					scores3_.push_back(scores3_[cur_size-1]+a);
				}
				else
				{
					scores2_.push_back(0);
					scores3_.push_back(a);
				}
			}
			cur_size++;
		}
    return values_[index];
}

int Random_generator::get_score_3(int index)
{
    if(index>=(int)scores3_.size())
		get_value(index);
    return scores3_[index];
}

int Random_generator::get_score_2(int index)
{
	if(index>=(int)scores2_.size())
		get_value(index);
    return scores2_[index];
}
