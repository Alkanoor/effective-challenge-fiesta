#include "include/load_and_send_to_remote.hpp"
#include "include/utils.hpp"
#include "include/crc64.hpp"
#include "include/grid.hpp"

#include "spoof_crc/spoof.h"

#include <iostream>
#include <cassert>


template <>
class Writable_Ostream<locus>
{
    public:
        Writable_Ostream(const locus& l) :
            _locus(l)
        {}

        void log(std::ostream& os) const
        {
            os<<"["<<_locus.off<<";"<<_locus.pos<<"]";
        }

    private:
        locus _locus;
};

int crc_solve(const std::vector<std::vector<locus> >& loci, std::vector<int>& final_loci, int locs, range_t len, word_t want, model_t model)
{
    int n, i;
    word_t p, sol[(locs + WORDBITS - 1) / WORDBITS];
    word_t mat[locs], mat_bef[locs];

    assert((int)loci.size() == locs);
    assert(locs >= model.dim);
    assert(want <= ONES(model.dim));

    for (int k = 0; k < locs; k++)
    {
        mat[k] = crc_sparse(&(loci[k][0]), loci[k].size(), len, model);
        mat_bef[k] = mat[k];
    }

    int k = gf2_matrix_solve(sol, mat, want, model.dim, locs);
    if (k)
        return -1;

    word_t cur = 0;
    for (k = 0, n = 0, i = 0, p = 1; k < locs; k++, p <<= 1) {
        if (p == 0) {
            p = 1;
            i++;
            cur = 0;
        }
        if (sol[i] & p)
        {
            cur ^= mat_bef[k];
            n++;
            final_loci.push_back(k);
        }
    }

    return n;
}


int main()
{
    Load_From_File loaded("data/input_c");
    Load_And_Send_To_Remote final_load("python_load_send.py", "data/input_c", "data/solution");
    //Grid<Load_From_File> to_work_on(&loaded);
    Grid<Load_And_Send_To_Remote> to_work_on(&final_load);
    std::cout<<to_work_on<<std::endl;

    std::string hex_path = to_work_on.get_current_hex_path();
    hex_path.resize(hex_path.size()-2);
    CRC64 crc;
    crc.compute_crc_from_hex(hex_path);

    auto switch_points = to_work_on.get_switch_index();

    model_t model;
    word_t want;
    range_t len;

    model.dim = 64;
    model.ref = 1;
    model.poly = 0xC96C5795D7870F42;
    want = 0x4242424242424242^crc.get_crc();
    len = (hex_path.size()-2)/2;


    std::vector<std::vector<locus> > loci;
    std::vector<int> final_loci;
    int locs = (int)switch_points.size();
    for(int i=0; i<locs; i++)
    {
        std::vector<locus> cur_loci;
        int a = to_work_on.get_grid_at_index(switch_points[i]+1);
        to_work_on.toggle_switch(switch_points[i]);
        int b = to_work_on.get_grid_at_index(switch_points[i]+1);
        to_work_on.toggle_switch(switch_points[i]);
        int c = a^b;
        for(int j=0; j<8; j++)
            if(c&(1<<j))
                cur_loci.push_back(locus{(range_t)switch_points[i]+1, (short)j});
        if(cur_loci.size())
            loci.push_back(cur_loci);
    }
    locs = (int)loci.size();
    crc_solve(loci, final_loci, locs, len+1, want, model);

    for(int it : final_loci)
        to_work_on.toggle_switch(switch_points[it]);

    std::cout<<to_work_on<<std::endl;

    hex_path = to_work_on.get_current_hex_path();
    hex_path.resize(hex_path.size()-2);
    crc.compute_crc_from_hex(hex_path);
    std::cout<<"Giving CRC64 : "<<std::endl;
    std::cout<<crc<<std::endl;

    std::string final_path = to_work_on.get_cardinal_path();
    std::cout<<final_path<<std::endl;

    final_load.send_result(final_path);

    return 0;
}



#define NO_DIRTY

#ifndef NO_DIRTY

