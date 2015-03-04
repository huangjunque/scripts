#!/usr/bin/env python
# create by zufallsheld
import os
import shutil
import time
import subprocess

#Functions

def check_dir_exist(os_dir):
    if not os.path.exists(os_dir):
        print os_dir, "does not exist."
        exit(1)

def confirm():
    go = raw_input("Continue? yes/no\n")
    global exit_condition
    if go == "yes":
        exit_condition = 0
        return exit_condition
    elif go == "no":
        exit_condition = 1
        return exit_condition
    else:
        print "Please answer with yes or no."
        confirm()

def delete_files(ending):
    for r, d, f in os.walk(backup_path):
        for files in f:
            if files.endswith("." + ending):
                os.remove(os.path.join(r, files))

#Spefify what and where to backup.
backup_path = raw_input("What shuold be backupd up today?\n")
check_dir_exist(backup_path)
print "Okey", backup_path, "will be saved."
time.sleep(3)

backup_to_path = raw_input("where to backup?\n")
check_dir_exist(backup_to_path)
if not os.path.exists(backup_to_path):
    os.makedirs(backup_to_path)

# Delete files first
print "First, let's cleanup unnecessary files in the backup path."
file_types = ["tmp", "bak", "txt","tar"]
for file_type in file_types:
    print "Delete", file_type, "files???"
    confirm()
    if exit_condition == 0:
        delete_files(file_type)

# Empty trash can
print "Empty trash can?"
confirm()
if exit_condition == 0:
    print "Emptying!"
    shutil.rmtree(os.path.expanduser("~/.local/share"))

# DO the actual backup
print "Doing the backup now!"
confirm()
if exit_condition == 1:
        print "Aborting!"
        exit(1)

#rsync("-auhvz", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc",
 # "--exclude=/mnt", "--exclude=/dev", "--exclude=/backup","--exclude=/etc", backup_path, backup_to_path)
#os.system('rsync -avzhpP --exclude=/lost+found/ --exclude=/sys  {backup_path}  {backup_to_path}' --format.  )         

subprocess.call(['rsync','-avzhPp','--progress','-exclude=/sys' ,backup_path,backup_to_path])
