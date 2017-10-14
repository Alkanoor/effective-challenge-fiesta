#include "socket.h"


/*Socket::Socket() :
    endpoint(boost::asio::ip::address::from_string("localhost"), 8888),
    socket(ios)
{
	socket.connect(endpoint);
	received.resize(100);
}

void Socket::send(const std::string& s)
{
    std::copy(s.begin(), s.end(), buf.begin());
	socket.write_some(boost::asio::buffer(buf, s.size()), error);
}

const std::string& Socket::recv()
{
    socket.read_some(boost::asio::buffer(data, 100));
    std::copy(data.begin(), data.end(), received.begin());

    return received;
}*/
