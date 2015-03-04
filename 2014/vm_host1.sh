#!bin/bash
for i in {1..9};do ping -c 3 192.168.1.10$i;done
for i in {1..9};do ping -c 3 192.168.1.11$i;done
sleep 5
for i in {1..9};do ping -c 3 192.168.1.12$i;done
echo "test done"
for i in {1..2};do ping -c 3 192.168.1.13$i;done

