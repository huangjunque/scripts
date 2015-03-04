#!/bin/bash
ssh_host="root@192.168.1.18"
file="/usr/local/nginx/conf/nginx.conf"

if ssh $ssh_host test -e $file;
    then echo $file exists
    else echo $file does not exists 
fi
