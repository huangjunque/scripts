#!/bin/bash
#-------script--------------
#   Name:gtx_init.sh
#   Date:2014-05-22
#   Author:syd_python

Date=`date +%Y%m%d%H`
Log="/var/log/gtx_init.sh.$Date"


#rootpasswd
read -p "Please enter the root init password:" op
echo "$op" > $Log
echo "op" | passwd --stdin root >> $Log

#sshport
sed -i 's/#Port 22/Port 1101/' /etc/ssh/sshd_config
/etc/init.d/sshd restart >> $Log

#iptablesconfig
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
iptables -A INPUT -p tcp  --dport 3306 -j ACCEPT
iptables -A INPUT -p tcp -m state --state NEW --dport 1101 ACCEPT
iptables-save > /etc/iptables.up.rules

echo "/sbin/iptables-restore < /etc/iptables.up.rules" >> /etc/rc.local
