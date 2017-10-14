#include "request_manager.h"

#include <iostream>


Request_manager::Request_manager()
{
    curl_ = curl_easy_init();
    if(!curl_)
    {
        std::cerr<<"Curl init failed"<<std::endl;
        exit(1);
    }

    CURLcode res = curl_easy_setopt(curl_, CURLOPT_WRITEFUNCTION, &Request_manager::write_body_callback);
    if(res)
    {
        std::cerr<<"Curl setopt writefunction failed : "<<res<<std::endl;
        exit(1);
    }
    res = curl_easy_setopt(curl_, CURLOPT_HEADERFUNCTION, &Request_manager::write_header_callback);
    if(res)
    {
        std::cerr<<"Curl setopt headerfunction failed : "<<res<<std::endl;
        exit(1);
    }
    res = curl_easy_setopt(curl_, CURLOPT_WRITEDATA, (void*)this);
    if(res)
    {
        std::cerr<<"Curl setopt writedata failed : "<<res<<std::endl;
        exit(1);
    }
    res = curl_easy_setopt(curl_, CURLOPT_HEADERDATA, (void*)this);
    if(res)
    {
        std::cerr<<"Curl setopt headerdata failed : "<<res<<std::endl;
        exit(1);
    }
}

Request_manager::~Request_manager()
{
    curl_easy_cleanup(curl_);
}

void Request_manager::set_url(const std::string& url)
{
    curl_easy_setopt(curl_, CURLOPT_URL, url.c_str());
}

void Request_manager::set_cookie(const std::string& cookie)
{
    curl_easy_setopt(curl_, CURLOPT_COOKIE, cookie.c_str());
}

void Request_manager::perform()
{
    CURLcode res = curl_easy_perform(curl_);
    if(res)
    {
        std::cerr<<"Curl perform failed : "<<res<<std::endl;
        exit(1);
    }
}

void Request_manager::set_body(const std::string& body)
{body_ = body;}

void Request_manager::set_header(const std::string& header)
{header_ = header;}

const std::string& Request_manager::body() const
{return body_;}

const std::string& Request_manager::header() const
{return header_;}

size_t Request_manager::write_body_callback(char *ptr, size_t size, size_t nmemb, void *userdata)
{
    Request_manager* manager = (Request_manager*)userdata;
    manager->set_body(std::string(ptr));
    return manager->body().size();;
}

size_t Request_manager::write_header_callback(char *ptr, size_t size, size_t nmemb, void *userdata)
{
    Request_manager* manager = (Request_manager*)userdata;
    manager->set_header(std::string(ptr));
    return manager->header().size();
}
