#!/bin/bash
#pingall
cat /etc/hosts | grep -v '^#'  | while read LINE
do
    ADDR=`awk '{print $1}'`
    for HOST in $ADDR
    do
        ping -c 3 $HOST 
    done 
done 
