import time
import urllib.request
from lxml import etree
import re
import fake_user_agent
import pandas as pd


movie_name = []
movie_country = []
movie_time = []
l = []


#获取url列表并命名为douban_url
def getallurl():
    global l
    for i in range(10):
        url = "https://movie.douban.com/top250?start=" + "{}".format(i * 25) + "&filter="
        l.append(url)

#获取电影名和上映时间以及国家
def getResource(url):

    time.sleep(1)
    global movie_name,movie_time,movie_country

    #伪装浏览器访问
    opener = urllib.request.build_opener()
    headers = {"User-Agent":fake_user_agent.user_agent()}
    req = urllib.request.Request(url=url,headers=headers)
    res = opener.open(req)
    res = res.read().decode('utf-8')

    #资源爬取
    req = etree.HTML(res)
    a = movie_name
    movie_name = req.xpath("//ol[@class='grid_view']//li//div[@class='hd']/a/span[1]/text()")
    a = a+movie_name
    movie_name = a
    movie_time_list = req.xpath("//ol[@class='grid_view']//li//div[@class='bd']/p/text()")
    for i in range(25):
        t = movie_time_list[4*i+1]
        pattern = re.compile('(?<=(/)).*?(?=(/))')
        str = u'{}'.format(t)
        country = pattern.search(str).group()
        country = re.findall("[\u4e00-\u9fa5]", country)
        movie_country_ = "".join(country)
        movie_country.append(movie_country_)
    for i in range(25):
        e = movie_time_list[4* i + 1]
        estr = re.findall("[0-9]", e)
        movie_time_str = "".join(estr)
        movie_time.append(movie_time_str)
getallurl()
for i in range(5):
    getResource(l[i])
numb = [i for i in range(1,126)]
dict = {"电影名":movie_name,"上映时间":movie_time,"制作者":movie_country}
df = pd.DataFrame(dict,index=numb)
df.to_csv("douban_125.csv",encoding="gbk")