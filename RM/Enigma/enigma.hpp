#include <iostream>
#include <string>
#include <vector>
#include <array>

#include "util.hpp"


class Enigma
{
    public:
        void reset(const std::array<unsigned char, 3>& s, const std::array<int, 3>& ro, const std::array<unsigned char, 3>& ri, const std::map<unsigned char, unsigned char>& corresp = std::map<unsigned char, unsigned char>(), int reflector = 1);

        unsigned char apply_rotor(unsigned char c, int offset, const std::string& key);
        unsigned char reflect(unsigned char c);
        unsigned char subst(unsigned char c, int offset = 0, const std::string& key="ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        void advance_rotor();
        unsigned char encipher_char(unsigned char c, bool debug=false);

        void set_cipher(const std::string& c);
        const std::string& cipher_decipher();

        bool is_config_ok(const std::array<unsigned char, 3>& setting, int offset);

        static bool is_char_ok(unsigned char c);
        static unsigned char norm_ok(unsigned char c);

    private:
        static std::array<std::string, 8> rotorkey;
        static std::array<std::string, 8> invrotor;
        static std::array<std::string, 3> reflectorkey;
        static std::array<std::vector<unsigned char>, 8> notch;

        std::map<unsigned char, unsigned char> correspondances;
        std::array<unsigned char, 3> settings;
        std::array<int, 3> rotors;
        std::array<unsigned char, 3> ringstellung;
        int reflector_index;

        std::string cipher;
        std::string clear;
};
