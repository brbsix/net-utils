#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=no-name-in-module

"""Lookup public IP"""

from __future__ import print_function


def first(iterable):
    """Return the first non-null item of an iterable."""

    return next((i for i in iterable if i is not None), '')


def query(url):
    """Query URL for HTTP response."""

    def _requests(url):
        return requests.get(url).text

    def _urllib(url):
        return urlopen(url).read().decode()

    try:
        # use requests if it is available
        import requests
        querytool = _requests
    except ImportError:
        # fallback to urllib
        try:
            from urllib.request import urlopen
        # Python 2 compat
        except ImportError:
            from urllib import urlopen
        querytool = _urllib

    try:
        return querytool(url)
    except:  # pylint: disable=bare-except
        pass


# list of URLs to query for public IP
URLS = ['http://v4.ident.me', 'http://ipecho.net/plain']

print(first((query(url) for url in URLS)))
