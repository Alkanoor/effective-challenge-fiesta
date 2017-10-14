#include "include/string_tree.hpp"


String_Tree::String_Tree() :
    weight(0),
    terminal(false)
{}

void String_Tree::add_string(const std::string& s)
{
    if(!s.size())
    {
        terminal = true;
        return;
    }
    children[s[0]].add_string(s.substr(1));
}

void String_Tree::add_strings(const std::vector<std::string>& v)
{
    for(auto s : v)
        add_string(s);
}

void String_Tree::add_string_with_weight(const std::string& s, float weight)
{
    if(!s.size())
    {
        this->weight = weight;
        return;
    }
    children[s[0]].add_string_with_weight(s.substr(1), weight);
}

void String_Tree::add_strings_with_weight(const std::vector<std::string>& v, std::vector<float>& weights)
{
    for(size_t i=0; i<v.size(); i++)
        add_string_with_weight(v[i], weights[i]);
}


bool String_Tree::is_completely_in_tree(const std::string& s)
{
    if(!s.size()&&terminal)
        return true;
    else if(!s.size())
        return false;

    if(!children.count(s[0]))
        return false;
    else
        return children[s[0]].is_completely_in_tree(s.substr(1));
}

bool String_Tree::is_partially_in_tree(const std::string& s)
{
    if(!s.size())
        return true;

    if(!children.count(s[0]))
        return false;
    else
        return children[s[0]].is_partially_in_tree(s.substr(1));
}

bool String_Tree::is_completely_in_tree_or_partially_from_size(const std::string& s, int limit_size, int cur_size)
{
    if(!s.size()&&terminal)
        return true;
    else if(!s.size()&&cur_size>=limit_size)
        return true;
    else if(!s.size())
        return false;

    if(!children.count(s[0]))
        return false;
    else
        return children[s[0]].is_completely_in_tree_or_partially_from_size(s.substr(1), limit_size, cur_size+1);
}

float String_Tree::get_weight(const std::string& s)
{
    if(!s.size())
        return weight;

    if(!children.count(s[0]))
        return 0;
    else
        return children[s[0]].get_weight(s.substr(1));
}

bool String_Tree::get_all_children_from_size(const std::string& cur, std::vector<std::string>& children_result, int size, const std::string& model)
{
    if(!cur.size())
    {
        if(terminal)
            children_result.push_back(model);
        if((int)model.size()>=size)
            for(auto i : children)
            {
                std::string model2 = model+i.first;
                i.second.get_all_children_from_size(cur, children_result, size, model2);
            }

        return true;
    }

    if(!children.count(cur[0]))
        return false;

    if(!model.size())
        return children[cur[0]].get_all_children_from_size(cur.substr(1), children_result, size, cur);
    else
        return children[cur[0]].get_all_children_from_size(cur.substr(1), children_result, size, model);
}

std::ostream& String_Tree::show(std::ostream& os, const std::string& cur)
{
    if(terminal)
        os<<cur<<std::endl;
    for(auto i : children)
    {
        std::string cur2 = cur+i.first;
        i.second.show(os, cur2);
    }

    return os;
}
