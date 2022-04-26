#!/bin/bash

if [ "$REQUEST_METHOD" == 'POST' ]
then
    cat | tr '\n' '|' >> log.txt;
    echo "" >> log.txt;
elif [ "$REQUEST_METHOD" == 'GET' ]
then
    echo "content-type: text/plain";
    echo "";
    cat < log.txt;
else
    exit 1;
fi