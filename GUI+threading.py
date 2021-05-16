# Python 学习 1  https://www.umei.cc/katongdongman/dongmantupian/160.htm
# 2021/4/1 11:02
import re
import sys
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from PyQt5.Qt import *
from login import Ui_MainWindow


def spider_onepage(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                      "87.0.4280.88 Safari/537.36"
              }
    res = requests.get(url=url,headers=headers)
    tree = etree.HTML(res.text)
    result = tree.xpath("/html/body/div[2]/div[8]/ul/*/a/img/@src")
    for i in result:
        path = r"D:\pycharm\workspace\spider study\GUI+Spider/" + i.split("/")[-1]
        with open(path, mode="wb") as f:
            img =requests.get(url=i,headers=headers)
            f.write(img.content)
            print("over" + i)
    print("over one page")
    pattern = r'\d+.htm'
    with ThreadPoolExecutor(50) as f:
        for i in range(1, 200):
            url = re.sub(pattern, f'{i}.htm', url)
            print(url)
            f.submit(spider_onepage(url))
            time = time.time()
            print(time)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display)
    def display(self):
        url = self.user_lineEdit.text()
        print(url)
        spider_onepage(url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())