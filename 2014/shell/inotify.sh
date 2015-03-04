#!/bin/bash  
PATH=/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/bin:/sbinmZexport PATH
host=192.168.1.150
src=/root/download/
dst=root@$host:/root/test_11_backup

#su - rsync
inotifywait -mrq --timefmt '%d%m%y %H:%M' --format '%T %w %f'  -e modify,delete,create,attrib ${src} | while read file
    do
        /usr/bin/rsync  --progress -ahztP  --delete $src $dst && echo -e "\033[32mSync $file is successfully. \033[0m"
        > /tmp/rsync_image.log
     done
    
