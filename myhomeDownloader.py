#-*- coding:utf-8 -*-
# python 2.7
import requests
import os,chardet
from time import sleep
import re
from bs4 import  BeautifulSoup
print "我们的家园下载器"
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    import cookielib
except:
    import http.cookiejar as cookielib

session=requests.session()
session.cookies=cookielib.LWPCookieJar(filename='cookies')

try:
    session.cookies.load(ignore_discard=True)
except:
    print 'cookie未能加载！'
##备注：此程序只适用于测试，并未对外泄露任何学校方面的信息，也为对学校的服务器造成压力
##开发者：SeaFish

heades={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host':'myhome.tsinghua.edu.cn',
    'Referer':'http://myhome.tsinghua.edu.cn/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=jdmfslzfiraczya43d0bzvft; UM_distinctid=1605dbe944c108-022c92d31e70558-17357940-100200-1605dbe944d201; CNZZDATA3006115=cnzz_eid%3D5073117-1513396874-http%253A%252F%252Fmyhome.tsinghua.edu.cn%252F%26ntime%3D1513396874'
}
def getHtml(url):
    req=requests.get(url,headers=heades)
    return BeautifulSoup(req.content,'html.parser')

if __name__=="__main__":
    print "开始下载"
    lostUrl='http://myhome.tsinghua.edu.cn/Netweb_List/Netweb_Home_Lose_List.html'
    parms={
        '__EVENTARGUMENT': 3,
        '__EVENTTARGET': 'Netweb_Home_Lose_ListCtrl1$pager1',
        #'__VIEWSTATE':'/wEPDwULLTE4MTI1NTI0OTAPZBYCAgMPZBYIAgMPZBYCAgIPFgIeB1Zpc2libGVoZAIFD2QWAmYPFgIeC18hSXRlbUNvdW50AgwWGAIBD2QWAmYPFQVEaHR0cDovL215aG9tZS50c2luZ2h1YS5lZHUuY24vbmV0d2ViX2J1aWxkaW5nL0J1aWxkaW5nQWR2aWNlQWRkLmFzcHgM5oiR5om+5qW86ZW/RGh0dHA6Ly9teWhvbWUudHNpbmdodWEuZWR1LmNuL21hbmFnZS8vSW1hZ2UvdGFiMS9tXzEyNjMwMjI3MTI2MTgucG5nRGh0dHA6Ly9teWhvbWUudHNpbmdodWEuZWR1LmNuL25ldHdlYl9idWlsZGluZy9CdWlsZGluZ0FkdmljZUFkZC5hc3B4DOaIkeaJvualvOmVv2QCAg9kFgJmDxUFLC9OZXR3ZWJfTGlzdC9uZXR3ZWJfcmVwYWlyc3JlY29yZF9Nb250aC5hc3B4DOe9keS4iuaK…2NvbG9yOnJlZCc+5pyq5b2S6L+YPC9zcGFuPmRkAhQPZBYKZg8VBBhOZXR3ZWJfSG9tZV9Mb3NlX0RldGFpbF8EODMzNwnpkqXljJnkuLIJ6ZKl5YyZ5LiyZAIBDw8WBB8UBQoyMDE3LTExLTA3HxUFETIwMTctMTEtNyAwOjAwOjAwZGQCAw8PFgQfFAUS5ou+5Yiw6ZKl5YyZ5LiA5LiyHxUFEuaLvuWIsOmSpeWMmeS4gOS4smRkAgUPDxYEHxQFC3FxNzgzNDIxNjA3HxUFC3FxNzgzNDIxNjA3ZGQCBw8PFgIfFAUoPHNwYW4gc3R5bGU9J2NvbG9yOnJlZCc+5pyq5b2S6L+YPC9zcGFuPmRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBSBuZXRfRGVmYXVsdF9Mb2dpbkN0cmwxJGxidG5Mb2dpbgUibmV0X0RlZmF1bHRfTG9naW5DdHJsMSRsYnRuU2VhcmNoMQ==',
        #'net_Default_LoginCtrl1$txtSearch1':'',
        #'net_Default_LoginCtrl1$txtUserName':'',
        #'net_Default_LoginCtrl1$txtUserPwd':'',
        #'Netweb_Home_Lose_ListCtrl1$pager1_input':2

    }
    '''
    r1=requests.post(lostUrl,data=parms,headers=heades)
    html = r1.content
    #print(html)
    r2= BeautifulSoup(r1.content,"html.parser")
    for i in r2.find_all(id="Netweb_Home_Lose_ListCtrl1_pager1"):
        print i.td.text
        '''

    file = open('lost_tings.txt', 'a')
    lostSoup=getHtml(lostUrl)
    page_nums=0  #网页总页数
    #找到失物的总个数
    for i in lostSoup.find_all(id="Netweb_Home_Lose_ListCtrl1_pager1"):
        print i.td.text[0:18]
        page_nums=int(i.td.text[14:17])
        file.write(i.td.text+'\n')
        break

    file.write("分别是丢失的物品名、丢失时间、丢失联系方式、丢失的具体描述、丢失的状态\n")
    page_nums=1
    gn=0

    while(page_nums>0):
        page_nums=page_nums-1
        Url = 'http://myhome.tsinghua.edu.cn/Netweb_List/Netweb_Home_Lose_List.html'
        lostSoup = getHtml(Url)
        #分别是丢失的物品名、丢失时间、丢失联系方式、丢失的具体描述、丢失的状态
        Lname=[]
        Ltime=[]
        Lcon=[]
        Ldetail=[]
        Lstatus = []
        Luser=[]
        for i in lostSoup.find_all('a',attrs={'href':re.compile('Netweb_Home_Lose_Detail')}):#使用正则表达式匹配href
            #print i.text
            Lhref= 'http://myhome.tsinghua.edu.cn/Netweb_List/'+i['href']
            ##获取丢失者的用户名
            Lname.append(i.text)
            lost1=getHtml(Lhref)
            for i in lost1.find_all(id=re.compile('User_Id')):
                Luser.append(i.text)

        for j in lostSoup.find_all(id=re.compile('Lose_Time')):
            Ltime.append(j.text)
            #print j.text
        for j in lostSoup.find_all(id=re.compile('Des_Detail')):
            #print j.text
            Ldetail.append(j.text)
        for j in lostSoup.find_all(id=re.compile('link_way')):
            #print j.text
            Lcon.append(j.text)
            '''
    '''
        for j in lostSoup.find_all(id=re.compile('Is_return')):
            
            #if(str(j.text)=="未归还"):
            #    print '没哟'
            
            Lstatus.append(j.text)
        #写入文件
        for i in range(len(Lname)):
            gn=gn+1
            file.write("No:%d\n     %s\n %      s\n         %s\n        %s\n        %s\n        %s\n"
                       %(gn,Lname[i],Ldetail[i],Ltime[i],Luser[i],Lcon[i],Lstatus[i]))





