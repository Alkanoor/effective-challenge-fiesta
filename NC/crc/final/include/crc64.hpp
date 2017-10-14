#ifndef CRC64_HPP
#define CRC64_HPP


#include <string>


class CRC64
{
    public:
        CRC64(const std::string& data = "");

        void compute_crc_from_hex(const std::string& hex_string);
        void compute_crc_from_raw(const std::string& raw_string);
        void update_crc_from_hex(const std::string& hex_string);
        void update_crc_from_raw(const std::string& raw_string);

        std::string get_crc_hex() const;
        uint64_t get_crc() const;

        static uint64_t compute_crc(uint64_t state, const std::string& raw);
        static uint64_t compute_crc(uint64_t state, unsigned char c);

        static std::string hex_to_raw(const std::string& hex_string);
        static std::string raw_to_hex(const std::string& raw_string);

        void log(std::ostream& os) const;

    private:
        std::string _data;
        uint64_t _crc;

        static uint64_t _poly;
};


#endif
