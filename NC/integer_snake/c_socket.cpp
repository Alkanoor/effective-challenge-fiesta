#include "c_socket.h"


bool C_socket::initialized = false;

C_socket::C_socket()
{
    if(!initialized)
        init();

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if(sock == INVALID_SOCKET)
    {
        perror("socket()");
        exit(errno);
    }

    struct hostent *hostinfo = NULL;
    SOCKADDR_IN sin = { 0 };
    const char *hostname = "localhost";

    hostinfo = gethostbyname(hostname);
    if(hostinfo == NULL)
    {
        fprintf(stderr, "Unknown host %s.\n", hostname);
        exit(EXIT_FAILURE);
    }

    sin.sin_addr = *(IN_ADDR *) hostinfo->h_addr;
    sin.sin_port = htons(8888);
    sin.sin_family = AF_INET;

    if(connect(sock,(SOCKADDR *) &sin, sizeof(SOCKADDR)) == SOCKET_ERROR)
    {
        perror("connect()");
        exit(errno);
    }

    str.resize(1024);
}

C_socket::~C_socket()
{
    closesocket(sock);
}

void C_socket::send_message(const std::string& s)
{
	if(send(sock, s.c_str(), s.size(), 0) < 0)
    {
        perror("send()");
        exit(errno);
    }
}

const std::string& C_socket::recv_message()
{
    int n = 0;
    if((n = recv(sock, &str[0], 1023, 0)) < 0)
    {
        perror("recv()");
        exit(errno);
    }

    str[n] = 0;
    cpy = str.substr(0,n);

    return cpy;
}


void C_socket::init(void)
{
#ifdef WIN32
    WSADATA wsa;
    int err = WSAStartup(MAKEWORD(2, 2), &wsa);
    if(err < 0)
    {
        puts("WSAStartup failed !");
        exit(EXIT_FAILURE);
    }
#endif
    initialized = true;
}

void C_socket::end(void)
{
#ifdef WIN32
    WSACleanup();
#endif
}
