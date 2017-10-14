#ifndef LOAD_FROM_FILE_HPP
#define LOAD_FROM_FILE_HPP


#include <string>
#include <vector>


class Load_From_File
{
    public:
        Load_From_File(const std::string& filename="");

        bool reload(const std::string& filename="");

        const std::vector<int>& get_data() const;

    private:
        std::string _filename;
        std::vector<int> _read;
};


#endif
