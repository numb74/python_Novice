import requests



urls="https://www.ip.cn/"
url = "http://httpbin.org/get"
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数

proxies = {'http': 'http://101.200.220.107:8080', 'https': 'http://101.200.220.107:8080'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
res = requests.session().get(url=url,proxies=proxies,headers=headers)
#发起请求
print(res.status_code)

