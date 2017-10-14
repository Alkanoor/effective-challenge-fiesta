#include "enigma.hpp"

#include <fstream>
#include <sstream>

//g++ main.cpp enigma.cpp util.cpp  -std=c++11 -o enigma

//py_cipher, indice de coincidence sur rotors+ringstellung, puis IC sur la position initiale, puis script python pour permutations

std::string read(const std::string& path)
{
    std::ifstream ifs(path.c_str(), std::ios::in|std::ios::binary);
    ifs.seekg(0, ifs.end);
    unsigned int s = ifs.tellg();
    ifs.seekg(0, ifs.beg);

    std::vector<unsigned char> v(s);
    ifs.read((char*)&(v[0]), s);

    ifs.close();

    return std::string(v.begin(), v.end());
}

void BF_ringstellung(const std::array<unsigned char, 3>& initial, const std::array<int, 3>& rotor);

std::string hash(char a, char b, char c, int index)
{
    std::ostringstream oss;
    oss<<a<<b<<c<<index;
    return oss.str();
}

void unhash(const std::string& h, char& a, char& b, char& c, int& index)
{
    std::istringstream iss(h);
    iss>>a>>b>>c>>index;
}

Enigma enigma;
std::string tmp;

int main()
{
    std::string data = clean(read("cipher"));
    std::cout<<data<<std::endl;
    std::cout<<IC(data)<<std::endl;

    std::vector<std::array<int,3> > rotors = {{3,4,5},{3,4,6},{3,4,7},{3,5,6},{3,5,7},{3,6,7},
                                              {4,3,5},{4,3,6},{4,3,7},{4,5,6},{4,5,7},{4,6,7},
                                              {5,4,3},{5,4,6},{5,4,7},{5,3,6},{5,3,7},{5,6,7},
                                              {6,4,5},{6,4,3},{6,4,7},{6,5,3},{6,5,7},{6,3,7},
                                              {7,4,5},{7,4,6},{7,4,3},{7,5,6},{7,5,3},{7,6,3}};
    auto t = rotors.size();
    for(int i=0; i<t; i++)
        rotors.push_back({rotors[i][0], rotors[i][2], rotors[i][1]});

    t = rotors.size();
    for(int i=0; i<t; i++)
        rotors[i] = {rotors[i][0]-3, rotors[i][1]-3, rotors[i][2]-3};

    //NWL + BUJ => truc presque correct
    std::array<unsigned char, 3> initial{'M','W','Q'};
    std::array<unsigned char, 3> ringstellung{'A','U','O'};
    int id_chosen = 45;

    enigma.set_cipher(data);

    //BF_ringstellung(initial, rotors[id_chosen]);

    std::map<unsigned char, unsigned char> corresp;

    corresp['B'] = 'K';
    corresp['K'] = 'B';
    corresp['D'] = 'E';
    corresp['E'] = 'D';
    corresp['M'] = 'U';
    corresp['U'] = 'M';
    /*corresp['K'] = 'O';
    corresp['O'] = 'K';*/
    corresp['J'] = 'X';
    corresp['X'] = 'J';
    corresp['V'] = 'L';
    corresp['L'] = 'V';
    /*corresp['X'] = 'T';
    corresp['T'] = 'X';*/

    enigma.reset(initial, rotors[id_chosen], ringstellung, corresp);
    std::cout<<corresp['B']<<" => "<<enigma.cipher_decipher()<<std::endl;

    return 0;

    corresp['E'] = 'D';
    corresp['D'] = 'E';

    // for(int i=0;i<26;i++)
    // {
    //     corresp['B'] = 'A' + i;
    //     enigma.reset(initial, rotors[id_chosen], ringstellung, corresp);
    //
    //     std::cout<<corresp['B']<<" => "<<enigma.cipher_decipher().substr(0,20)<<std::endl;
    // }

    corresp['B'] = 'K';
    corresp['K'] = 'B';

    enigma.reset(initial, rotors[id_chosen], ringstellung, corresp);
    std::cout<<corresp['B']<<" => "<<enigma.cipher_decipher()<<std::endl;
    return 0;

    /*corresp['H'] = 'L';
    corresp['L'] = 'H';

    enigma.reset(initial, rotors[id_chosen], ringstellung, corresp);
    std::cout<<corresp['H']<<" => "<<enigma.cipher_decipher()<<std::endl;*/

    corresp['N'] = 'F';
    corresp['F'] = 'N';

    enigma.reset(initial, rotors[id_chosen], ringstellung, corresp);
    std::cout<<corresp['N']<<" => "<<enigma.cipher_decipher()<<std::endl;

    for(int i=0;i<26;i++)
    {
        corresp['N'] = 'A' + i;
        enigma.reset(initial, rotors[id_chosen], ringstellung, corresp);

        std::cout<<corresp['N']<<" => "<<enigma.cipher_decipher().substr(0,20)<<std::endl;
    }
    return 0;

    std::map<float, std::string> scores;
    std::map<float, int> scores2;
    std::map<int, float> total_scores;

    // int N = 100;
    // srand(time(NULL));
    // for(int i=0;i<N;i++)
    // {
    //     scores.clear();
    //     for(int j=0;j<3;j++)
    //     {
    //         initial[j] = rand()%26+'A';
    //         ringstellung[j] = rand()%26+'A';
    //     }
    //     for(int j=0;j<rotors.size();j++)
    //     {
    //         enigma.reset(initial, rotors[j], ringstellung);
    //         tmp = enigma.cipher_decipher();
    //         float score = IC(tmp);
    //         scores2[score] = j;
    //         if(!i)
    //             total_scores[j] = score;
    //         else
    //             total_scores[j] += score;
    //     }
    //     std::cout<<"============"<<std::endl;
    //     print_map_sorted(std::cout, scores2, 20, false);
    // }
    // std::cout<<"============"<<std::endl;
    // print_map_sorted(std::cout, reverse_map_info_loss(total_scores), 20, false);
    // std::cout<<"poooooooooooop"<<std::endl;
    // print_map_sorted(std::cout, reverse_map_info_loss(total_scores));
    // std::cout<<"mmmmmmmmmmmmm"<<std::endl;
    // std::cout<<reverse_map_info_loss(total_scores);
    // return 0;

    std::ifstream hashes("out_combinations", std::ios::in|std::ios::binary);
    std::vector<std::string> hashh;
    while(hashes>>tmp)
        hashh.push_back(tmp);


    int size_max = 500;
    int cur = 0;
    float min = -1;

    for(auto s : hashh)
    {
        char c1, c2, c3;
        int id;
        std::cout<<"S : "<<s<<std::endl;
        unhash(s,c1,c2,c3,id);
        std::cout<<"Giving : "<<c1<<" "<<c2<<" "<<c3<<" "<<id<<std::endl;
        //enigma.reset(initial, rotors[id], {c1,c2,c3});
        for(int l='A'; l<='Z'; l++)
        {
            std::cout<<"Cur letter : "<<l<<std::endl;
            auto st = time(NULL);
            for(int m='A'; m<='Z'; m++)
                for(int n='A'; n<='Z'; n++)
                {
                    initial[0] = l;
                    initial[1] = m;
                    initial[2] = n;
                    /*if(enigma.is_config_ok(initial, 5))
                    {
                        std::cout<<"FOUND genial !!! "<<std::endl;
                        std::cout<<initial<<std::endl;
                        return 0;
                    }*/
                    enigma.reset(initial, rotors[id], {c1,c2,c3});
                    tmp = enigma.cipher_decipher();
                    float score = IC(tmp);

                    if(cur<size_max)
                    {
                        scores[-score] = hash(l,m,n,id);
                        if(score<min||min<0)
                            min = score;
                    }
                    else if(score>min)
                    {
                        float prev = min;
                        min = -1;
                        scores[-score] = hash(l,m,n,cur);
                        for(auto it : scores)
                            if((it.first<min||min<0)&&it.first>=prev)
                                min = it.first;
                    }
                }
            std::cout<<"Time taken (secs) : "<<time(NULL)-st<<std::endl;
            print_map_no_sort(std::cout, scores, 20, true);
        }
        std::cout<<"FINALLLL"<<std::endl;
        print_map_no_sort(std::cout, scores, 200, true);
    }

    //Donne NWL comme position initiale

    for(int j=0;j<3;j++)
        initial[j] = rand()%26+'A';

    for(int l='A'; l<='Z'; l++)
    {
        std::cout<<"Cur letter : "<<l<<std::endl;
        auto st = time(NULL);
        for(int m='A'; m<='Z'; m++)
        {
            for(int n='A'; n<='Z'; n++)
            {
                ringstellung[0] = l;
                ringstellung[1] = m;
                ringstellung[2] = n;
                cur = 0;
                for(auto r : rotors)
                {
                    enigma.reset(initial, r, ringstellung);
                    tmp = enigma.cipher_decipher();
                    float score = IC(tmp);

                    if(cur<size_max)
                    {
                        scores[-score] = hash(l,m,n,cur);
                        if(score<min||min<0)
                            min = score;
                    }
                    else if(score>min)
                    {
                        float prev = min;
                        min = -1;
                        scores[-score] = hash(l,m,n,cur);
                        for(auto it : scores)
                            if((it.first<min||min<0)&&it.first>=prev)
                                min = it.first;
                    }

                    cur++;
                    if(score>0.05)
                    {
                        std::cout<<"PAS MAL : "<<score<<std::endl;
                        std::cout<<initial;
                        std::cout<<ringstellung;
                        std::cout<<r;
                        std::cout<<tmp<<std::endl;
                        if(score>0.06)
                        {
                            std::cout<<"FOUND !"<<std::endl;
                            return 0;
                        }
                    }
                }
            }
        }
        std::cout<<"Time taken (secs) : "<<time(NULL)-st<<std::endl;
        print_map_no_sort(std::cout, scores, 20, true);
    }
    std::cout<<"FINALLLL"<<std::endl;
    print_map_no_sort(std::cout, scores, 200, true);
}

