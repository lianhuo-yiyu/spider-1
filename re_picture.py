# Python 学习 1
# 2021/3/21 10:04
''''''''''''''''''''''迅雷电影下载''''''''
import re
import requests
import csv
url = "https://dytt8.net/index.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
res = requests.get(url=url,headers=headers)
res.encoding = "gb2312"
text = res.text
#print(text)
obj = re.compile(r'<a href="/html/gndy/index.html">迅雷电影资源</a>]<a href=\W/html(?P<lianjie>.*?)\W>(?P<movie>.*?)
                                      </a><br/>', re.S)
result = obj.finditer(text)
with open("迅雷电影下载.csv", "w", encoding="utf-8") as csvfile:
    for i in result:
   # print(i.group("movie"),i.group("lianjie"))
         dic = i.groupdict()
         writeCSV = csv.writer(csvfile)
         dic["lianjie"] = url + dic["lianjie"]
         writeCSV.writerow(dic.values())
print("congratulations")
res.close()
'''''''''

# 爬取壁纸 正则爬取
import re
import requests
url = "https://www.umei.cc/bizhitupian/diannaobizhi/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
res = requests.get(url=url,headers = headers)
res.encoding = "utf-8"
s = res.text
print(s)
obj = re.compile(r'<li><a href=.*?<img src="(?P<jpg>.*?)" width=.*?</span></a></li>',re.S)
result = obj.finditer(s)
for i in result:
        geturl = i.group("jpg")
        print(type(geturl))
        image_res = requests.get(geturl)
        print(image_res.content)
        image_name = r"D:\pycharm\workspace\spider study\zhengze/" + geturl.split("/")[-1]                    # 重点 文件路径连接用   /
        with open(image_name, mode="wb") as f:
            f.write(image_res.content)
        print("over ", image_name)
res.close()
''''''''''''''''''''''''''''目前困难是正则爬取到了照片链接后不会下载图片并保存'''
# 解决了问题重点 文件路径连接用   /  注释是三个‘’ ‘’ ‘’
