#ifndef GRID_HPP
#define GRID_HPP


#include "crc64.hpp"

#include <stdexcept>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>


struct Point
{
    int x;
    int y;
};

template <typename T>
class Grid
{
    public:
        Grid(T* load_object = nullptr);

        const std::vector<int>& get_switch_index() const;
        std::vector<int> get_current_path() const;
        std::string get_current_hex_path() const;
        std::string get_cardinal_path() const;
        int get_grid_at_switch_index(int index);
        int get_grid_at_index(int index);
        void toggle_switch(int index);

        void update(T* load_object);
        void update();

        void log(std::ostream& os) const;

    private:
        T* _load_object;
        std::vector<std::vector<int> > _grid;
        std::vector<std::vector<int> > _state; //0 means unused,
                                               //1 means used and going down for next,
                                               //2 means used and going left for next,
                                               //3 means used and going up for next,
                                               //4 means used and going right for next
        std::vector<std::vector<int> > _switching_state; //0 means cannot switch,
                                                         //1 means can switch left with down,
                                                         //2 means can switch right with up

        std::vector<Point> _current_path;
        std::vector<int> _switching_index;
        std::vector<int> _current_path_states; //0 means fixed,
                                               //1 means floating currently up,
                                               //2 means floating currently down

        int _width, _height;
};


template <typename T>
Grid<T>::Grid(T* load_object)
{
    update(load_object);
}

template <typename T>
const std::vector<int>& Grid<T>::get_switch_index() const
{
    return _switching_index;
}

template <typename T>
std::vector<int> Grid<T>::get_current_path() const
{
    std::vector<int> ret;
    for(auto p : _current_path)
        ret.push_back(_grid[p.y][p.x]);
    return ret;
}

template <typename T>
std::string Grid<T>::get_current_hex_path() const
{
    std::string ret;
    for(auto p : _current_path)
    {
        std::stringstream ss;
        ss<<std::hex<<std::setfill('0')<<std::setw(2)<<_grid[p.y][p.x];
        ret += ss.str();
    }
    return ret;
}

template <typename T>
std::string Grid<T>::get_cardinal_path() const
{
    std::string ret;
    for(int i=0; i+1<(int)_current_path.size(); i++)
    {
        auto p = _current_path[i];
        switch(_state[p.y][p.x])
        {
            case 1:
                ret += "S";
                break;
            case 2:
                ret += "O";
                break;
            case 3:
                ret += "N";
                break;
            case 4:
                ret += "E";
                break;
        }
    }
    return ret;
}

template <typename T>
int Grid<T>::get_grid_at_switch_index(int index)
{
    Point p = _current_path[_switching_index[index]];
    return _grid[p.y][p.x];
}

template <typename T>
int Grid<T>::get_grid_at_index(int index)
{
    Point p = _current_path[index];
    return _grid[p.y][p.x];
}

template <typename T>
void Grid<T>::toggle_switch(int index)
{
    auto cur_point = _current_path[index];
    auto cur_next_point = _current_path[index+1];
    if(_current_path_states[index] == 1)
    {
        _current_path_states[index] = 2;
        _current_path[index+1] = Point{cur_next_point.x+1, cur_next_point.y+1};
    }
    else if(_current_path_states[index] == 2)
    {
        _current_path_states[index] = 1;
        _current_path[index+1] = Point{cur_next_point.x-1, cur_next_point.y-1};
    }
    else
        std::cerr<<"[-] Asking for switching inexisting switch point at index "<<index<<std::endl;

    auto next_point = _current_path[index+1];
    if(_state[cur_point.y][cur_point.x] == 1)
    {
        _state[cur_point.y][cur_point.x] = 2;
        _state[next_point.y][next_point.x] = 1;
    }
    else if(_state[cur_point.y][cur_point.x] == 2)
    {
        _state[cur_point.y][cur_point.x] = 1;
        _state[next_point.y][next_point.x] = 2;
    }
    else if(_state[cur_point.y][cur_point.x] == 3)
    {
        _state[cur_point.y][cur_point.x] = 4;
        _state[next_point.y][next_point.x] = 3;
    }
    else if(_state[cur_point.y][cur_point.x] == 4)
    {
        _state[cur_point.y][cur_point.x] = 3;
        _state[next_point.y][next_point.x] = 4;
    }
    _state[cur_next_point.y][cur_next_point.x] = 0;
}


template <typename T>
void Grid<T>::update(T* load_object)
{
    _load_object = load_object;
    update();
}

