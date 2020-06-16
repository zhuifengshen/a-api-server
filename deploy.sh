#!/bin/bash

echo start deploy...

kill -HUP `cat api_server.pid`
kill `cat api_server.pid`
gunicorn api_server:app -p api_server.pid -b 0.0.0.0:5000 -w 4 -D

echo finish deploy...