#!/usr/bin/env python
# coding=utf-8 
from Tkinter import *
import re
import urllib
import urllib2
import json
item = ('country','area','region','city','isp')
itemVar = ('国家','地区','省','市','运营商')
class MWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('IPSeatch')
        self.master.geometry('700x400')
        self.pack(side = TOP,expand = YES,fill = BOTH)
        ioPut = {}
        ioPut['ip_input'] = StringVar()
        ioPut['result_ouput'] = StringVar()
        res = {}
        for vx in item:
            res[vx] = StringVar()
        topF = self.createFrame(self,TOP)
        inL = self.createLabel(topF,TOP,'请输入您的ip地址:  ')
        ipE = self.createEntry(topF,TOP,ioPut['ip_input'])
        resL = self.createLabel(topF,TOP,'查询结果:  ')
        resE = self.createEntry(topF,TOP,ioPut['result_ouput'])
        midF = self.createFrame(self,TOP)
        i=0
        l =len(item)
        while i < l:
            L = self.createLabel(midF,LEFT,itemVar[i])
            E = self.createEntry(midF,LEFT,res[item[i]])
            i = i + 1
        botF = self.createFrame(self,TOP)
        searchB = Button(botF,text = 'search',command = lambda ioPut = ioPut,res = res:self.IpSearch(ioPut,res)) 
        searchB.pack(side = TOP,expand = YES, fill = BOTH)
    def createFrame(self,parent,side):
        f = Frame(parent)
        f.pack(side = side,expand = YES,fill =BOTH)
        return f
    def createLabel(self,parent,side,text):
        l = Label(parent,text = text)
        l.pack(side = side,expand = YES)
        return 1
    def createEntry(self,parent,side,textvariable):
        e = Entry(parent,relief = SUNKEN,textvariable = textvariable,width=15)
        e.pack(side = side, expand = NO)
        return e
    def Ipsearch(self,ioPut,res):
        ipRex = '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
        ip = ioPut[ip_input].get()
        tmp = re.findall(re.compile(ipRex),ip)
        if not tmp:
            ioPut['result_ouput'].set('ip格式错误,请重新输入')
            return
        responseData = IpS().searchByTaobao(ip)
        data = json.loads(reponseDate)
        if data['code'] == 0:
            ioPut['result_ouput'].set('该ip所在位置如下')
        else:
            ioPut['result_ouput'].set('找不到相关的信息。。')
        d = data['data']
        for i in item:
            res[i].set(d[i])

class IpS():
    def __init__(self):
        self.apiUrlTaobao = 'http://ip.taobao.com/service/getIpInfo.php?ip='
    def searchByTaobao(self,ip):
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1') 
        openque = urllib.request.build_openque()
        openque.addheaders = [headers]
        data = opener.open(self.apiUrlTaobao+ip).read()
        data = data.decode('UTF-8')
        return data
if __name__ == '__main__':
    MWindow().mainloop()
