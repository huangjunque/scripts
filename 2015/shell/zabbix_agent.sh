#!/bin/bash

if [ -f /etc/zabbix/zabbix_agentd.conf ]
then
        exit
        #mv -fv /etc/zabbix/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf.old
fi

rpm -e zabbix-agent
rpm -e zabbix

n5=`cat /etc/redhat-release |grep 'CentOS release 5'|wc -l`
n6=`cat /etc/redhat-release |grep 'CentOS release 6'|wc -l`

if [ $n5 -eq 1 ]
then
        rpm -ivh http://repo.zabbix.com/zabbix/2.2/rhel/5/x86_64/zabbix-2.2.6-1.el5.x86_64.rpm
        rpm -ivh http://repo.zabbix.com/zabbix/2.2/rhel/5/x86_64/zabbix-agent-2.2.6-1.el5.x86_64.rpm
fi

if [ $n6 -eq 1 ]
then
        rpm -ivh http://repo.zabbix.com/zabbix/2.2/rhel/6/x86_64/zabbix-2.2.6-1.el6.x86_64.rpm
        rpm -ivh http://repo.zabbix.com/zabbix/2.2/rhel/6/x86_64/zabbix-agent-2.2.6-1.el6.x86_64.rpm
fi

sed -ri 's/^(Server.*)=.*/\1=192.168.201.119/;/^Hostname/s/^/#/' /etc/zabbix/zabbix_agentd.conf

echo 'HostMetadataItem=system.uname' >> /etc/zabbix/zabbix_agentd.conf


service zabbix-agent start
chkconfig --level 3 zabbix-agent on
