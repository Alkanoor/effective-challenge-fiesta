#ifndef LOAD_AND_SEND_TO_REMOTE
#define LOAD_AND_SEND_TO_REMOTE


#include "load_from_file.hpp"


class Load_And_Send_To_Remote
{
    public:
        Load_And_Send_To_Remote(const std::string& program_path, const std::string& filename="data/input_c", const std::string& _tmp_file="data/solution");

        bool reload(const std::string& program_path, const std::string& filename="data/input_c");

        const std::vector<int>& get_data() const;

        void send_result(const std::string& result);

    private:
        std::string _program_path;
        std::string _filename;
        std::string _solution_filename;

        Load_From_File _load_file;
};


#endif
