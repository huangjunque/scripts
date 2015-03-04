#!/usr/local/env python
#time 2014-11-12
'''should be installed python-psutil'''
import os, sys, subprocess, psutil,smtplib, datetime, time
from time import gmtime, strftime

#email configure
from_addr = 'junqueh@gmail.com'
to_addr_list = 'junqueh@gmail.com'
cc_addr_list = 'junqueh@gmail.com'
subject='test_subjuct'

tr(time_in_log())+"\t CPU usage per core = "+str(output)+"\n"logini'junqueh'
password='que900821'
smtpserver='smtp.gmail.com:587'

#configs
frequency=30
host = 'www.sina.com.cn'
timeformat='%m%d %H:%M:%S'
cpu_threshold=80
memory_threshold=10
swap_threshold=40
disk_threshold=50
#disk='/'
LogStorage='/var/log/monitor.log'


#---------code-------------
e_message=[]
def time_in_log():
    return strftime(timefortmat,gmtime())
def mtr():
    output=subprocess.call('mtr' + host + '-c 4 -r'
        shell=True,
        stdout=open(LogStorage, 'a')
        stderr=subprocess.STDOUT)

def w():
    output=subprocess.call('w',
        shell=True,
        stdout=open(LogStorage, 'a'),
        stderr=subprocess.STDOUT)

def ping():
    output = subprocess.call('ping' + host + ' -c 3 | grep "time\|rtt"',
        shell=True,
        stdout=open(LogStorage,'a'),
        stderr=subprocess.STDOUT)
    if output==0:
        e_message.append("No ping")

def cpu_total():
    output=psutil.cpu_percent(interval=3)
    f=open(LogStorage,'a')
    f.write(str(time_in_log())+"\t CPU usage per core = "+str(output)+"\n")
    for i in range(len(output)):
        if output[i] > float(cpu_threshold):
            cpu_per_core_message="CPU"+str(i)+" usage is critical="+str(output[i])
            e_message.append(cpu_per_core_message)
def memory():
    output=psutil.virtual_memory()[2]
    f=open(LogStorage, 'a')
    f.write(str(time_in_log())+"\t Memort usage + "+str(output)+"\n")
    if output>memory_threshold:
        memory_message="Memory usage is critical="+str(output) + "%"
        e_message.append(swap_message)

def sendmail_client(from_addr,to_addr_list, cc_addr_list,
                    subject,mssage,login,password,smtpserver):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def exact_mail():
   sendemail_client(from_addr, to_addr_list, cc_addr_list,subject,e_message,login, password,smtpserver) 

while True:
    e_message=[]
    df()
    w()
    cpu_per_core()
    cpu_total()
    memory()
    swap()
    disk()
    ping()
    mtr()

    exact_mail() #- Sending email
    time.sleep(frequency)

