#!/usr/bin/python

import io
import re
import pycurl
import certifi
import StringIO
from urllib import urlencode


def clear(o):
    o.truncate(0)
    o.seek(0)

body_buffer = StringIO.StringIO()
header_buffer = StringIO.StringIO()


c = pycurl.Curl()
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.SSL_VERIFYHOST, 0)
c.setopt(c.WRITEFUNCTION, body_buffer.write)
c.setopt(c.HEADERFUNCTION, header_buffer.write)

c.setopt(c.COOKIE, '')

c.setopt(c.URL, 'http://vip.hacking.w3challs.com/')
c.setopt(c.POSTFIELDS, urlencode({}))
c.perform()

body = body_buffer.getvalue()
header = header_buffer.getvalue()

print(body)
print(header)

clear(body_buffer)
clear(header_buffer)
