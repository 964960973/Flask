import gevent
from gevent.queue import Queue,Empty
from gevent import monkey
monkey.patch_all()#将IO转化为异步执行的函数
import time
from bs4 import BeautifulSoup
import requests

link_list=[]
def crawler_run(index):
    processid = 'process-'+str(index)
    while not workqueue.empty():
        num = workqueue.get(timeout=2)
        soup = connec_douban(num)
        titles = soup.findAll("div",class_="item")#.find("span",class_="title").text
        for title in titles:
            print(processid,workqueue.qsize(),title.find("span",class_="title").text+"\n")
def connec_douban(num1):
    link="https://movie.douban.com/top250?start="+str(num1)+"&filter="
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    re = requests.get(link,headers=headers)
    soup = BeautifulSoup(re.text,"lxml")
    # print("url-status",re.status_code,end="\n")
    return soup
def boss():
    for i in range(0,226,25):
        workqueue.put_nowait(i)

if __name__=='__main__':
    start = time.time()
    workqueue = Queue(10)
    gevent.spawn(boss).join()
    jobs = []
    for i in range(4):
        jobs.append(gevent.spawn(crawler_run,i))
    gevent.joinall(jobs)
    end = time.time()
    print("总时间为",end-start)
