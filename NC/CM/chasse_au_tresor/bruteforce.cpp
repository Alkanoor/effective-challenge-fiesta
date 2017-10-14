#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>

#ifdef WIN32
#include <windows.h>
#else
#include <unistd.h>
#define Sleep sleep
#endif


#define N 60000

std::string s[5] = {
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx *+      O xxx#==      = xxxxxxxx x#xxxxxxxxxxxxx#xxxxxxxxxxS  #xxxxxxxxxxxxxxxxxx",
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx     #####xxxx +O+     #xxxx ===     #xxxxxxxxx    #xxxx       ++#xxxx +   S ==#xxxxxxxx xxxxxxxxxxxxxxxxxxxxxx",
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       O  +xxx* O ##### =xxx  +      # xxx OxO  O O# xxx =+=# O O# xxxxOOO#++Ox# xxxxOxxxOxOx# xxxxOxxxOxOx#Sxxxxxxxxxxxxxxxx",
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx =OOOOOOO=Sxxx#=+O+++++=#xxx#=++O++++=#xxx#=+++O+++=#xxx#=++++O++=#xxx#=+++++O+=#xxx#=++++++O=#xxx#=+++++++=#xxxxxxxxxxxxxxxx",
  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx+ xxxxxxxxxxxxx#xxx    O   x #xxx #x+=   x #xxx #x#OO  x #xxx#===+=O S #xxx#   ===#x  xxx########x  xxxxxxxxxxxxxxxx"
};


bool try_solution(const std::string& to_try, const std::string& base, int& position, std::string& after)
{
  int v20 = position;
  int v1 = 0, v2, v3;
  int v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18;
  int i, j;
  after = base;
  while ( 1 )
  {
    //std::cout<<v1<<std::endl;
    if(v1>=to_try.size())
        return false;
    if ( v1 == 512 )
      return 1;
    v2 = to_try[v1];
    if ( v2 == 76 )
    {
      v4 = v20;
      v3 = after[v20-1];
      switch ( v3 )
      {
        case 32:
          v4 = v20 - 1;
          break;
        case 79:
          v2 = after[v20-2];
          if ( v2 == 32 )
          {
            after[v20-2] = 79;
            after[v20-1] = 32;
          }
          break;
        case 43:
          v4 = v20 - 1;
          after[v20 - 1] = 32;
          break;
        case 42:
          v4 = v20 - 1;
          after[v20 - 1] = 32;
          break;
        case 61:
          v4 = v20 - 1;
          after[v20 - 1] = 32;
          break;
        case 35:
          v4 = v20 - 1;
          break;
      }
      v20 = v4;
      goto LABEL_48;
    }
    if ( v2 != 82 )
    {
      if ( v2 == 85 )
      {
        v6 = v20;
        v3 = after[v20-14];
        if ( v3 == 32 )
        {
          v2 = after[v20];
          if ( v2 == 35 )
            v6 = v20 - 14;
        }
        else if ( v3 == 35 )
        {
          v2 = after[v20];
          if ( v2 == 35 )
            v6 = v20 - 14;
        }
        goto LABEL_40;
      }
      if ( v2 == 68 )
      {
        v6 = v20;
        v3 = after[v20+14];
        if ( v3 == 32 )
        {
          v7 = v20 + 14;
        }
        else
        {
          if ( v3 != 35 )
          {
LABEL_40:
            v20 = v6;
            goto LABEL_48;
          }
          v7 = v20 + 14;
        }
        v20 = v7;
        goto LABEL_48;
      }
      return false;
    }
    v5 = v20;
    v3 = after[v20+1];
    switch ( v3 )
    {
      case 32:
        v5 = v20 + 1;
        break;
      case 79:
        v2 = after[v20+2];
        if ( v2 == 32 )
        {
          after[v20+2] = 79;
          after[v20+1] = 32;
        }
        break;
      case 43:
        v5 = v20 + 1;
        after[v20 + 1] = 32;
        break;
      case 42:
        v5 = v20 + 1;
        after[v20 + 1] = 32;
        break;
      case 61:
        v5 = v20 + 1;
        after[v20 + 1] = 32;
        break;
      case 35:
        v5 = v20 + 1;
        break;
    }
    v20 = v5;
    i = 0;
LABEL_48:
    //std::cout<<to_try.substr(0,v1)<<" "<<v20<<std::endl;
    //std::cout<<after<<std::endl;
    for ( ; i != 196; ++i )
    {
      v9 = after[i];
      if ( v9 == 42 || v9 == 43 )
      {
LABEL_56:
        for (j = 195; j != -1; --j )
        {
          if ( after[j] == 32 )
          {
            v13 = v20;
            if ( v20 != j )
            {
              int v13 = after[j-14];
              if ( v13 == 79 )
              {
                v14 = v1;
                v15 = after[j-14];
                after[j-14] = 32;
                after[j] = v15;
                //std::cout<<after<<std::endl;
                v1 = v14;
                goto LABEL_56;
              }
              if ( v13 == 43 )
              {
                v16 = v1;
                v17 = after[j-14];
                after[j-14] = 32;
                after[j] = v17;
                //std::cout<<after<<std::endl;
                v1 = v16;
                goto LABEL_56;
              }
              v18 = v20;
              v2 = j - 14;
              if ( j - 14 == v20 )
              {
                int v18 = after[j-14];
                if ( v18 != 35 )
                {
                  v2 = v20 + 14;
                  v20 += 14;
                  goto LABEL_56;
                }
              }
              else
              {
                v2 = j;
              }
            }
          }
        }
        goto LABEL_69;
      }
    }
    position = v20;
    return true;

LABEL_69:
      v3 = 0;
      ++v1;
      position = v20;
      continue;
  }
  position = v20;
  return false;
}

