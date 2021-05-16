# Python 学习 1
# 2021/3/24 21:42

from lxml import etree
import re
import requests
import re
import requests
import csv
url = "https://www.umei.cc/bizhitupian/diannaobizhi/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url=url,headers = headers)
res.encoding = "utf-8"
s = res.text
print(s)
et = etree.HTML(s)
result = et.xpath('/html/body//div[@class = "TypeList_2"]//li/a//img/@src')
print(result)
for item in result:
    print(item)
    img = requests.get(item)
    path = r"D:\pycharm\workspace\spider study\xpath/" + item.split("/")[-1]
    with open(path, mode="wb") as f:
        f.write(img.content)
        print(path + "is over")
print("over")
res.close()
