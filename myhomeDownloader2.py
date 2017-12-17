#-*- coding:utf-8 -*-

#实现了通过selenium 爬取网站所有的信息
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import  re
def pageNum(number):
        print number.text
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#开始执行seleum

if __name__=='__main__':
    Url = 'http://example.com/Netweb_List/Netweb_Home_Lose_List.html'

    driver=webdriver.Firefox()
    driver.set_window_position(x=50,y=60)
    driver.set_window_size(width=1366,height=700)
    driver.get(url=Url)
    number = driver.find_element_by_css_selector(
        '#Netweb_Home_Lose_ListCtrl1_pager1 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > '
        'td:nth-child(1)')
    all_num=int(number.text[14:17]) #获取总页数
    f=open('link.txt','w')
    #下面抓取所有丢失物品链接，保存在文件中
    for i in range(1,all_num):
        #下面进行页面的点击提交
        nextSelecter=driver.find_element_by_id('Netweb_Home_Lose_ListCtrl1$pager1_input')
        nextSelecter.clear()
        nextSelecter.send_keys(str(i))
        nextSelecter2=driver.find_element_by_id('Netweb_Home_Lose_ListCtrl1$pager1_btn')
        nextSelecter2.click()
        href=driver.find_element_by_css_selector('.myTable > tbody:nth-child(1)')
        href2=href.find_elements_by_css_selector('tr td:nth-child(1) a')
        #根据获取到的个人信息链接
        for i in href2:
            f.write(i.get_attribute('href')+'\n')    #将链接写入文件

    link=[] #所有的个人丢失物品的链接
    for i in range(len(link)):
        driver.get(link[i])
        Ele = driver.find_element_by_css_selector('.content1 > tbody:nth-child(1)')
        str2=str(Ele.text).replace('\n','').replace(' ','') #解析到的所有信息
        #print str2
        p = re.compile('联系方式：(\w*)')
        mat = p.findall(str2) #匹配联系方式
        if len(mat)>0:
            print mat[0]
    driver.close()  #关闭浏览器
