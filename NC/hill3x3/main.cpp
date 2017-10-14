#include <iostream>
#include <cassert>
#include <fstream>
#include <cmath>
#include <set>

#include "Ostream_writable.h"
#include "Constants.h"


std::vector<std::string> get_trios(const Matrix& m)
{
    assert(m.size() == 3);

    std::vector<std::string> ret(m[0].size());
    for(unsigned int j=0; j<m[0].size(); j++)
    {
        std::string trio = "AAA";
        for(unsigned int i=0; i<3; i++)
            trio[i] = int_to_chr_map[m[i][j]];
        ret[j] = trio;
    }

    return ret;
}

std::map<std::string, int> compute_trios(const std::vector<std::string>& trios)
{
    std::map<std::string, int> ret;
    std::map<std::string, int> tmp;
    for(unsigned int j=0; j<trios.size(); j++)
    {
        std::string trio = trios[j];
        if(tmp.count(trio))
        {
            tmp[trio]++;
            ret[trio] = 1;
        }
        else
            tmp[trio] = 1;
    }

    for(auto it : ret)
        ret[it.first] = tmp[it.first];

    return ret;
}

std::tuple<float, int, int, int, std::vector<int>, std::vector<int>, std::vector<int> > evaluate(const Matrix& m, const std::map<char, float>& detail)
{
    auto trios = get_trios(m);
    float score = 0;
    int good = 0;
    int very_good = 0;
    int very_very_good = 0;
    std::vector<int> good_index;
    std::vector<int> very_good_index;
    std::vector<int> very_very_good_index;
    int counter = 0;
    for(auto i : trios)
    {
        if(i[0] == i[1] && i[0] == i[2])
        {
            std::cout<<"One very very good obtained ! "<<i<<std::endl;
            very_very_good++;
            score += 2*detail.at(i[0]);
            good_index.push_back(counter);
            very_good_index.push_back(counter);
            very_very_good_index.push_back(counter);
        }
        else if(i[0] == i[1])
        {
            score += detail.at(i[0]);
            good++;
            if(detail.at(i[0]) >= 0.05)
            {
                very_good_index.push_back(counter);
                very_good++;
            }
            good_index.push_back(counter);
        }
        else if(i[1] == i[2])
        {
            score += detail.at(i[1]);
            good++;
            if(detail.at(i[1]) >= 0.05)
            {
                very_good_index.push_back(counter);
                very_good++;
            }
            good_index.push_back(counter);
        }
        else if(i[0] == i[2])
        {
            score += detail.at(i[0]);
            good++;
            if(detail.at(i[0]) >= 0.05)
            {
                very_good_index.push_back(counter);
                very_good++;
            }
            good_index.push_back(counter);
        }
        counter++;
    }

    return std::make_tuple(score, good, very_good, very_very_good, good_index, very_good_index, very_very_good_index);
}

std::string get_line(const Matrix& m, int line, const std::map<int, char>& corresp)
{
    std::string ret;
    for(unsigned int j=0; j<m.at(line).size(); j++)
        ret += corresp.at(m.at(line).at(j));
    return ret;
}

std::vector<std::string> extract_interesting(const std::vector<std::string>& trios, const std::vector<int>& index)
{
    std::vector<std::string> ret;
    for(auto i : index)
        ret.push_back(trios[i]);
    return ret;
}

float entropy(const std::string& m)
{
    auto counter = Utils::count(m);
    float ret = 0;
    float sum = 0;
    for(auto it : counter)
        sum += it.second;
    for(auto it : counter)
        ret -= (float)it.second/sum*log((float)it.second/sum);
    return ret;
}

