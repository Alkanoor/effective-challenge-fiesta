#ifndef REQUEST_MANAGER_H
#define REQUEST_MANAGER_H


#include <sys/select.h>
#include <curl/curl.h>
#include <string>


class Request_manager
{
    public:
        Request_manager();
        ~Request_manager();

        void set_url(const std::string& url);
        void set_cookie(const std::string& cookie);

        void perform();

        void set_body(const std::string& body);
        void set_header(const std::string& header);

        const std::string& body() const;
        const std::string& header() const;

        static size_t write_body_callback(char *ptr, size_t size, size_t nmemb, void *userdata);
        static size_t write_header_callback(char *ptr, size_t size, size_t nmemb, void *userdata);

    private:
        CURL *curl_;
        std::string body_;
        std::string header_;
};


#endif
