# Python 学习 1
# 2021/3/29 21:06
from lxml import etree
import re
import requests
import time
from concurrent.futures import ThreadPoolExecutor


def img_onepage(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url=url, headers=headers)
    res.encoding = "utf-8"
    tree = etree.HTML(res.text)
    result = tree.xpath("/html/body/div[2]/div[8]/ul/*/a/img/@src")
    print(result)
    for item in result:
        img = requests.get(item)
        path = r"D:\pycharm\workspace\spider study\more xpath/" + item.split("/")[-1]
        with open(path, mode="wb") as f:
            f.write(img.content)
            print("over" + path)
    print("over one page")
    time.sleep(0.5)
    res.close()


if __name__ == '__main__':
    # for i in range(1,132):
    #     url = f"https://www.umei.cc/weimeitupian/yijingtupian/{i}.htm"
    #      img_onepage(url)
    with ThreadPoolExecutor(50) as f:
        for i in range(1,132):
            url = f"https://www.umei.cc/weimeitupian/yijingtupian/{i}.htm"
            f.submit(img_onepage(url))
    print("结束")
    time = time.time()
    print(time)
    