int main()
{
    known_text = Utils::clean(known_text);
    target_text_ciphered = Utils::clean(target_text_ciphered);

    /** lignes de toute puissance **/
    /**
    std::vector<int> a = {1,2,4,5};
    std::cout<<a<<std::endl<<std::endl;

    std::vector<std::vector<int> > b = {a,a,a};
    std::cout<<b<<std::endl<<std::endl;

    std::vector<std::vector<std::vector<int> > > c = {b, b};
    std::cout<<c<<std::endl<<std::endl;

    std::cout<<known_text<<std::endl;
    std::cout<<Utils::IC(known_text)<<std::endl;
    std::cout<<Utils::IC(target_text_ciphered)<<std::endl;

    auto counter = Utils::count(target_text_ciphered);
    std::cout<<counter<<std::endl;

    std::cout<<Utils::inverse_map_accumulate(counter)<<std::endl;
    std::cout<<Utils::inverse_map_accumulate(Utils::count(known_text))<<std::endl;
    **/

    /*for(int i=0; i<10; i++)
        for(int j=0; j<10; j++)
            for(int k=0; k<10; k++)
                for(int l=0; l<10; l++)
                    for(int m=0; m<10; m++)
                        for(int n=0; n<10; n++)
    {
        Vec v1{6,i,j}, v2{k,6,l}, v3{m,n,6};
        Matrix m{v1, v2, v3};
        if(Utils::det(m) == 1)
            std::cout<<m<<std::endl;
    }*/

    Matrix chosen = {{6, 9, 2}, {4, 6, 1}, {5, 8, 6}};
    Matrix inverted_chosen = Utils::inverse(chosen);
    std::cout<<"Inverted :"<<std::endl<<inverted_chosen<<std::endl;
    std::cout<<"Verification : "<<std::endl<<Utils::rescaleMod36(Utils::prod(chosen, inverted_chosen))<<std::endl;

    std::string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    charset = "9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA";
    chr_to_int_map = Utils::map_from_charset(charset);
    int_to_chr_map = Utils::inverse_map(chr_to_int_map);

    auto step1 = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, false);
    std::cout<<"Step1"<<std::endl<<step1<<std::endl;
    auto step2 = Utils::rescaleMod36(Utils::prod(chosen, step1));
    std::cout<<"Step2"<<std::endl<<step2<<std::endl;
    auto step3 = Utils::convert_mat_to_string(step2, int_to_chr_map, true);
    std::cout<<"Step3"<<std::endl<<step3<<std::endl;
    known_text_ciphered = step3;

    step1 = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, true);
    step2 = Utils::rescaleMod36(Utils::prod(chosen, step1));
    step3 = Utils::convert_mat_to_string(step2, int_to_chr_map, true);
    known_text_ciphered2 = step3;

    auto step4 = Utils::convert_string_to_mat(step3, chr_to_int_map, 3, step3.size()/3, true);
    auto step5 = Utils::rescaleMod36(Utils::prod(inverted_chosen, step4));
    auto step6 = Utils::convert_mat_to_string(step5, int_to_chr_map, true);

    std::cout<<"Step6"<<std::endl<<step6<<std::endl;


    auto tmp = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, true);
    auto trios1 = get_trios(tmp);
    auto trios1_counter = compute_trios(trios1);
    tmp = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, false);
    auto trios2 = get_trios(tmp);
    auto trios2_counter = compute_trios(trios2);

    std::cout<<"Trios on known text vertical : (size : "<<trios1_counter.size()<<")"<<std::endl;
    std::cout<<trios1_counter<<std::endl;

    std::cout<<"Trios on known text horizontal : (size : "<<trios2_counter.size()<<")"<<std::endl;
    std::cout<<trios2_counter<<std::endl;


    tmp = Utils::convert_string_to_mat(known_text_ciphered, chr_to_int_map, 3, known_text.size()/3, true);
    trios1 = get_trios(tmp);
    trios1_counter = compute_trios(trios1);
    tmp = Utils::convert_string_to_mat(known_text_ciphered, chr_to_int_map, 3, known_text.size()/3, false);
    trios2 = get_trios(tmp);
    trios2_counter = compute_trios(trios2);

    std::cout<<"Trios on known text ciphered horizontal vertical : (size : "<<trios1_counter.size()<<")"<<std::endl;
    std::cout<<trios1_counter<<std::endl;

    std::cout<<"Trios on known text ciphered horizontal horizontal : (size : "<<trios2_counter.size()<<")"<<std::endl;
    std::cout<<trios2_counter<<std::endl;


    tmp = Utils::convert_string_to_mat(known_text_ciphered2, chr_to_int_map, 3, known_text.size()/3, true);
    trios1 = get_trios(tmp);
    trios1_counter = compute_trios(trios1);
    tmp = Utils::convert_string_to_mat(known_text_ciphered2, chr_to_int_map, 3, known_text.size()/3, false);
    trios2 = get_trios(tmp);
    trios2_counter = compute_trios(trios2);

    std::cout<<"Trios on known text ciphered vertical vertical : (size : "<<trios1_counter.size()<<")"<<std::endl;
    std::cout<<trios1_counter<<std::endl;

    std::string trios_counter_string;
    for(auto it : trios1_counter)
        trios_counter_string += it.first;
    auto trios_counter = Utils::count(trios_counter_string);

    std::cout<<"Trios on known text ciphered vertical horizontal : (size : "<<trios2_counter.size()<<")"<<std::endl;
    std::cout<<trios2_counter<<std::endl;


    /*tmp = Utils::convert_string_to_mat(target_text_ciphered, chr_to_int_map, 3, known_text.size()/3, true);
    trios1 = get_trios(tmp);
    trios1_counter = compute_trios(trios1);
    tmp = Utils::convert_string_to_mat(target_text_ciphered, chr_to_int_map, 3, known_text.size()/3, false);
    trios2 = get_trios(tmp);
    trios2_counter = compute_trios(trios2);

    std::cout<<"Trios on known target text ciphered vertical : (size : "<<trios1_counter.size()<<")"<<std::endl;
    std::cout<<trios1_counter<<std::endl;

    std::string trios_counter_string;
    for(auto it : trios1_counter)
        trios_counter_string += it.first;
    auto trios_counter = Utils::count(trios_counter_string);

    std::cout<<"Trios on known target text ciphered horizontal : (size : "<<trios2_counter.size()<<")"<<std::endl;
    std::cout<<trios2_counter<<std::endl;*/


    //std::cout<<"Trios counter size : "<<trios_counter.size()<<std::endl;
    //std::cout<<trios_counter<<std::endl;


    std::map<char, float> detail;
    for(int i=0; i<26; i++)
        detail['A'+i] = 0.001;
    for(int i=0; i<10; i++)
        detail['0'+i] = 0.001;
    detail['E'] = 0.12;
    detail['S'] = 0.07;
    detail['A'] = 0.07;
    detail['I'] = 0.07;
    detail['N'] = 0.065;
    detail['T'] = 0.06;
    detail['R'] = 0.06;

    std::string chosen_text, chosen_text2;
    Matrix chosen_matrix;

    std::ofstream matrixes("matrices.txt", std::ios::out|std::ios::trunc);

    std::vector<Matrix> correct_matrix;
    std::map<float, std::tuple<Matrix, int, int, int> > sorted;
    for(int i=0; i<10; i++)
        for(int j=0; j<10; j++)
            for(int k=0; k<10; k++)
                for(int l=0; l<10; l++)
                    for(int m=0; m<10; m++)
                        for(int n=0; n<10; n++)
    {
        Vec v1{6,i,j}, v2{k,6,l}, v3{m,n,6};
        Matrix m{v1, v2, v3};
        if(Utils::det(m) == 1)
        {
            matrixes<<m<<std::endl;
            step1 = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, true);
            step2 = Utils::rescaleMod36(Utils::prod(m, step1));
            step3 = Utils::convert_mat_to_string(step2, int_to_chr_map, true);
            known_text_ciphered = step3;
            tmp = Utils::convert_string_to_mat(known_text_ciphered, chr_to_int_map, 3, known_text.size()/3, true);
            std::tuple<float, int, int, int, std::vector<int>, std::vector<int>, std::vector<int> > evaluated = evaluate(tmp, detail);
            sorted[-std::get<0>(evaluated)] = std::make_tuple(m, std::get<1>(evaluated), std::get<2>(evaluated), std::get<3>(evaluated));
            if(std::get<0>(evaluated)>=1 && std::get<0>(evaluated)<=1.1)
            {
                chosen_text = known_text_ciphered;
                chosen_matrix = m;
                step1 = Utils::convert_string_to_mat(known_text2, chr_to_int_map, 3, known_text2.size()/3, true);
                step2 = Utils::rescaleMod36(Utils::prod(m, step1));
                chosen_text2 = Utils::convert_mat_to_string(step2, int_to_chr_map, true);
            }
            correct_matrix.push_back(Utils::inverse(m));
        }
    }

    std::cout<<sorted<<std::endl;

    std::cout<<"Evaluation of ciphered text"<<std::endl;
    tmp = Utils::convert_string_to_mat(target_text_ciphered, chr_to_int_map, 3, known_text.size()/3, true);
    std::tuple<float, int, int, int, std::vector<int>, std::vector<int>, std::vector<int> > evaluated = evaluate(tmp, detail);
    std::tuple<std::vector<std::string>, std::vector<std::string>, std::vector<std::string> > selected_trios = std::make_tuple(
                                            extract_interesting(get_trios(tmp), std::get<4>(evaluated)),
                                            extract_interesting(get_trios(tmp), std::get<5>(evaluated)),
                                            extract_interesting(get_trios(tmp), std::get<6>(evaluated)));
    std::cout<<evaluated<<std::endl;
    std::cout<<selected_trios<<std::endl;


    std::cout<<"Evaluation of similar text"<<std::endl;
    auto clear_text = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, true);
    auto clear_text_trios = get_trios(clear_text);

    tmp = Utils::convert_string_to_mat(chosen_text, chr_to_int_map, 3, known_text.size()/3, true);
    evaluated = evaluate(tmp, detail);
    auto selected_trios_ciphered = std::make_tuple(extract_interesting(get_trios(tmp), std::get<4>(evaluated)),
                                                   extract_interesting(get_trios(tmp), std::get<5>(evaluated)),
                                                   extract_interesting(get_trios(tmp), std::get<6>(evaluated)));
    auto selected_trios_clear = std::make_tuple(extract_interesting(clear_text_trios, std::get<4>(evaluated)),
                                                extract_interesting(clear_text_trios, std::get<5>(evaluated)),
                                                extract_interesting(clear_text_trios, std::get<6>(evaluated)));

    std::cout<<evaluated<<std::endl;
    std::cout<<selected_trios_ciphered<<std::endl;

    clear_text = Utils::convert_string_to_mat(known_text2, chr_to_int_map, 3, known_text2.size()/3, true);
    clear_text_trios = get_trios(clear_text);

    tmp = Utils::convert_string_to_mat(chosen_text2, chr_to_int_map, 3, known_text2.size()/3, true);
    evaluated = evaluate(tmp, detail);
    auto selected_trios_ciphered2 = std::make_tuple(extract_interesting(get_trios(tmp), std::get<4>(evaluated)),
                                                   extract_interesting(get_trios(tmp), std::get<5>(evaluated)),
                                                   extract_interesting(get_trios(tmp), std::get<6>(evaluated)));

    std::cout<<evaluated<<std::endl;
    std::cout<<selected_trios_ciphered2<<std::endl;

    std::cout<<chosen_matrix<<std::endl;
    std::cout<<Utils::inverse(chosen_matrix)<<std::endl;

    std::cout<<Utils::convert_mat_to_string(Utils::rescaleMod36(Utils::prod(Utils::inverse(chosen_matrix), Utils::convert_string_to_mat("RRX", chr_to_int_map, 3, 1, true))), int_to_chr_map, true)<<std::endl;

    /*Matrix mats[8];
    mats[0] = Matrix{{6, 0, 1},
                    {1, 6, 4},
                    {9, 7, 6}};
    mats[1] = Matrix{{6, 1, 4},
                    {0, 6, 1},
                    {7, 9, 6}};
    mats[2] = Matrix{{6, 1, 4},
                    {9, 6, 1},
                    {7, 0, 6}};
    mats[3] = Matrix{{6, 9, 7},
                    {5, 6, 4},
                    {0, 5, 6}};
    mats[4] = Matrix{{6, 1, 5},
                    {7, 6, 9},
                    {1, 8, 6}};
    mats[5] = Matrix{{6, 7, 5},
                    {5, 6, 4},
                    {7, 9, 6}};
    mats[6] = Matrix{{6, 9, 7},
                    {5, 6, 5},
                    {5, 8, 6}};
    mats[7] = Matrix{{6, 9, 8},
                    {8, 6, 5},
                    {7, 7, 6}};

    for(int i=0; i<8; i++)
    {
        step1 = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, true);
        step2 = Utils::rescaleMod36(Utils::prod(mats[i], step1));
        std::cout<<"======================="<<std::endl;
        std::cout<<"Testing matrix "<<i<<std::endl;
        for(int j=0; j<3; j++)
        {
            std::string cur = get_line(step2, j, int_to_chr_map);
            auto counter = Utils::count(cur);
            std::cout<<"Line "<<j<<" gives ("<<counter.size()<<") "<<cur<<std::endl;
            std::cout<<counter<<std::endl;
            std::cout<<"=> entropy : "<<entropy(cur)<<std::endl;
        }
    }*/

    std::vector<std::string> charsets{"BIPW3GNU18ELSZ6AHOV29CJQX4FMT07DKRY5", "CJQX4HOV29FMT07BIPW3ADKRY5GNU18ELSZ6", "DKRY5IPW3AGNU18CJQX4BELSZ6HOV29FMT07", "ELSZ6JQX4BHOV29DKRY5CFMT07IPW3AGNU18", "FMT07KRY5CIPW3AELSZ6DGNU18JQX4BHOV29", "GNU18LSZ6DJQX4BFMT07EHOV29KRY5CIPW3A", "HOV29MT07EKRY5CGNU18FIPW3ALSZ6DJQX4B",
                                      "18FMT6DKRY4BIPW07ELSZ29GNU5CJQX3AHOV", "29GNU7ELSZ5CJQX18FMT03AHOV6DKRY4BIPW", "3AHOV8FMT06DKRY29GNU14BIPW7ELSZ5CJQX", "4BIPW9GNU17ELSZ3AHOV25CJQX8FMT06DKRY", "5CJQXAHOV28FMT04BIPW36DKRY9GNU17ELSZ", "6DKRYBIPW39GNU15CJQX47ELSZAHOV28FMT0", "7ELSZCJQX4AHOV26DKRY58FMT0BIPW39GNU1",
                                      "MENTIABCDFGHJKLOPQRSUVWXYZ0123456789", "MAGOUZ49EBHPV05NCJQW16TDKRX27IFLSY38"};

    for(const std::string& s : charsets)
    {
        chr_to_int_map = Utils::map_from_charset(s);
        int_to_chr_map = Utils::inverse_map(chr_to_int_map);

        step1 = Utils::convert_string_to_mat(known_text, chr_to_int_map, 3, known_text.size()/3, true);
        step2 = Utils::rescaleMod36(Utils::prod(chosen, step1));
        step3 = Utils::convert_mat_to_string(step2, int_to_chr_map, true);

        for(const std::string& test : charsets)
        {
            chr_to_int_map = Utils::map_from_charset(test);
            int_to_chr_map = Utils::inverse_map(chr_to_int_map);

            step4 = Utils::convert_string_to_mat(step3, chr_to_int_map, 3, step3.size()/3, true);
            for(auto m : correct_matrix)
            {
                step5 = Utils::rescaleMod36(Utils::prod(m, step4));
                step6 = Utils::convert_mat_to_string(step5, int_to_chr_map, true);

                if(Utils::IC(step6)>0.05)
                    std::cout<<"FOUND xD "<<Utils::IC(step6)<<" for "<<step6<<" ("<<test<<")"<<std::endl;
            }
        }
    }

    for(const std::string& test : charsets)
    {
        chr_to_int_map = Utils::map_from_charset(test);
        int_to_chr_map = Utils::inverse_map(chr_to_int_map);

        step4 = Utils::convert_string_to_mat(target_text_ciphered, chr_to_int_map, 3, target_text_ciphered.size()/3, true);
        for(auto m : correct_matrix)
        {
            step5 = Utils::rescaleMod36(Utils::prod(m, step4));
            step6 = Utils::convert_mat_to_string(step5, int_to_chr_map, true);

            if(Utils::IC(step6)>0.05)
                std::cout<<"FOUND xD "<<Utils::IC(step6)<<" for "<<step6<<" ("<<test<<")"<<std::endl;
        }
    }
    /*std::cout<<correct_matrix.size()<<std::endl;
    int c = 0;
    for(auto m : correct_matrix)
    {
        std::cout<<"For iteration "<<c<<std::endl;
        for(int i=1; i<36; i++)
            for(int j=1; j<36; j++)
                if(i!=j)
                    for(int k=1; k<36; k++)
                        if(i!=k && j!=k)
                            for(int l=1; l<36; l++)
                                if(i!=l && j!=l && k!=l)
        {
            Matrix _e55 = {{i},{j},{j}};
            Matrix _ee5 = {{i},{i},{j}};
            Matrix _3e3 = {{k},{i},{k}};
            Matrix _353 = {{k},{j},{k}};
            Matrix _558 = {{j},{j},{l}};

            std::set<int> final_set;
            Matrix tmp = Utils::rescaleMod36(Utils::prod(m, _e55));
            for(int i=0; i<3; i++)
                final_set.insert(tmp[i][0]);
            tmp = Utils::rescaleMod36(Utils::prod(m, _ee5));
            for(int i=0; i<3; i++)
                final_set.insert(tmp[i][0]);
            tmp = Utils::rescaleMod36(Utils::prod(m, _3e3));
            for(int i=0; i<3; i++)
                final_set.insert(tmp[i][0]);
            tmp = Utils::rescaleMod36(Utils::prod(m, _353));
            for(int i=0; i<3; i++)
                final_set.insert(tmp[i][0]);
            tmp = Utils::rescaleMod36(Utils::prod(m, _558));
            for(int i=0; i<3; i++)
                final_set.insert(tmp[i][0]);

            if(final_set.size()<6)
                std::cout<<i<<" "<<j<<" "<<k<<" "<<l<<" "<<final_set.size()<<std::endl;
        }
    }*/

    return 0;
}
