# -*- coding:utf-8 -*-
__author__ = "fank-cd"

#这个是用来爬http://www.kanmeizi.cn这个网站的，首页有不同的帖子，点进去是妹子图片，存在D盘meizi文件下，注意，如果事先存在文件，则会报错


import urllib
import urllib2
import re
import thread
import time
import os
import timeit


class MMM:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0)'
        self.headers = {'User-Agent' :self.user_agent}
        self.items=[]
        self.count=0
        self.i=0

    def getPage(self,pageIndex):
        try:
            url = "http://www.kanmeizi.cn/index_%s_16.html" %str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            print url
            #print pageCode
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "error",e.reason
                return None

    def getPage2(self,i):
       #i=int(i)
        print "downing:",self.items[i]

        try:
            url = self.items[i]
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            #print pageCode
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "error",e.reason
                return None

    def geturl(self,pageIndex):
        if not self.i==0:
            self.items=[]
            print "haha"
        self.i+=1
        pagecode=self.getPage(pageIndex)
        pattern = re.compile('<span class="fl p5".*?href="(.*?)"',re.S)
        items =re.findall(pattern,pagecode)
        for item in items:
            self.items.append("http://www.kanmeizi.cn"+item)
        print len(self.items)


    def getitems(self,i):
        pagecode=self.getPage2(i)
        #print pagecode
        pattern = re.compile('<div class="thumbnail"><img.*?"(.*?)"',re.S)
        Imgurl = re.findall(pattern,pagecode)
        #print title

        path = "D:\\meizi\\%d\\"%self.count
        os.makedirs(path)
        self.count+=1
        x=0
        for imgurl in Imgurl:
            #print "imgurl"+"***%d"%(imgurl,x)
            try:
                urllib.urlretrieve(imgurl,path+"%d.jpg"%x)
                x+=1
            except urllib.ContentTooShortError:
                print "netwrok is not good"
                urllib.urlretrieve(imgurl, path + "%d.jpg" % x)
            #print timeit.timeit('urllib.urlretrieve(imgurl,path+"1.jpg")')




mmm=MMM()
#mmm.geturl(1)
#mmm.getitems(1)

for i1 in range(100):
    mmm.geturl(i1)
    for i2 in range(15):
        mmm.getitems(i2)
