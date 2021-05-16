# Python 学习 1
# 2021/3/17 20:35

# import requests
# url = 'https://www.bilibili.com/'
# res = requests.get(url)
# print(res) #验证发送的响应是否成功 获得的是响应头状态码
# #print(res.text)#获取网页的源代码
# print((res.headers))
# print(res.url)
# print(res.cookies)


# 如果访问时被检测为恶意行为，将url.get里面的headers部分加进去，这样就可以瞒过去

# import requests url = 'https://www.bilibili.com/' headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;
# x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


# res = requests.get(url,headers)
# print(res) #验证发送的响应是否成功
# print(res.text)#获取网页的源代码
#
#

# #post请求
# import requests
# url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
# word = input('输入你要查询的单词')
# data = {"w": word}
# res2 = requests.post(url,data=data)
# print(res2)
# print(res2.text)
# print(res2.json())
# print(res2.encoding)
#
#
# import requests
# url = 'https://fanyi.baidu.com/sug'
# s = input('输入你要查询的单词')
# dat = {"kw": s}
# res2 = requests.post(url=url,data=dat)
# print(res2)
# print(type(res2))
# print(res2.text)
# print(type(res2.text))
# print(type(res2.json()))
# print(res2.json())
# print(res2.encoding)
# print('test')
#
# # 准备参数
# kw = input("请输⼊你要翻译的英语单词:")
# dic = {
#  "kw": kw # 这⾥要和抓包⼯具⾥的参数⼀致.
# }
# # 请注意百度翻译的sug这个url. 它是通过post⽅式进⾏提交/
# # 的. 所以我们也要模拟post请求
# resp =requests.post("https://fanyi.baidu.com/sug",
# data=dic)
# # 返回值是json 那就可以直接解析成json
# resp_json = resp.json()
#
# print(resp_json['data'][0]['v']) # 拿到返回字典中的
#
# # 案例3: 抓取⾖瓣电影
# import  requests
# import json
# url = 'https://movie.douban.com/j/chart/top_list'
# param = {
#  'type': '24',
#  'interval_id': '100:90',
#  'action':''
# ,
#  'start': '0',#从库中的第⼏部电影去取
#  'limit': '20',#⼀次取出的个数
# }
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel/Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
# 72.0.3626.121 Safari/537.36'}
# response = requests.get(url=url,params=param,headers=headers)
# list_data = response.json()
# fp = open('./douban.json','w',encoding='utf-8')
# json.dump(list_data,fp=fp,ensure_ascii=False)
# print('over!!!')


#
# #小说排名的抓取,并进行保存
# import re
# import requests
# import csv
# url = "http://chuangshi.qq.com/bang/rq/xh-week.html"
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# res = requests.get(url=url)
# s = res.text
# #print(s)
# obj = re.compile(r"<a target='_blank' href='http://chuangshi.qq.com/bk/xh/\d+.html'>(?P<xiaoshuo>.*?)
# </a>.*?<a class='grey'>(?P<writer>.*?)</a>.*?<a target='_blank' href='(?P<url>.*?).html'>.*?</a>", re.S)
# result = obj.finditer(s)
# with open("小说排行.csv", "w", encoding="utf-8") as csvfile:
#   for i in result:
#         dic = i.groupdict()
#         writeCSV = csv.writer(csvfile)
#         writeCSV.writerow(dic.values())
#     # print(i.group("xiaoshuo"))
#     # print(i.group("writer"))
#     # print(i.group("url"))
#   print("第一页抓取成功并保存了下来")
# res.close()