int main()
{
    /** test pour etre sur que le CRC est bon **/

    /**
    CRC64 test;
    test.compute_crc_from_hex("161a653b38");
    std::cout<<test<<std::endl;

    // Data that has been crc(ed) :
    // 161a653b38
    // CRC : 0x181c307118953949

    **/

    Load_From_File loaded("data/input_c");
    std::cout<<loaded.get_data()<<std::endl;
    Grid<Load_From_File> to_work_on(&loaded);
    std::cout<<to_work_on<<std::endl;

    std::cout<<to_work_on.get_current_path()<<std::endl;
    std::cout<<to_work_on.get_current_hex_path()<<std::endl<<std::endl;
    std::string hex_path = to_work_on.get_current_hex_path();
    hex_path.resize(hex_path.size()-2);
    CRC64 crc;
    crc.compute_crc_from_hex(hex_path);
    std::cout<<"Giving CRC64 : "<<std::endl;
    std::cout<<crc<<std::endl;

    auto switch_points = to_work_on.get_switch_index();

    /*std::cout<<"Before at "<<switch_points[0]<<" and "<<switch_points[0]+1<<" : "<<to_work_on.get_grid_at_index(switch_points[0])<<" ; "<<to_work_on.get_grid_at_index(switch_points[0]+1)<<std::endl;
    to_work_on.toggle_switch(switch_points[0]);
    to_work_on.toggle_switch(switch_points[2]);
    to_work_on.toggle_switch(switch_points[4]);
    to_work_on.toggle_switch(switch_points[6]);
    std::cout<<"After at "<<switch_points[0]<<" and "<<switch_points[0]+1<<" : "<<to_work_on.get_grid_at_index(switch_points[0])<<" ; "<<to_work_on.get_grid_at_index(switch_points[0]+1)<<std::endl<<std::endl;
    std::cout<<to_work_on.get_current_hex_path()<<std::endl<<std::endl;

    std::cout<<to_work_on<<std::endl;

    to_work_on.toggle_switch(switch_points[0]);
    to_work_on.toggle_switch(switch_points[2]);
    to_work_on.toggle_switch(switch_points[4]);
    to_work_on.toggle_switch(switch_points[6]);
    std::cout<<"Still after at "<<switch_points[0]<<" and "<<switch_points[0]+1<<" : "<<to_work_on.get_grid_at_index(switch_points[0])<<" ; "<<to_work_on.get_grid_at_index(switch_points[0]+1)<<std::endl<<std::endl;

    std::cout<<to_work_on<<std::endl;*/

    //std::string hex_path = to_work_on.get_current_hex_path();


    int k;
    model_t model;
    word_t want;
    range_t len;

    model.dim = 64;
    model.ref = 1;
    model.poly = 0xC96C5795D7870F42;
    want = 0x4242424242424242^crc.get_crc();
    len = (hex_path.size()-2)/2;

    if (model.dim > WORDBITS)
        fail("CRC too long for crc integer type spoof was compiled with");
    if (model.dim < 1 || model.ref < 0 || model.ref > 1 ||
                   model.poly > ONES(model.dim))
        fail("invalid CRC description");
    if ((model.poly & ((word_t)1 << (model.ref ? model.dim - 1 : 0))) == 0)
        fail("invalid polynomial (you may need to reverse the bits)");

    if (want > ONES(model.dim))
        fail("invalid target CRC");
    if (len < (range_t)((model.dim + 7) >> 3))
        fail("invalid sequence length (must be at least length of CRC)");

    k = model.dim << 1;

    std::cout<<k<<" "<<model.dim<<" "<<want<<" "<<len<<std::endl;

    std::vector<std::vector<locus> > loci;
    std::vector<int> final_loci;
    int locs = (int)switch_points.size();
    for(int i=0; i<locs; i++)
    {
        std::vector<locus> cur_loci;
        int a = to_work_on.get_grid_at_index(switch_points[i]+1);
        to_work_on.toggle_switch(switch_points[i]);
        int b = to_work_on.get_grid_at_index(switch_points[i]+1);
        to_work_on.toggle_switch(switch_points[i]);
        int c = a^b;
        for(int j=0; j<8; j++)
            if(c&(1<<j))
                cur_loci.push_back(locus{(range_t)switch_points[i]+1, (short)j});
        if(cur_loci.size())
            loci.push_back(cur_loci);
    }
    locs = (int)loci.size();
    std::cout<<loci<<std::endl<<len<<std::endl;
    std::cout<<crc_solve(loci, final_loci, locs, len+1, want, model)<<std::endl;

    /*for(int i=0; i<(int)switch_points.size(); i++)
    {
        int a = to_work_on.get_grid_at_index(switch_points[i]+1);
        to_work_on.toggle_switch(switch_points[i]);
        int b = to_work_on.get_grid_at_index(switch_points[i]+1);
        to_work_on.toggle_switch(switch_points[i]);
        int c = a^b;
        std::stringstream ss;
        ss<<std::hex<<c;
        std::string tmp;
        for(int j=0; j<(int)len-switch_points[i]-1; j++)
            tmp += "00";
        crc.compute_crc_from_hex(ss.str()+tmp);
        std::cout<<crc;
    }*/

    std::cout<<final_loci<<std::endl;
    for(int it : final_loci)
    {
        std::cout<<switch_points[it]<<std::endl;
        to_work_on.toggle_switch(switch_points[it]);
    }

    std::cout<<to_work_on<<std::endl;

    hex_path = to_work_on.get_current_hex_path();
    hex_path.resize(hex_path.size()-2);
    crc.compute_crc_from_hex(hex_path);
    std::cout<<"Giving CRC64 : "<<std::endl;
    std::cout<<crc<<std::endl;

    /*crc.compute_crc_from_hex("0065d0458bfc838f132ca1cd25428cbf7b110c51c04029b8cab26f1ddda0f7bf226d44bb82ef00ca2b9554bf6836beba09f83d13f9b98aa1eb4b6a49a621ccc633ba36d2295c39ba83ee3f0b73ea3a8c4c7979723066a544d79299fc748d6bab9afd73f833fdbf01c3d499d702a4ab22a951e83e10c2c96fe8006440cdd66652afec86fe9512937210778d70f191962134411b29356858759815ee121a9a2cba3f6641560873eca50046b0f6bdb96547bba33d92be6189f5c5922bd7551feca227fb274f55178518b833a61678aa12032df90600b37b679e88c6361c1df97c430233fd505536677d3c091b2d1fa0343205aff60dfd1b91b5643a69952503b3af0661a700bda97cca");
    std::cout<<crc<<std::endl;
    crc.compute_crc_from_hex("0065d0458bfc838f132ca1cd2542dbbf7b110c51c04029b8cab26f1ddda0f7bf226d44bb82ef00ca2b9554bf6836beba09f83d13f9b98aa1eb4b6a49a621ccc633ba36d2295c39ba83ee3f0b73ea3a8c4c7979723066a544d79299fc748d6bab9afd73f833fdbf01c3d499d702a4ab22a951e83e10c2c96fe8006440cdd66652afec86fe9512937210778d70f191962134411b29356858759815ee121a9a2cba3f6641560873eca50046b0f6bdb96547bba33d92be6189f5c5922bd7551feca227fb274f55178518b833a61678aa12032df90600b37b679e88c6361c1df97c430233fd505536677d3c091b2d1fa0343205aff60dfd1b91b5643a69952503b3af0661a700bda97cca");
    std::cout<<crc<<std::endl;

    int a = to_work_on.get_grid_at_index(switch_points[2]+1);
    to_work_on.toggle_switch(switch_points[2]);
    int b = to_work_on.get_grid_at_index(switch_points[2]+1);
    to_work_on.toggle_switch(switch_points[2]);
    int c = a^b;

    std::cout<<"Given c = "<<c<<std::endl;
    std::stringstream ss;
    ss<<std::hex<<c;
    std::string tmp;
    for(int j=0; j<(int)len-switch_points[2]-1; j++)
        tmp += "00";
    crc.compute_crc_from_hex(ss.str()+tmp);
    std::cout<<crc;*/

    return 0;
}


int crc_solve(const std::vector<std::vector<locus> >& loci, std::vector<int>& final_loci, int locs, range_t len, word_t want, model_t model)
{
    int n, i;
    word_t p, sol[(locs + WORDBITS - 1) / WORDBITS];
    word_t mat[locs], mat_bef[locs];

    assert((int)loci.size() == locs);
    assert(locs >= model.dim);
    assert(want <= ONES(model.dim));

    for (int k = 0; k < locs; k++)
    {
        mat[k] = crc_sparse(&(loci[k][0]), loci[k].size(), len, model);
        mat_bef[k] = mat[k];
    }

    int k = gf2_matrix_solve(sol, mat, want, model.dim, locs);
    if (k)
        return -1;

    word_t cur = 0;
    for (k = 0, n = 0, i = 0, p = 1; k < locs; k++, p <<= 1) {
        if (p == 0) {
            p = 1;
            i++;
            cur = 0;
        }
        if (sol[i] & p)
        {
            cur ^= mat_bef[k];
            n++;
            final_loci.push_back(k);
        }
    }

    return n;
}

#endif
