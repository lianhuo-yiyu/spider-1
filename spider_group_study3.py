# Python 学习 1
# 2021/3/20 15:06
# 准备参数


# 进行百度翻译
# import requests
#
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

# 正则表达式 正则表达式的使用 re模块     分别有findall（返回值为list）、finditer
# 返回值是一个迭代器，也就是一个循环体，要得出相应的值必须要for循环得出print(www.group()）、search(会进⾏匹配.
# 但是如果匹配到了第⼀个结果. 就会返回这个结果. 如果匹配不上search返回的则是None)
# match 只能从字符串的开头进⾏匹配、compile() 可以将⼀个⻓⻓的正则进⾏预加载. ⽅便后⾯的使⽤
#  . 匹配除换⾏符以外的任意字符
# \w 匹配字⺟或数字或下划线
# \s 匹配任意的空⽩符
# \d 匹配数字
# 量词: 控制前⾯的元字符出现的次数
# 贪婪匹配和惰性匹配
# \n 匹配⼀个换⾏符
# \t 匹配⼀个制表符
# ^ 匹配字符串的开始
# $ 匹配字符串的结尾
# \W 匹配⾮字⺟或数字或下划线
# \D 匹配⾮数字
# \S 匹配⾮空⽩符
# a|b 匹配字符a或字符b
#  () 匹配括号内的表达式，也表示⼀个组
# [...] 匹配字符组中的字符
#  [^...] 匹配除了字符组中字符的所有字符
#
#
# * 重复零次或更多次
# + 重复⼀次或更多次
# ? 重复零次或⼀次
# {n} 重复n次
#  {n,} 重复n次或更多次
# {n,m} 重复n到m次
#
#  .* 贪婪匹配
# .*? 惰性匹配

# 小说排名的抓取           obj = re.compile
# import re
# import requests
# url = "http://chuangshi.qq.com/bang/rq/xh-week.html"
# header = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# res = requests.get(url=url)
# s = res.text
# print(s)
# obj = re.compile(r"<a target='_blank' href='http://chuangshi.qq.com/bk/xh/\d+.html'>(?P<xiaoshuo>.*?)</a>", re.S)
# result = obj.finditer(s)
# for i in result:
#     print(i.group("xiaoshuo"))

#
# import re                                                                        obj = re.findall(
# import requests
# url = "http://chuangshi.qq.com/bang/rq/xh-week.html"
# header = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# res = requests.get(url=url)
# s = res.text
# obj = re.findall(r"<a target='_blank' href='http://chuangshi.qq.com/bk/xh/\d+.html'>(?P<xiaoshuo>.*?)</a>", s )
# print(obj)              #输出结果为列表

#
# import re
# import requests
# url = "http://chuangshi.qq.com/bang/rq/xh-week.html"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
#     /537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# res = requests.get(url=url)
# s = res.text
# obj = re.findall(r"<a target='_blank' href='http://chuangshi.qq.com/bk/xh/\d+.html'>(?P<xiaoshuo>.*?)</a>", s)
# for i in obj:
#     print(i)


# 豆瓣实验
import re
import requests
import csv
url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         "Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url=url, headers=headers)
s = res.text
print(s)
# obj = re.finditer('<span class="title">(?P<movie>.*?)</span>', s)
obj = re.finditer(r'<span class="title">(?P<movie>.*?)</span>', s)
# obj = re.finditer(r'<span class="title">(?P<movie>.*?)</span>\n.*?<span class=',s)  # 搜出来两个就是因为正则太短，条件匹配的不止这一条
for i in obj:
    print(i.group("movie"))
res.close()

