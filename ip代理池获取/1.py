import time

import requests
from lxml import etree
import fake_user_agent

#获取网址列表
l = []
out = []
def get_all_url():

    for i in range(1,6):
        global l
        url = "https://www.kuaidaili.com/free/inha/{}/".format(i)
        l.append(url)


#爬取某页代理ip资源
def get_ip_resource(url):
    time.sleep(1)
    global out
    headers = {"User-Agent":fake_user_agent.user_agent()}
    r = requests.get(url=url,headers=headers)
    html = etree.HTML(r.text)
    a = html.xpath("//div[@id='list']//td[@data-title='IP']/text()")
    print(a)
    out = out + a
    print(out)


get_all_url()
for i in range(len(l)):
    get_ip_resource(l[i])

str = '\n'
f = open("C:/Users/86137/PycharmProjects/pythonProject/爬虫/ip代理池获取/数据/1.txt","wb")
f.write(str.join(out).encode('gbk'))
f.close()
