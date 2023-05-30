from multiprocessing import Process,Queue,Pool,Manager
import requests
import time
from bs4 import BeautifulSoup

def crawler_run(q,index):
    Process_id='Process--'+str(index)
    while not q.empty():
        num = q.get(timeout=2)
        soup = connec_douban(num)
        titles = soup.findAll("div",class_="item")#.find("span",class_="title").text
        for title in titles:
            print(Process_id,q.qsize(),title.find("span",class_="title").text+"\n")
def connec_douban(num1):
    link="https://movie.douban.com/top250?start="+str(num1)+"&filter="
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    re = requests.get(link,headers=headers)
    soup = BeautifulSoup(re.text,"lxml")
    print("url-status",re.status_code,end="\n")
    return soup


if __name__=='__main__':
    start = time.time()
    manager = Manager()
    p = Pool(4)
    q = manager.Queue(10)
    #q = Queue(10)
    for j in range(0,225,25):
        q.put(j)

    for i in range(4):
        p.apply_async(func=crawler_run,args=(q,i))
        print("Start Process",i)
    p.close()
    p.join()

    end = time.time()
    print('Pool+Queue 的多进程爬虫的总时间为',end-start)
    print("END")
