#ifndef STATE_H
#define STATE_H


#include "random_generator.h"
#include "log_table.h"

#include <ostream>
#include <array>

#define N 5


template <size_t M, typename T>
using Vec = std::array<T, M>;
template <size_t M, typename T>
using Mat = std::array<Vec<M, T>, M>;

class State
{
    public:
        State(int step=-1, int total_score=0, int score_2=0, int score_3=0);

        void reset(const Mat<N, short>& state);
        void reset_string(const std::string& to_reach);
        void append_to_path(char c);

        int score() const;
        int total_score() const;
        float differential() const;
		float other_differential() const;
        char* allowed(int& nb_possibilities);
        void next_state(char mvt, State& next);
        void finish(State& res);

        const std::string& path() const;
        std::string online_path() const;
        const int step() const;

        std::ostream& dump(std::ostream& os);

        template <typename T>
        static inline T my_abs(T a);
		
		static int near_2(int a);
		static int near_3(int a);

    private:
        int step_;
        int total_score_;
		int score2_;
		int score3_;
        Mat<N, short> state_;
		Mat<N, short> target_;
        char allowed_[2*N*(N-1)];
        std::string path_;

        static char convert_index_to_movements(int i, int j);
};


template <typename T>
T State::my_abs(T a)
{
    return (a>=0)? a: -a;
}


#endif
