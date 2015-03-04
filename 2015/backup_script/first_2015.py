#!/usr/bin/env python
# coding=utf-8

import gzip
import subprocess
import os
import datetime

# Directoires to bakcup

dir_to_backup = '/var/www/'

# DBs to backup
db_to_backup = ['Mondial', 'Mondial1']

# DB storage server
db_host = '192.168.50.100'
db_user = 'backup'
db_dir = '/root/backup/db/'

# Files storage server
file_host = '192.168.50.101'
file_user = 'backup'
file_dir = '/root/bakcup/files/'

#MySQL credentials
mysql_user = 'root'
mysql_pass = 'root'
mysql_hostname = 'localhost'
mysql_port = 3306
#Log and alert variables
email_alert = 'junqueh@gmail.com'
log_path = "/home/script/backup.log";
file_path ="/home/script/temp"

#Date use for timestamp the DBs and files backups
date_string = datetime.datetime.now().strftime("%Y-%m-%d")

# Files to upload
db_to_up = []
files_to_up = []

def db_backup(db_name, mysql_user, mysql_pass, mysql_hostname, date_string, file_path):
# Write in log File 
    log.write("Create backup files for db: %s\n" %(db_name))

    cmd = "mysqldump -u%s -p %s -h %s -e --single-transaction -c %s" % (mysql_user, mysql_pass, mysql_hostname, db_name)
    
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    error = process.stderr.read()
    dump_process = process.cummunicate()[0]

#Filename 
file_name = "%s_%s.sql.gz" %(db_name, date_string)

if error != "":
    log.write("Error: %s\n" % error)
else:
    log.write("File %s successfully created\n" % file_name)

#Create the .gz file with the .SQL extracted
gzip_file = gizp.open(file_path + "/" + file_name, "wb")
gzip_file.write(dump_process)
gzip_file.close()

return file_name

def files_backup(dir_backup, date_string, file_path):
    log.write("Create backup files for directory: %s\n" % (dir_backup))

#Create the file tar.gz

    file_name = "files_%s.tar.gz" % date_string
    os.chdir(dir_backup)
    cmd = "tar -czpPf %s/%s ." %(file_path, file_name)
    os.system(cmd)
    log.write("File files_%s.tar.gz successfully created\n" % date_string)

    return file_name

def file_upload(file_name, user, host, directory, file_path):

    log.write("Uploading %s\n" % file_name)

#Move to the files directory
    os.chdir(file_path)

    cmd = "scp -B %s %s@%s:%s/%s" % (file_name, user, host, directory, file_name)
    os.system(cmd)

    log.write("File %s successfully uploaded\n" % file_name)

#script start

log = open(log_path,'a')
log.write(
    "Starting script at %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

# Loop db_to_backup to create backups of DBs
for index, item in enumerate(db_to_backup):
    db_to_up.append(db_backup(item, mysql_user, mysql_pass, mysql_hostname, date_string, file_path))

# Create backup of Files
files_to_up.append(files_backup(dir_to_backup, date_string, file_path))

print

 
# Upload the backups to the servers
#DBs first
for index, item in enumerate(db_to_up):
    file_upload(item, db_user, db_host, db_dir, file_path)

#Files
for index, item in enumerate(files_to_up):
    file_upload(item, file_user, file_host, file_dir, file_path)

##Close Logs
log.write("Ending script at %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
log.close()


