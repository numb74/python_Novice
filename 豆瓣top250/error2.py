import time
from lxml import etree
import requests
import fake_user_agent
import R_proxy

l = R_proxy.get_proxy_list2()

def judge_ip(pro):
    try:
        headers = {"User-Agent": fake_user_agent.user_agent()}
        req = requests.get("https://ip.hao86.com/", headers=headers, proxies=pro,verify=False)
        res = req.text
        html = etree.HTML(res)
        ip = html.xpath("//div[@class='ip_table_mess']//tr[1]/td[2]/text()")
        print(ip[0])
        return 1
    except Exception as e:
        print(f"错误信息为:{e}")
        return 0
proxy_list = []

for i in range(15):
    proxies = { 'http':'http://{}'.format(l[i]),
        'https':'http://{}'.format(l[i])}
    if judge_ip(proxies) ==1:
        proxy_list.append(proxies)


print(proxy_list)