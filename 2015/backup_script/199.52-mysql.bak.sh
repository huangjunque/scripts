#!/bin/bash 
# mysql_backup.sh: backup mysql databases and keep newest 5 days backup.
#
# Last updated: 20 March 2006
# ----------------------------------------------------------------------
# This is a free shell script under GNU GPL version 2.0 or above
# Copyright (C) 2006 Sam Tang
# Feedback/comment/suggestions : http://www.real-blog.com/
# ----------------------------------------------------------------------
# your mysql login information
# db_user is mysql username
# db_passwd is mysql password
# db_host is mysql host
# -----------------------------
db_user="skst"
db_passwd='xxoo8855'
db_host='192.168.199.52'
backup_dir="/backups/sos"
#date format for backup file
time=$(date +"%Y-%m-%d.%H.%M")

#mysql
MYSQL="/usr/bin/mysql"
MYSQLDUMP="/usr/bin/mysqldump"
MKDIR="/bin/mkdir"
RM="/bin/rm"
MV="/bin/mv"
GZIP="/bin/gzip"
db="v506"

#check the directory for store backup is writeable
test ! -w $backup_dir && echo  "Error: $backup_dir is  un-writeable."  && exit 0
test ! -d "$backup_dir/backup.0/" && $MKDIR "$backup_dir/backup.0/"
#l99 datebase
$MYSQLDUMP -u $db_user -h $db_host -p$db_passwd --ignore-table=$db.contacts --ignore-table=$db.sos.l99.com $db | $GZIP -9 > "backup_dir/backup.0/$time.$db.gz"

#delete oldest backup
test -d "$backup_dir/backup.5/" && $RM -rf "$backup_dir/backup.5"
# rotate backup directory
for i in 4 3 2 1 0
do
    if(test -d "backup_dir"/backup."$i")
    then
            next=`expr $i +1 `
            MV "$bakcup_dir"/backup."$i" "$backup_dir"/backup."$next"
    fi
done
exit 0;


