#!/bin/bash
#author que
#ssh authentication
for p in $(cat /tmp/ip.txt)
do
ip=$(echo "$p" | cut -f1 -d ":")
password=$(echo "$p" | cut -f2 -d ":")


#expect
expect -c "
spawn ssh-copy-id -i /root/.ssh/id_rsa.pub root@$ip
        expect {
                \"*yes/no*\" {send \"yes\r\"; exp_continue}
                \"*password*\" {send \"$password\r\"; exp_continue}
                \"*Password*\" {send \"$password\r\";}
        }
"
done

