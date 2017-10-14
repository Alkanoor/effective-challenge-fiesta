#include <iostream>
#include <array>
#include <list>

#include "crypto_part.hpp"


char buf[] = "\x33\x23\x27\x02\x08\xFF\x80\x01\x60\x54\x32\x36\x00\x53\x55\x32\x34\x88\x90\x20\x22\x20\x30\x40\x51\x71\x43\x12\xF1\x10\xA0\x30\xB0\xC0\xD0\x40\xF3\x44\x32\x78\x64\x36\x22\x20\x0A\x33\x81\x91\x1A\x88\x22\x11\x30\x21\x32\x0F\x00\xA0\xB0\xCA\xCC\xFE\xC0\x22\x41\xA0\xA4\x43\xA8\x32\xC1\xC7\x97\x47\x90\xD3\x99\xF1\x32\x34\xE1\x88\x32\x88\x22\x32\x42\x52\x62\xFE\x43\x10\xA0\x36\x97\x91\x53\x48\x10\xFA\x33\x43\xE0\xE8\xF4\x30\x32\xDE\x77\x07\xC1\x81\x37\x11\x22\x01\x12\x24\x91\xFF\xAA\xAC\x55\xCC\xC3\xA1\xC9\xC3\xEE\xFE\xE8\xF4\x32\x00\xAA\x22\x12\xAA\xEE\xDE\x22\xC5\x97\xF5\x32\x44\x48\x20\x00\x10\xEE\xAA\xCC\xDD\xA1\xFE\xFA\x34\x44\x48\xD1\xB3\x0A\x42\x30\x20\x40\xF5\xC1\x30\x32\x40\xCC\xC9\x55\xD5\x20\x10\xC1\xFD\xC3\xCA\xE1\x00\xAA\xF3\xCC\xFD\xEE\xF7\xC1\xD1\xC9\xC4\xC8\xEE\xAA\xEE\xFF\x30\x80\x90\x98\x78\x70\x1F\x76\x33\x74\x72\x01\xC3\x2D\xEE\x99\xCC\x99\xFE\xF4\xAF\xF8\xC4\xC2\x05\x00\xCC\xFF\xFF\x22\x28\x55\xCA\xFF\x87\xC9\xC3\xDD\xF7\x00\xCA\xC2\xC4\xC8\xFE\x00\xA4\x37\xA2\x88\x90\x7F\xD3\x22\xFF\x30\x20\xD9\x3A\x34\x10\x33\x00\xDA\xC1\xD4\xD8\xE4\x01\xE2\x59\x01\xFF\xC1\x10\x20\x30\x40\xF1\xFA\xFE\x20\x49\xE2\xE4\x01\xE4\xEC\x00\xCA\xC2\xC4\xC8\xFE\x00\xE0\x43\xF0\xF2\xF8\xCC\xEE\x20\x43\x24\x01\x11\x32\x80\xCC\xFF\xEE\xAA\xAC\xFC\xFE\xD0\x77\xD4\xC1\x51\x77\x59\xCA\xC3\x90\xFF\x88\x78\x01\x32\x99\xC9\xFD\x8D\x34\x47\x80\x90\x00\x0A\x0C\xEE\xDD";


class Node
{
    public:
        Node(int a, int b, int c, const Node* parent, const std::string& to_reach_here="")
        {
            vals[0] = a;
            vals[1] = b;
            vals[2] = c;
            _parent = parent;
            _to_reach_here = to_reach_here;
        }

        int operator[] (int index) const
        {
            return vals.at(index);
        }

        bool is_node_in_hierarchy(int a, int b, int c) const
        {
            if(a==vals.at(0) && b==vals.at(1) && c==vals.at(2))
                return true;
            else if(_parent)
                return _parent->is_node_in_hierarchy(a,b,c);
            else
                return false;
        }

        void print() const
        {
            std::cout<<"================"<<std::endl;
            print_body();
            std::cout<<_to_reach_here<<std::endl;
        }

        void print_body() const
        {
            std::cout<<vals[0]<<" "<<vals[1]<<" "<<vals[2]<<std::endl;
            if(_parent)
                _parent->print_body();
        }

        const std::array<int, 3>& get_array() const
        {
            return vals;
        }

        const std::string& to_reach_string() const
        {
            return _to_reach_here;
        }

    private:
        const Node* _parent;
        std::array<int, 3> vals;
        std::string _to_reach_here;
};


static std::array<std::string, 6> corresp = {"s", "w", "d", "a", "r", "f"};

void successors(const Node* current, std::list<Node*>& succ)
{
    std::array<int, 3> tmp = current->get_array();
    for(int i=0; i<3; i++)
    {
        if((*current)[i]<6)
        {
            tmp[i]++;
            if(buf[7*tmp[0]+tmp[1]+49*tmp[2]]&1 && !current->is_node_in_hierarchy(tmp[0], tmp[1], tmp[2]))
            {
                Node* tmp_node = new Node(tmp[0], tmp[1], tmp[2], current, current->to_reach_string()+corresp[2*i]);
                succ.push_back(tmp_node);
            }
            tmp[i]--;
        }
        if((*current)[i]>0)
        {
            tmp[i]--;
            if(buf[7*tmp[0]+tmp[1]+49*tmp[2]]&1 && !current->is_node_in_hierarchy(tmp[0], tmp[1], tmp[2]))
            {
                Node* tmp_node = new Node(tmp[0], tmp[1], tmp[2], current, current->to_reach_string()+corresp[2*i+1]);
                succ.push_back(tmp_node);
            }
            tmp[i]++;
        }
    }
}

//ddrrdsssffddrrrssraaaarrddwwfdddrsss C4r1b0U
int main()
{
    std::list<Node*> nodes;
    std::list<Node*> to_delete;
    nodes.push_back(new Node(0, 0, 0, nullptr));
    while(nodes.size())
    {
        Node* n = *nodes.begin();
        to_delete.push_back(n);
        //std::cout<<"Current nodes size : "<<nodes.size()<<std::endl;
        //std::cout<<"Current node : "<<(*n)[0]<<" "<<(*n)[1]<<" "<<(*n)[2]<<std::endl;
        if((*n)[0]==6 && (*n)[1]==6 && (*n)[2]==6)
        {
            std::cout<<"Found fitting n !"<<std::endl;
            n->print();
            std::string path = n->to_reach_string();
            if(compute_entropy_from_string(path)<0.8)
            {
                std::cout<<"Nice it fits entropy ! "<<compute_entropy_from_string(path)<<std::endl;
                goto end;
            }
        }
        nodes.pop_front();
        successors(n, nodes);
    }
end:
    for(auto p : to_delete)
        delete p;

    return 0;
}
