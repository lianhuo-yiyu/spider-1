# Python 学习 1
# 2021/3/22 14:54
from bs4 import BeautifulSoup
import re
import requests
import re
import requests
import csv
url = "https://www.umei.cc"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url=url, headers=headers)
res.encoding = "utf-8"
s = res.text
print(s)
obj = BeautifulSoup(s, 'lxml')
result = obj.find_all("div", class_="Pix-box")
print(result)
for i in result:
    print(i)
# '''''''''''问题是在列表中没有匹配到相应的链接并下载保存'''''''''''''''

#
# from lxml import etree
# from bs4 import  BeautifulSoup
# import re
# import requests
# import re
# import requests
# import csv
# url = "https://desk.3gbizhi.com/deskDW/"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# res = requests.get(url=url,headers = headers)
# res.encoding = "utf-8"
# s = res.text
# print(s)
# # obj = BeautifulSoup(s,"html.parser")
# # result = obj.find("div",attrs={"class": "contlistw mtw"})
# # print(type(result))
# # #print(result)
# # geturl = result.find("lazysrc2x")
# # print(geturl)
#
# #xpath一层层提取
# et = etree.HTML(s)
# print(et)
# result = et.xpath(r'/html/body//ul[@class = "cl"]/li/a/img/@lazysrc')#不在前面的也是父子点
# print(result)
# for item in result:
#     imgpath = r"D:\pycharm\workspace\spider study\xpath/" + item.split("/")[-1]
#     with open(imgpath, mode="wb") as f:
#         img = requests.get(item)
#         f.write(img.content)
#         print("over", imgpath)
# res.close()
