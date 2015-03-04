__author__ = 'junqueh'
#coding:uff-8

import smtplib

def sendMail(mail_to):
    mail_server = 'smtp.163.com'
    mail_port = '25'
    username = '260037121@163.com'
    password = 'xxxxxxxxx'
    mail_title = 'python test'
    mail_content = 'This is a test from python for sending email'
    if type(mail_to) == str:
        mail_list = mail_to.split(';')
    elif type(mail_to) == list:
        mail_list = mail_to
    else:
        print "你输入的收件人格式有误"

    try:
        handle = smtplib.SMTP(mail_server,mail_port)
        handle.login(username,password)
        msg = "From:%s\r\n To:%s\r\nContent-Type: text/html;"charset=gb2312\r\nSubject:%s\r\n\r\n %s"%("张3",";".join(mail_list),mail_title,mail_content)
        handle.sendmail(username,mail_list,msg)
        print "Send email success"
    except Exception,e:
        print "Send email failed because %s" % e

    if __name__ == "__main__":
        sendMail('junqueh@gmail.com')