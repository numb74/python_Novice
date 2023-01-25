import fake_user_agent
import requests
from lxml import etree
import re


douban_url_list = []
top250_movie_time_list = []
def get_all_movie_time(url):
    global top250_movie_time_list
    req = requests.session().get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    top250_movie_time_list_messy = html.xpath("//ol[@class='grid_view']//li//div[@class='bd']/p[1]/text()")
    print(len(top250_movie_time_list))


def get_all_url():
    global douban_url_list
    for i in range(10):
        url = "https://movie.douban.com/top250?start="+"{}".format(25*i)+"&filter="
        douban_url_list.append(url)
get_all_url()
for i in range(10):
    get_all_movie_time(douban_url_list[i])