int test(std::string& str)
{
  int j;
  for (j = 0; ; ++j)
  {
    int v2 = str[j];
    if ( v2 == 83 )
      break;
  }
  str[j] = 32;
  return j;
}

bool is_bad(const std::string& s)
{
    for(int i=0;i+2<s.size();i++)
        if(s[i]=='O' && (s[i+1]=='+' || s[i+1]=='*') && s[i+2] == 'O')
            return true;
    return false;
}

int count_symbols(const std::string& str)
{
  int n = 0;
  for(int i=0; i<(int)str.size(); i++)
    if(str[i]=='*' || str[i]=='+')
      n++;
  return n;
}

std::string int_to_str(int a)
{
  std::ostringstream oss;
  oss<<a;
  return oss.str();
}

class State
{
  public:
    State(const std::string& s="", const std::string& input="", int offset=0, State* parent_ = NULL) :
      state(s),
      in(input),
      off(offset),
      parent(parent_),
      cur(this)
    {}

    State(const State& s) :
      state(s.state),
      in(s.in),
      off(s.off),
      parent(s.parent),
      cur(this)
    {}

    std::string state;
    std::string in;
    int off;
    State* parent;
    State* cur;

    bool is_ancestor(const std::string& str, int position)
    {
      State* p = cur;
      while(p)
      {
        if(p->off==position&&p->state==str)
          return true;
        p = p->parent;
      }
      return false;
    }

    std::ostream& log(std::ostream& os)
    {
      os<<in<<" at position "<<off<<" => giving "<<state<<" wuth parent "<<parent<<std::endl;
      return os;
    }
};



int main()
{
  std::vector<int> pos(5, 0);
  std::vector<std::string> initial1(5);
  std::vector<std::string> initial2(5);
  std::vector<State> initial3(5);
  for(int i=0; i<5; i++)
  {
    pos[i] = test(s[i]);
    initial1[i] = s[i];
    initial2[i] = "";
    initial3[i] = State(s[i], "", pos[i]);
  }

  int position = 0;
  std::string after;

  std::string possibilities[4] = {"L", "U", "R", "D"};
  std::vector<State*> alls;
  std::string final;
  for(int i=0; i<5; i++)
  {
    std::map<std::string, State*> states_cpy;
    std::map<std::string, State*> states_cpy_tmp;
    std::map<int, std::set<std::string> > all_states;
    states_cpy[initial2[i]] = new State(initial3[i]);
    all_states[count_symbols(initial2[i])].insert(initial1[i]+int_to_str(pos[i]));
    alls.push_back(states_cpy[initial2[i]]);

    int min = -1;
    bool found = false;
    while(!found)
    {
      states_cpy_tmp = states_cpy;
      states_cpy.clear();
      for(auto it : states_cpy_tmp)
      {
        std::string cur = it.second->state;
        std::vector<State*> children;
        for(int j=0; j<4; j++)
        {
          std::string to_test = it.second->in+possibilities[j];
          int position = pos[i];
          if(try_solution(to_test, initial1[i], position, after))
          {
            found = true;
            std::cout<<"Found item "<<i<<" : "<<std::endl;
            std::cout<<to_test<<" => "<<position<<", "<<after<<std::endl;
            final += to_test;
            if(i<4)
              final += "-";
            Sleep(1);
            //exit(0);
            break;
          }

          if(!is_bad(after) && !all_states[count_symbols(after)].count(after+int_to_str(position)))
          {
            all_states[count_symbols(after)].insert(after+int_to_str(position));
            states_cpy[to_test] = new State(after, to_test, position, it.second->cur);
            alls.push_back(states_cpy[to_test]);
            children.push_back(states_cpy[to_test]);
          }
        }
        if(found)
          break;
      }

      if(!states_cpy.size())
      {
        std::cout<<"Not found at all :'("<<std::endl;
        exit(1);
      }
      else if(states_cpy.size()>N)
      {
          std::map<int, int> m;
          std::map<std::string, State*> to_keep;
          std::vector<std::string> tmp(states_cpy.size());
          int j = 0;
          for(auto it : states_cpy)
          {
              int a = count_symbols(it.second->state);
              if(m.count(a))
                m[a]++;
              else
                m[a] = 1;
          }
          int sum = 0, threshold;
          auto b = m.begin();
          while(b != m.end() && sum<N)
          {
              sum += b->second;
              threshold = b->first;
              b++;
          }
          j = 0;
          for(auto it : states_cpy)
              if(count_symbols(it.second->state)<=threshold)
              {
                  tmp[j] = it.first;
                  j++;
              }
          tmp.resize(j);
          //std::random_shuffle(tmp.begin(), tmp.end());
          for(int j=0; j<tmp.size(); j++)
            to_keep[tmp[j]] = states_cpy[tmp[j]];
          states_cpy = to_keep;
          std::cout<<"Current histogram :"<<std::endl;
          for(auto b : m)
            std::cout<<b.first<<" => "<<b.second<<std::endl;
      }

      std::cout<<"Not found yet, testing with "<<states_cpy.size()<<" sized"<<std::endl;
    }

    for(auto i : alls)
      delete i;
    alls.clear();
  }

  std::cout<<"Final String :) "<<final<<std::endl;
  return 0;
}
