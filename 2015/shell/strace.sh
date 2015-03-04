#!/bin/bash
if [ $# -lt 1 ];then
    echo "usage:$0 process_name"
    exit 1
fi

process_name="$1"

function strace_all()
{
    strace $(pidof "${1}" | sed 's/\([0-9]*\)/-p \1/g')
}

strace $process_name
