import requests
import fake_user_agent
from lxml import etree
import time
import re
import pandas as pd


requests.adapters.DEFAULT_RETRIES = 5
#获取豆瓣top250所有网址列表,命名为douban_url_list
douban_url_list = []

def get_all_url():
    global douban_url_list
    for i in range(10):
        url = "https://movie.douban.com/top250?start="+"{}".format(25*i)+"&filter="
        douban_url_list.append(url)


#获取豆瓣top250各个影片详情页
douban_url_detail_list = []

def get_detail_url(url):
    time.sleep(0.5)
    global douban_url_detail_list
    req = requests.session().get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    # req = requests.get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    u = html.xpath("//div[@class='hd']/a")
    for i in range(25):
        url = u[i].attrib['href']
        douban_url_detail_list.append(url)

# get_all_url()
# for i in range(10):
#     get_detail_url(douban_url_list[i])




#获取豆瓣top250电影名
top250_movie_name_list = []

def get_all_movie_name(url):
    time.sleep(0.5)
    global top250_movie_name_list
    req = requests.session().get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    # req = requests.get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    top250_movie_name_list5 = html.xpath("//ol[@class='grid_view']//li//div[@class='hd']/a/span[1]/text()")
    top250_movie_name_list = top250_movie_name_list + top250_movie_name_list5
    print(top250_movie_name_list5)


# req = requests.get("https://movie.douban.com/top250",headers={"User-Agent":fake_user_agent.user_agent()})
# html = etree.HTML(req.text)
# movie_name_list = html.xpath("//ol[@class='grid_view']//li//div[@class='hd']/a/span[1]/text()")


#获取豆瓣top250电影上映时间和上映国家以及剧情类别,评分,评价
top250_movie_time_list = []
top250_movie_country_list = []
top250_movie_type_list = []
top250_movie_grade_list = []
top250_movie_appraise_list = []

def get_all_movie_time(url):
    time.sleep(0.5)
    global top250_movie_time_list,top250_movie_country_list,top250_movie_type_list,top250_movie_grade_list,top250_movie_appraise_list
    req = requests.session().get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    # req = requests.get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    top250_movie_time_list_messy = html.xpath("//ol[@class='grid_view']//li//div[@class='bd']/p[1]/text()")
    top250_movie_grade_list5 = html.xpath("//div[@class='star']//span[@class='rating_num']/text()")
    top250_movie_appraise_list5 = html.xpath("//div[@class='star']//span[4]/text()")

    top250_movie_grade_list = top250_movie_grade_list + top250_movie_grade_list5
    top250_movie_appraise_list = top250_movie_appraise_list + top250_movie_appraise_list5

    for i in range(25):
        s = re.findall("\d+", top250_movie_time_list_messy[2*i+1])
        if len(s) > 1:
            top250_movie_time_list.append(s[0])
        else:
            top250_movie_time_list = top250_movie_time_list + s

        s2 = re.findall("/(.*?)/",top250_movie_time_list_messy[2*i+1])
        s22 = re.findall("[\u4e00-\u9fa5]+",s2[0])
        s222 = "".join(s22)
        top250_movie_country_list.append(s222)


        s3 = re.findall("(?<=/).*",top250_movie_time_list_messy[2*i+1])
        s33 = re.findall("(?<=/).*$",s3[0])
        s333 = re.findall("[\u4e00-\u9fa5]",s33[0])
        s3333 = "".join(s333)
        top250_movie_type_list.append(s3333)






# #获取豆瓣top250导演    后面有优化,这个函数不需要了
# top250_movie_director_list = []
#
# def get_all_movie_director(url):
#     time.sleep(0.5)
#     global top250_movie_director_list
#     req = requests.get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
#     html = etree.HTML(req.text)
#     top250_movie_director_list_messy = html.xpath("//ol[@class='grid_view']//li//div[@class='bd']/p[1]/text()")
#     for i in range(25):
#         s = top250_movie_director_list_messy[2*i]
#         t = re.findall("导演:(.*?)主",s)
#         if len(t)!=0:
#             w = re.findall("[\u4e00-\u9fa5]", t[0])
#             out = "".join(w)
#             top250_movie_director_list.append(out)
#         else:
#             top250_movie_director_list.append("该导演全是英文捏")


#获取top250主演和导演
top250_movie_actor_list = []
top250_movie_director_list = []

def get_actor_name(url):
    global top250_movie_actor_list
    global top250_movie_director_list
    req = requests.get(url=url,headers={"User-Agent":fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    u = html.xpath("//span[@class='actor']//span[@class='attrs']/a[1]/text()")#主演
    u2 = html.xpath("//div[@id='info']/span[1]//span[@class='attrs']/a[1]/text()")#导演
    print(u)
    print(u2)
    top250_movie_actor_list = top250_movie_actor_list + u
    top250_movie_director_list = top250_movie_director_list + u2


#获得主演和导演
# get_all_url()
# for i in range(10):
#     get_detail_url(douban_url_list[i])
#
# for i in range(250):
#     get_actor_name(douban_url_detail_list[i])


# top250_movie_name_list                     电影名
# top250_movie_time_list                     电影上映时间
# top250_movie_country_list                  电影制作国家
# top250_movie_type_list                     电影类型
# top250_movie_actor_list                    电影主演
# top250_movie_director_list                 电影导演
# top250_movie_grade_list                    电影评分
# top250_movie_appraise_list                 电影评价人数


get_all_url()
print("我已经获取所有列表,展示如下:")
print(douban_url_list)
# print("准备获取详情页")
# for i in range(10):
#     get_detail_url(douban_url_list[i])
#     print("获取第{}页url完毕".format(i+1))
# print("获取详情页完毕")


print("准备获取所有的电影名称列表")
for i in range(10):
    get_all_movie_name(douban_url_list[i])
    print("获取第{}页电影名列表完毕".format(i+1))
for i in range(10):
    get_all_movie_time(douban_url_list[i])
    print("获取第{}页电影各种信息列表完毕".format(i+1))
# top250_movie_name_list                     电影名
# top250_movie_time_list                     电影上映时间
# top250_movie_country_list                  电影制作国家
# top250_movie_type_list                     电影类型
# top250_movie_grade_list                    电影评分
# top250_movie_appraise_list                 电影评价人数

print(len(top250_movie_name_list))
print(len(top250_movie_time_list))
print(len(top250_movie_country_list))
print(len(top250_movie_type_list))
print(len(top250_movie_grade_list))
print(len(top250_movie_appraise_list))

numb = [i for i in range(1,251)]
dict = {"电影名":top250_movie_name_list,"上映时间":top250_movie_time_list,
        "制作者":top250_movie_country_list,"剧情类型":top250_movie_type_list,
        "评分":top250_movie_grade_list,"评价人数":top250_movie_appraise_list
        }
df = pd.DataFrame(dict,index=numb)
df.to_csv("数据/douban_top250.csv",encoding="gbk")
# for i in range(250):
#     get_actor_name(douban_url_detail_list[i])
#     print("获取第{}页详情页面下的导演和主演完毕".format(i+1))


