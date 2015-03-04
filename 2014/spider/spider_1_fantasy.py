#!/usr/bin/env python
# coding=utf-8

import string
import urllib2
import urllib2
import re
from threading import Thread 
from Queue import Queue
from time import sleep
import os
import sys
#Q is task queue
Q = Queue()
thread_num = 7

class HTML_Tool:
#----Deal with all kinds of labels on the page----
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    EndCharToNoneRex = re.compile("<.*?")
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  

## 将一些html的符号实体转变为原始符号  
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," "),(""","\"")]  ")]

    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("",x)
        x = self.BgnPartRex.sub("\n  ",x)
        x = self.CharToNewLineRex.sub("\n",x)
        x = self.CharToNextTabRex.sub("\t",x)
        x = self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:
            x = x.replace(t[0],t[1])
        return x
#---------- 处理页面上的各种标签 -------------

class MM_Spider:
    # 构造函数
    def __init__(self,url):
        self.myUrl = url
        self.urlNum = 0
        self.myTool = HTML_Tool()
        print u'MM spider start........'

#header伪装获得html内容
    def get_html(self,url):
        req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req_timeout = 30
        try:
            req = urllib2.Request(url,None,req_header)
            page = urllib.urlopen(req,None,req_timeout)
            html = page.read().decode("utf-8")
        except urllib2.URLError as e:
            print e.message
        except socket.timeout as e:
            user_html(self.myUrl)
        return html

#每个线程去抓一个人的图,简介等，要自己组织文件目录
    def working(self):
        while True:
            url=Q.get()
            self.get_MM_pic(url)
#sleep(1)
            Q.task_done()

    def get_MM_pic(self,url):
        personal_page =self.get_html(url)
        title=re.search(r'<title>([^ |]*)',personal_page,re.S)
        print title.group(1)
        os.mkdir(title.group(1))
        profile=re.search(r'<div class="column grid_12" style="margin-bottom: 10px">([^<]*)',personal_page,re.S)  

        f = open(title.group(1)+'/'+title.group(1)+'简介'+'.txt',+'w+')
        if profile==None:
            f.writelines("no profile")
        else:
            f.writelines(self.myTool.Replace_Char(profile.group(1)))
        f.close()
        album=re.findall(r'<a href=\'([^\']*)\' class="caption">',personal_page,re.S)  
        count=0
        for item in album:
            print item
            count=self.save_MM_page(item,title.group(1),count)

    def save_MM_page(self,url,catalog,count):
        photos_page=self.get_html(url)
        photos=re.findall(r"<img title=.*?delay='(.*?)' />",photos_page,re.S) 
        for item in photos:
            urllib.urlretrieve(item,catalog+ '/' +'%d.jpg' %count)
            count +=1
        return count
#main()
    def MM_pic(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        os.chdir('pics')
        for i in range(thread_num):
            t=Thread(target=self.working)
            t.setDaemon(True)
            t.start()
        myPage=self.get_html(self.myUrl)
        myItems=re.findall(r'<li title=.*?<a target="_blank" href=\"([^\"]*)\"',myPage,re.S)
        for item in myItems:
            Q.put(item)
            self.urlNum+=1
            print item
        print self.urlNum

print u'按任意键开始抓取......'
raw_input()
url='http://gril-atlas.com/'
mySpider=MM_Spider(url)
mySpider.MM_pic()

Q.join()
print "xxxxoo mm"
'''
xx
'''