template <typename T>
void Grid<T>::update()
{
    if(!_load_object)
        return;

    try
    {
        auto tmp = _load_object->get_data();
        _height = tmp[0];
        _width = tmp[1];
        _grid.resize(_height);
        _state.resize(_height);
        _switching_state.resize(_height);
        _current_path.clear();
        _switching_index.clear();

        for(int i=0; i<_height; i++)
        {
            _grid[i].resize(_width);
            _state[i].resize(_width);
            _switching_state[i].resize(_width);
            for(int j=0; j<_width; j++)
            {
                _grid[i][j] = tmp[2+i*_width+j];
                _state[i][j] = 0;
                _switching_state[i][j] = 0;
            }
        }

        _current_path.push_back(Point{0, 0});
        _current_path_states.push_back(0);
        int counter=1;
        int prevx=0, prevy=0, x=0, y=1;
        bool right=true, first_step=true;
        while(true)
        {
            _current_path.push_back(Point{x, y});
            _current_path_states.push_back(0);
            if(prevx+1==x)
                _state[prevy][prevx] = 4;
            else if(prevx-1==x)
                _state[prevy][prevx] = 2;
            else if(prevy+1==y)
                _state[prevy][prevx] = 1;
            else
                _state[prevy][prevx] = 3;

            prevx = x;
            prevy = y;

            if(!x)
            {
                int index = 0;
                for(int i=0; i<_height; i++)
                    if(_state[i][x+1])
                        index = i;
                if(y>=index+3 || y+1>=_height)
                    x++;
                else
                    y++;

                right = true;
                first_step = true;
            }
            else if(x==_width-1)
            {
                if(y==_height-1)
                    break;

                int index = 0;
                for(int i=0; i<_height; i++)
                    if(_state[i][x-1])
                        index = i;
                if(y>=index+3)
                    x--;
                else
                    y++;

                right = false;
                first_step = true;
            }
            else if(!y)
            {
                int index = 0;
                for(int i=0; i<_width; i++)
                    if(_state[y+1][i])
                        index = i;
                if(x>=index+3 || x+1>=_width)
                    y++;
                else
                    x++;

                right = false;
                first_step = true;
            }
            else if(y==_height-1)
            {
                if(x==_width-1)
                    break;

                int index = 0;
                for(int i=0; i<_width; i++)
                    if(_state[y-1][i])
                        index = i;
                if(x>=index+3)
                    y--;
                else
                    x++;

                right = true;
                first_step = true;
            }
            else
            {
                if(first_step && right)
                {
                    if(x+2<_width && y>1)
                    {
                        _switching_state[y][x] = 2;
                        _switching_index.push_back(counter);
                        _current_path_states[_current_path_states.size()-1] = 1;
                    }
                    y--;
                }
                else if(right)
                    x++;
                else if(first_step)
                {
                    if(x>1 && y+2<_height)
                    {
                        _switching_state[y][x] = 1;
                        _switching_index.push_back(counter);
                        _current_path_states[_current_path_states.size()-1] = 1;
                    }
                    x--;
                }
                else
                    y++;
                first_step = !first_step;
            }
            counter++;
        }

        if(prevx+1==x)
            _state[prevy][prevx] = 4;
        else if(prevx-1==x)
            _state[prevy][prevx] = 2;
        else if(prevy+1==y)
            _state[prevy][prevx] = 1;
        else
            _state[prevy][prevx] = 3;
    }
    catch(const std::exception& e)
    {
        std::cerr<<"[-] Unable to update grid from bad object : "<<e.what()<<std::endl;
    }
}

template <typename T>
void Grid<T>::log(std::ostream& os) const
{
    if(!_width || ! _height)
    {
        os<<"Empty grid ..."<<std::endl;
        return;
    }
    os<<_width<<"x"<<_height<<" grid"<<std::endl;

    for(int i=0; i<_height; i++)
    {
        for(int j=0; j<_width; j++)
        {
            if(_switching_state[i][j] == 1)
                os<<"l";
            else if(_switching_state[i][j] == 2)
                os<<"u";
            else
                os<<".";

            if(j+1<_width && _state[i][j+1] == 2)
                os<<"<-";
            else if(_state[i][j] == 4)
                os<<"->";
            else
                os<<"  ";
        }
        os<<std::endl;

        for(int j=0; j<_width; j++)
        {
            if(_state[i][j] == 1)
                os<<"!";
            else if(i+1<_height && _state[i+1][j] == 3)
                os<<"|";
            else
                os<<" ";
            os<<"  ";
        }
        os<<std::endl;
    }

    os<<std::endl;
    os<<"Switching index are "<<_switching_index.size()<<std::endl;
    os<<_switching_index<<std::endl;
}


#endif
