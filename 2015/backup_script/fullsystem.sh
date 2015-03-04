#!/bin/bash
TODAY=`/bin/date +%Y%m%d-%H` 
NAME=`date +%Y-%m-%d`
FILENAME="fullbackup-${TODAY}-${NAME}"

tar -jcvpf /backups_junqueh/${FILENAME}.tar.gz2  --directory=/ --exclude=proc --exclude=sys --exclude=dev/pts --exclude=backups_junqueh  --exclude=proc --exclude=selinux .

echo
echo "Backup finished"
date 


exit 0
