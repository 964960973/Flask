import requests
from bs4 import BeautifulSoup
import time
import threading
import queue
class Mythreading(threading.Thread):
    def __init__(self,q,name):
        threading.Thread.__init__(self)
        self.q = q
        self.name=name
    def run(self):#这个run方法在进程创建后会自动运行这个程序
        # print("starting"+self.name)
        # print(self.q.qsize())
        # print(self.q.empty())
        while not self.q.empty():
            crawler_run(self.q,self.name)
        print("exiting...")
def crawler_run(q,name):
    num = q.get(timeout=2)
    soup = connec_douban(num)
    #print("run-run")
    titles = soup.findAll("div",class_="item")#.find("span",class_="title").text
    for title in titles:
        print(name,q.qsize(),title.find("span",class_="title").text+"\n")
def connec_douban(num1):
    link="https://movie.douban.com/top250?start="+str(num1)+"&filter="
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    re = requests.get(link,headers=headers)
    soup = BeautifulSoup(re.text,"lxml")
   # print("url-status",re.status_code,end="\n")
    return soup

if __name__=='__main__':
    threadset=[]
    start = time.time()
    q = queue.Queue(14)
    for i in range(0,326,25):
        q.put(i)
    ThreadNames=["process1","process2","process3","process4"]
    for i in range(0,4):
        p = Mythreading(q,ThreadNames[i])
        p.start()
        threadset.append(p)
    for thread in threadset:
        thread.join()
    end = time.time()
    print("总时间:",end-start)
