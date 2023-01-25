import requests
import fake_user_agent
from lxml import etree


#获取代理的地址1
def get_proxy_list():
    req = requests.get("http://proxydb.net/?protocol=https&anonlvl=4&country=CN",headers={"User-Agent": fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    ip = html.xpath("//div[@class='table-responsive']//tr//td[1]//a/text()")
    print(ip)
    return ip
# ip = get_proxy_list()
# print(ip)
#获取代理的地址2
def get_proxy_list2():
    req = requests.get("https://proxy.seofangfa.com/",headers={"User-Agent": fake_user_agent.user_agent()})
    html = etree.HTML(req.text)
    ipx = html.xpath("//div[@class='table-responsive']//tbody//tr/td[1]/text()")
    ipy = html.xpath("//div[@class='table-responsive']//tbody//tr/td[2]/text()")
    l = dict(zip(ipx,ipy))
    ip = []
    for k in l:
        t = '{}:{}'.format(k,l[k])
        ip.append(t)
    print(ip)
    return ip



#判断单个ip是否有效
def judge_ip(pro):
    try:
        headers = {"User-Agent": fake_user_agent.user_agent()}
        req = requests.get("https://ip.hao86.com/", headers=headers, proxies=pro,verify=False,timeout=3)
        res = req.text
        html = etree.HTML(res)
        ip = html.xpath("//div[@class='ip_table_mess']//tr[1]/td[2]/text()")
        print(ip[0])
        return 1
    except Exception as e:
        print(f"错误信息为:{e}")
        return 0


l = get_proxy_list2()
for i in range(10):
    proxies = { 'http':'{}'.format(l[i]),
        'https':'{}'.format(l[i])}
    judge_ip(pro=proxies)