void BF_ringstellung(const std::array<unsigned char, 3>& initial, const std::array<int, 3>& rotor)
{
    int size_max = 500;
    int cur = 0;
    float min = -1;

    std::array<unsigned char, 3> ringstellung;

    std::map<float, std::string> scores;

    for(int l='A'; l<='Z'; l++)
    {
        std::cout<<"Cur letter : "<<l<<std::endl;
        auto st = time(NULL);
        for(int m='A'; m<='Z'; m++)
            for(int n='A'; n<='Z'; n++)
            {
                ringstellung[0] = l;
                ringstellung[1] = m;
                ringstellung[2] = n;

                enigma.reset(initial, rotor, ringstellung);
                tmp = enigma.cipher_decipher();
                float score = IC(tmp);

                if(cur<size_max)
                {
                    scores[-score] = hash(l,m,n,1);
                    if(score<min||min<0)
                        min = score;
                }
                else if(score>min)
                {
                    float prev = min;
                    min = -1;
                    scores[-score] = hash(l,m,n,1);
                    for(auto it : scores)
                        if((it.first<min||min<0)&&it.first>=prev)
                            min = it.first;
                }
            }
        std::cout<<"Time taken (secs) : "<<time(NULL)-st<<std::endl;
        print_map_no_sort(std::cout, scores, 20, true);
    }
    std::cout<<"FINALLLL"<<std::endl;
    print_map_no_sort(std::cout, scores, 200, true);
}
