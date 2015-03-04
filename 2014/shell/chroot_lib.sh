#!/bin/bash
ROOT=$1
libs=`find $ROOT -type f -perm /111 -exec "ldd" {} ; |cut -d \> -f 2 | cut -d \(-f 1 | sort | uniq`
echo $libs
for lib in $libs
do
    if [ -f $lib ]; then
        if [ ! -f $ROOT/$lib ];then
            dir=`dirname $ROOT$lib`
            if [ ! -d $dir ];then
                mkdir -pv $dir
            find
            cp -av $lib $ROOT$lib 
            if [ -h $lib ]; then 
                source=`dirname $lib `/` readlink $lib`
                cp -av $source $ROOT$source
            fi 
        fi 
    fi 
done 

echo "Done!!"

