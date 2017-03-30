#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=no-name-in-module

"""Lookup public IP"""

from __future__ import print_function

import sys


def first(iterable):
    """Return the first non-null item of an iterable."""
    return next((i for i in iterable if i is not None), None)


def main():
    """Start program."""
    # list of URLs to query for public IP
    urls = ['http://v4.ident.me', 'http://ipecho.net/plain']

    ip_address = first((query(url) for url in urls))
    if ip_address:
        print(ip_address)
    else:
        sys.exit(1)


def query(url):
    """Query URL for HTTP response."""
    request = tool()

    try:
        return request(url)
    except:  # pylint: disable=bare-except
        pass


def tool():
    """Return appropriate HTTP tool."""
    try:
        # use requests if it is available
        import requests
        return lambda url: requests.get(url).text
    except ImportError:
        # fallback to urllib
        try:
            from urllib.request import urlopen
        # Python 2 compat
        except ImportError:
            from urllib import urlopen
        return lambda url: urlopen(url).read().decode()


if __name__ == '__main__':
    main()
