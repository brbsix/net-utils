# net-utils

This is a small collection of simple Bash shell scripts I've created for personal use.

Scripts
--------

* digname - Query the hostname of an IP address via dig
* geoip-fx - Query geoiplookup for data on a target hostname or IP address (requires geoiplookup)
* http-response - Get the HTTP response code for a URL
* netcheck - Check for INTERNET and/or LOCAL network access
* public-ip-logger - Log public IP address and hostname (if available)
* pulse - Check whether network targets are DEAD or ALIVE
* whatismyip - Lookup public IP and/or hostname

Installation
------------

Copy scripts to your bin folder (generally /usr/local/bin or $HOME/.local/bin) then mark as executable.

Usage
-----

Should be self-explanatory... Most of the scripts include a usage string that can be accessed via `script --help`.

License
-------

Copyright (c) 2015 Six (brbsix@gmail.com).

Licensed under the GPLv3 license.
