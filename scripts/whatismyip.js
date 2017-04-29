#!/usr/bin/env node
/* jshint esversion: 6 */

const http = require('http');

function get (url, callback) {
    return http.get(url, function (response) {
        // continuously update stream with data
        let body = '';
        response.on('data', function (d) {
            body += d;
        });
        response.on('end', function () {
            callback(body);
        });
    });
}

get('http://v4.ident.me', r => console.log(r));
