#!/bin/bash
#auto bakcup mysql 
#date 2014.12.12
#author junqueh
HOST="localhost"
USER="root"
PASSWD=""
BACKUPDIR='/opt/backup'
############

DATE=`date +%Y%m%d`
M=`date +Y%m`

function createdir()
{
while [ ! -d $BACKUPDIR ]; do
    echo "BAKCUPDIR is not exits, please create now "
    mkdir -pv $BACKUPDIR
done
cd $BACKUPDIR
while [ ! -d "$DATE" ]; do
    mkdir -pv $DATE
done
while [ ! -d "$M" ]; do
    mkdir $M
done
}

function showdatabase()
{
mysql -h $HOST -u$USER -p$PASSWD -e 'show databases;' |grep -v 'Database'|grep -v 'information_schema' > /tmp/mysqldblist
}

function backup()
{
while read LINE
do
    mysqldump -h $HOST -u$USER -p$PASSWD --all-database > $DATE/all$DATE.sql
done < /tmp/mysqldblist
tar cvfj $DATE.tar.gz $DATE
rm -rf $DATE
mv $DATE.tar.gz $M/
}

createdir && showdatabase && backup  
