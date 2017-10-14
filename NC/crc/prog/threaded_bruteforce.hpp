#ifndef THREADED_BRUTEFORCE_HPP
#define THREADED_BRUTEFORCE_HPP


#include <thread>
#include <mutex>


class Threaded_bruteforce
{
    public:
        Threaded_bruteforce();

        void run();

        char itere(int x, int y, UINT64 cur_crc, int depth = 0);

        static int w, h;
        static std::vector<std::vector<char> > T;
        static std::chrono::system_clock::time_point begin;

    private:
        static std::set<UINT64> up;
        static std::set<UINT64> down;
        static bool up_accessed;
        static bool down_accessed;
        static std::mutex mutex_on_up;
        static std::mutex mutex_on_down;

        static int total_up;
        static int total_down;

        std::vector<int> chosen_path;

        int thread_id;
        std::thread *thread;
        static int counter_id;

        bool up_or_down;
        bool has_admin_right_on_set;
        int granted_size_temp_buf;
        std::vector<UINT64> temp_buf;
};


#endif
