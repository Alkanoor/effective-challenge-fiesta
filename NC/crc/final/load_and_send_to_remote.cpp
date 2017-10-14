#include "include/load_and_send_to_remote.hpp"

#include <sys/wait.h>
#include <unistd.h>
#include <iostream>
#include <fstream>


Load_And_Send_To_Remote::Load_And_Send_To_Remote(const std::string& program_path, const std::string& filename, const std::string& tmp_file) :
    _solution_filename(tmp_file)
{
    reload(program_path, filename);
}

bool Load_And_Send_To_Remote::reload(const std::string& program_path, const std::string& filename)
{
    if(program_path.size())
        _program_path = program_path;
    if(filename.size())
        _filename = filename;

    int pid = fork();
    if(pid<0)
    {
        std::cerr<<"[-] Error during fork"<<std::endl;
        return false;
    }
    else if(!pid)
    {
        char* args[] = {(char*)_program_path.c_str(), (char*)"load", (char*)_filename.c_str(), (char*)"PHPSESSID=8bd6a6df13dcc4e612b5a79499a7b93a; SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1666111888%3Bi%3A3%3Bi%3A0%3B%7D", NULL};
        if(execv(_program_path.c_str(), args) < 0)
        {
            std::cerr<<"[-] Error during execv of "<<_program_path<<std::endl;
            return false;
        }
    }
    else
        wait(nullptr);

    _load_file.reload(_filename);

    return true;
}

const std::vector<int>& Load_And_Send_To_Remote::get_data() const
{
    return _load_file.get_data();
}

void Load_And_Send_To_Remote::send_result(const std::string& result)
{
    std::ofstream ofs(_solution_filename.c_str(), std::ios::trunc|std::ios::out);
    ofs<<result;
    ofs.close();

    int pid = fork();
    if(pid<0)
    {
        std::cerr<<"[-] Error during fork"<<std::endl;
        exit(1);
    }
    else if(!pid)
    {
        char* args[] = {(char*)_program_path.c_str(), (char*)"send", (char*)_solution_filename.c_str(), (char*)"PHPSESSID=8bd6a6df13dcc4e612b5a79499a7b93a; SMFCookie89=a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2263127%22%3Bi%3A1%3Bs%3A40%3A%228f76ee4e57b4cb44bc9082e26c5dd7be554dbd81%22%3Bi%3A2%3Bi%3A1666111888%3Bi%3A3%3Bi%3A0%3B%7D", NULL};
        if(execv(_program_path.c_str(), args) < 0)
        {
            std::cerr<<"[-] Error during execv of "<<_program_path<<std::endl;
            exit(1);
        }
    }
    else
        wait(nullptr);
}
