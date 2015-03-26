# net-utils

This is a small collection of simple Bash shell scripts I've created for personal use. They're mostly useful integrated with more complex scripts.

Scripts
--------

* **digname** - Query the hostname of an IP address via dig
* **geoip-fx** - Query geoiplookup for data on a target hostname or IP address (requires geoiplookup)
* **http-response** - Get the HTTP response code for a URL
* **netcheck** - Check for INTERNET and/or LOCAL network access
* **public-ip-logger** - Log public IP address and hostname (if available)
* **pulse** - Check whether network targets are DEAD or ALIVE
* **whatismyip** - Lookup public IP and/or hostname

Installation
------------

To install to your system bin folder:

    sudo install -t /usr/local/bin scripts/*

To install to your local bin folder:

    install -d $HOME/.local/bin
    install -t $HOME/.local/bin scripts/*

*NOTE: Ensure that your local bin folder is on your PATH*

Usage
-----

Most of the scripts include a usage string accessible via `script --help`.

License
-------

Copyright (c) 2015 Six (brbsix@gmail.com).

Licensed under the GPLv3 license.
