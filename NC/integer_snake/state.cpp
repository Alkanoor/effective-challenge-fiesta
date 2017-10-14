#include "state.h"

#include <cmath>
#include <iostream>


State::State(int step, int total_score, int score_2, int score_3) :
    step_(step),
    total_score_(total_score),
	score2_(score_2),
	score3_(score_3)
{
    /*if(score2_<2||score3_<2)
    {
        for(int k=0; k<N; k++)
            for(int j=0; j<N; j++)
                target_[k][j] = 1;
    }
    else
    {
        int near2 = near_2(score2_);
        int near3 = near_3(score3_);
        int i=0, j=0, direction=1;
        for(; near2>1; near2/=2)
            if(score2_&near2)
            {
                target_[i][j] = near2;
                j += direction;
                if(j>=N||j<0)
                {
                    direction *= -1;
                    i++;
                    if(j>=N)
                        j = N-1;
                    else
                        j = 0;
                }
            }
        while(j>=0&&j<N)
        {
            target_[i][j] = -1;
            j += direction;
        }
        int target_i = i+1;
        i=N-1, j=N-1, direction=-1;
        int a=0;
        for(; near3>1; near3/=2)
            if((score3_/3)&(near3/3))
            {
                target_[i][j] = near3;
                j += direction;
                if(j>=N||j<0)
                {
                    direction *= -1;
                    i--;
                    if(j>=N)
                        j = N-1;
                    else
                        j = 0;
                }
                a++;
            }
        while(j>=0&&j<N&&a<9)
        {
            target_[i][j] = -1;
            j += direction;
            a++;
        }
        while(j>=0&&j<N)
        {
            target_[i][j] = -1;
            j += direction;
        }
        direction *= -1;
        i--;
        if(j>=N)
            j = N-1;
        else
            j = 0;
        while(a<9)
        {
            target_[i][j] = -1;
            j += direction;
            a++;
        }
        while(j>=0&&j<N)
        {
            target_[i][j] = -1;
            j += direction;
        }
        for(int k=target_i; k<i; k++)
            for(j=0; j<N; j++)
                target_[k][j] = 1;
        if(score2_>120)
        {
            std::cout<<"We obtained i2="<<i<<std::endl;

            std::cout<<"For score "<<score2_<<" ("<<near2<<") "<<score3_<<" ("<<near3<<")"<<std::endl;
            for(int i=0; i<N; i++)
            {
                for(int j=0; j<N; j++)
                    std::cout<<target_[i][j]<<" ";
                std::cout<<std::endl;
            }
        }
    }*/
}

void State::reset(const Mat<N, short>& state)
{state_ = state;}

void State::reset_string(const std::string& to_reach)
{path_ = to_reach;}

void State::append_to_path(char c)
{path_ += c;}

int State::score() const
{
    /*int s = 0;
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            s += state_[i][j];
    return s;*/
	return score2_+score3_;
}

int State::total_score() const
{return total_score_;}

float State::other_differential() const
{
    /*if(score2_>100)
    {
        std::cout<<"Other diffff "<<std::endl;
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
                std::cout<<state_[i][j]<<" ";
            std::cout<<std::endl;
        }
        std::cout<<std::endl;
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
                std::cout<<target_[i][j]<<" ";
            std::cout<<std::endl;
        }
    }*/
	float dif = 0;
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
            if(target_[i][j]>=0)
                if(state_[i][j]%3 == target_[i][j]%3)
                    dif += my_abs(Log_table::log_table[state_[i][j]]-Log_table::log_table[target_[i][j]]);
                else
                    dif += std::max(Log_table::log_table[state_[i][j]], Log_table::log_table[target_[i][j]]);

    /*if(score2_>100)
        std::cout<<"=> "<<dif<<std::endl;*/
    dif += 3*differential();
    return dif;
}

float State::differential() const
{
    float dif = 0;
	float tmp1, tmp2;
    for(int i=0; i<N-1; i++)
        for(int j=0; j<N; j++)
        {
            if((!(state_[i][j]%3)&&(state_[i+1][j]%3))||((state_[i][j]%3)&&!(state_[i+1][j]%3)))
                tmp1 = std::max(Log_table::log_table[state_[i][j]], Log_table::log_table[state_[i+1][j]]);
                /*if(my_abs(2-i)+my_abs(2-j)>my_abs(2-i-1)+my_abs(2-j))
                    dif += Log_table::log_table[state_[i][j]];
                else
                    dif += Log_table::log_table[state_[i+1][j]];*/
            else
                tmp1 = my_abs(Log_table::log_table[state_[i][j]]-Log_table::log_table[state_[i+1][j]]);

            if((!(state_[j][i]%3)&&(state_[j][i+1]%3))||((state_[j][i]%3)&&!(state_[j][i+1]%3)))
                tmp2 = std::max(Log_table::log_table[state_[j][i]], Log_table::log_table[state_[j][i+1]]);
                /*if(my_abs(2-i)+my_abs(2-j)>my_abs(2-i-1)+my_abs(2-j))
                    dif += Log_table::log_table[state_[j][i]];
                else
                    dif += Log_table::log_table[state_[j][i+1]];*/
            else
                tmp2 = my_abs(Log_table::log_table[state_[j][i]]-Log_table::log_table[state_[j][i+1]]);

			if(((!i&&!j)||(i==N-2&&j==N-1))&&(state_[0][0]>=128||state_[N-1][N-1]>=128))
				dif += std::min(tmp1, tmp2);
			else
				dif += tmp1+tmp2;
        }

    return dif;
}

