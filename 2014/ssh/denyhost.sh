#!/bin/bash
cat /var/log/secure | awk '/Failed/{print $(NF -3)}'|sort | uniq -c | awk '{print $2"="$1;}' > /root/files/black.txt
maxlimit="20"
for i in `cat /root/files/black.txt`
do
ip=`echo $i|awk -F= '{print $1}'`
num=`echo $i|awk -F= '{print $2}'`
if [ $num -gt $maxlimit ];
then
grep $IP /etc/hosts.deny > /dev/null 
if [ $? -gt 0 ];
then
echo "sshd:$IP" >> /etc/hosts.deny 
fi 
fi 
done
