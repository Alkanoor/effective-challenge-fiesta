#include "include/crc64.hpp"

#include <iomanip>
#include <sstream>


uint64_t CRC64::_poly = 0xC96C5795D7870F42;

CRC64::CRC64(const std::string& data) :
    _data(data),
    _crc(compute_crc(0, data))
{}

void CRC64::compute_crc_from_hex(const std::string& hex_string)
{
    _crc = 0;
    _data = "";
    update_crc_from_hex(hex_string);
}

void CRC64::compute_crc_from_raw(const std::string& raw_string)
{
    _crc = 0;
    _data = "";
    update_crc_from_raw(raw_string);
}

void CRC64::update_crc_from_hex(const std::string& hex_string)
{
    update_crc_from_raw(hex_to_raw(hex_string));
}

void CRC64::update_crc_from_raw(const std::string& raw_string)
{
    _data += raw_string;
    _crc = compute_crc(_crc, raw_string);
}

std::string CRC64::get_crc_hex() const
{
    std::ostringstream oss;
    oss<<std::hex<<_crc;
    return oss.str();
}

uint64_t CRC64::get_crc() const
{return _crc;}

uint64_t CRC64::compute_crc(uint64_t state, const std::string& raw)
{
    for(auto c : raw)
        state = compute_crc(state, c);
    return state;
}

uint64_t CRC64::compute_crc(uint64_t state, unsigned char byte)
{
    for(int i=0; i<8; i++, byte>>=1)
        state = ((state>>1) & ~((uint64_t)1<<63)) ^ (((state^byte) & 1) ? _poly : 0);
    return state;
}

std::string CRC64::hex_to_raw(const std::string& hex)
{
    int size = (int)(hex.size()+1)/2;
    std::string raw;
    raw.resize(size);

    int offset = 0;
    if(hex.size()%2 == 1)
    {
        std::string byte_string = hex.substr(0, 1);
        unsigned char byte = (char)strtol(byte_string.c_str(), NULL, 16);
        raw[0] = byte;
        offset = 1;
    }

    for(int i=offset; i<size; i++)
    {
        std::string byte_string = hex.substr(offset+(i-offset)*2, 2);
        unsigned char byte = (char)strtol(byte_string.c_str(), NULL, 16);
        raw[i] = byte;
    }

    return raw;
}

std::string CRC64::raw_to_hex(const std::string& raw)
{
    std::string hex;

    for(int i=0; i<(int)raw.size(); i++)
    {
        std::stringstream ss;
        ss<<std::hex<<std::setfill('0')<<std::setw(2)<<(int)(unsigned char)raw[i];
        hex += ss.str();
    }

    return hex;
}

void CRC64::log(std::ostream& os) const
{
    os<<"Data that has been crc(ed) :"<<std::endl;
    os<<raw_to_hex(_data)<<std::endl;
    os<<"CRC : 0x"<<std::hex<<_crc<<std::endl;
}
