#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Lookup public IP"""


# list of URLs to query for public IP
URLS = ['http://v4.ident.me',
        'http://ipecho.net/plain']


def multiquery(urls):
    """Query multiple URLs for HTTP response and return first success."""

    for url in urls:
        try:
            response = query(url)
        except:
            continue

        if response:
            return response


def query(url):
    """Query URL for HTTP response."""
    import pycurl
    from io import BytesIO

    storage = BytesIO()

    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(curl.WRITEFUNCTION, storage.write)
    curl.perform()
    curl.close()

    output = storage.getvalue().decode()

    return output if output else None


print(multiquery(URLS))
