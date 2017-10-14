#include "include/load_from_file.hpp"

#include <fstream>


Load_From_File::Load_From_File(const std::string& filename)
{
    reload(filename);
}

bool Load_From_File::reload(const std::string& filename)
{
    if(filename != "")
        _filename = filename;

    std::ifstream ifs(_filename);
    if(!ifs)
        return false;

    int tmp;
    while(ifs>>tmp)
        _read.push_back(tmp);

    return true;
}

const std::vector<int>& Load_From_File::get_data() const
{
    return _read;
}