const std::string& State::path() const
{return path_;}

std::string State::online_path() const
{
    std::string ret;
    for(int i=0; i<(int)path_.size(); i+=2)
    {
        ret += path_[i];
        ret += path_[i+1];
        if(i+2<(int)path_.size())
            ret += '|';
    }
    return ret;
}

const int State::step() const
{return step_;}

char* State::allowed(int& nb_possibilities)
{
    nb_possibilities = 0;
    for(int i=0; i<N; i++)
        for(int j=0; j+1<N; j++)
        {
            if(state_[i][j]==state_[i][j+1])
                allowed_[nb_possibilities++] = 2*(i+N*j);
            else if(state_[j][i]==state_[j+1][i])
                allowed_[nb_possibilities++] = 1+2*(i+N*j);
        }

    return allowed_;
}

void State::next_state(char mvt, State& next)
{
    next = State(step_+1, total_score_, Random_generator::generator.get_score_2(step_), Random_generator::generator.get_score_3(step_));
    //next = State(step_+1, total_score_, 0, 0);
    next.path_ = path_;
    next.reset(state_);
    Mat<N, short>& m = next.state_;
    bool direction = false;
    if(mvt%2)
        direction = true;

    mvt /= 2;
    if(!(mvt%2))
    {
        mvt /= 2;
        next.total_score_ += 2*m[mvt%N][mvt/N];
        if(direction)
        {
            m[mvt%N][mvt/N+1] = m[mvt%N][mvt/N]+m[mvt%N][mvt/N+1];
            m[mvt%N][mvt/N] = Random_generator::generator.get_value(step_);
            next.append_to_path(convert_index_to_movements(mvt%N, mvt/N));
            next.append_to_path(convert_index_to_movements(mvt%N, mvt/N+1));
        }
        else
        {
            m[mvt%N][mvt/N] = m[mvt%N][mvt/N]+m[mvt%N][mvt/N+1];
            m[mvt%N][mvt/N+1] = Random_generator::generator.get_value(step_);
            next.append_to_path(convert_index_to_movements(mvt%N, mvt/N+1));
            next.append_to_path(convert_index_to_movements(mvt%N, mvt/N));
        }
    }
    else
    {
        mvt /= 2;
        next.total_score_ += 2*m[mvt/N][mvt%N];
        if(direction)
        {
            m[mvt/N+1][mvt%N] = m[mvt/N][mvt%N]+m[mvt/N+1][mvt%N];
            m[mvt/N][mvt%N] = Random_generator::generator.get_value(step_);
            next.append_to_path(convert_index_to_movements(mvt/N, mvt%N));
            next.append_to_path(convert_index_to_movements(mvt/N+1, mvt%N));
        }
        else
        {
            m[mvt/N][mvt%N] = m[mvt/N][mvt%N]+m[mvt/N+1][mvt%N];
            m[mvt/N+1][mvt%N] = Random_generator::generator.get_value(step_);
            next.append_to_path(convert_index_to_movements(mvt/N+1, mvt%N));
            next.append_to_path(convert_index_to_movements(mvt/N, mvt%N));
        }
    }
}

void State::finish(State& res)
{
    res = *this;
    int n = 0;
    State next;
    char* poss = res.allowed(n);
    while(n)
    {
        res.next_state(poss[0], next);
        res = next;
        poss = res.allowed(n);
    }
}

std::ostream& State::dump(std::ostream& os)
{
    os<<"State at step "<<step_<<" with score "<<score()<<" ("<<total_score_<<")  :"<<std::endl;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
            os<<state_[i][j]<<" ";
        os<<std::endl;
    }
    return os;
}

char State::convert_index_to_movements(int i, int j)
{
    return 'A'+i*5+j;
}

int State::near_2(int a)
{
	int b = 1;
	while(b*2<a)
		b *= 2;
	return b;
}

int State::near_3(int a)
{
	int b = 3;
	while(b*2<a)
		b *= 2;
	return b;
}
