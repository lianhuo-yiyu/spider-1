# url介绍   ？前面是URL，？后面是参数，也就是param部分。 urllib库中urlopen.request   urllib.request.urlopen(url, data=None,[timeout,]*,
# cafile=None,capath=None,cadefault=False,context=None) url:访问的网址 data:额外的数据，如header，form data
# GET方法请求网页，对网页进行request，将获取到信息打印出来  GET请求将请求的参数都放在URL后面 GET可以直接输入URL访问 import urllib.request with
# urllib.request.urlopen("http://www.python.org/") as f: print(f.read(300))

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))


# POST方法请求网页,获取数据   Post请求中网页的源代码处有一个FORM data，post 要构建一个表单，进行表单提交才可以进行请求到数据（理解是必须发送一个存在在请求里的键值对才能够获取到数据）
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://www.baidu.com', data=data)
print(response.read())


'''
#timeout超时设置
import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)
print(response.read())
'''

''''''''''''''''
#获得状态码和响应头
# 响应类型
import urllib
import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(type(response))
# 状态码， 响应头
print(response.status)#获取状态码 status
print(response.getheaders())#获取响应头
print(response.getheader('Connection'))#获取特定响应头部分
'''''''''''''''
