#include "hashmap.hpp"
#include <iostream>

int main()
{
    HashMap h;
    std::cout<<h.add_and_check(0x4242424242424242)<<std::endl;
    std::cout<<h.add_and_check(0x4242424241424242)<<std::endl;
    std::cout<<h.add_and_check(0x4242424242424142)<<std::endl;
    std::cout<<h.add_and_check(0x4241424242424242)<<std::endl;
    std::cout<<h.add_and_check(0x4242424241424242)<<std::endl;
}
