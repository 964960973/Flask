# 从geven库导入monkey模块
from gevent import monkey

# monkey.path_all()能把程序变成协作式运行，帮助程序实现异步
monkey.patch_all()

# 导入gevent,requests,time
import gevent
import requests
import time

# 记录程序开始时间
start = time.time()

# 将8个网址封装成列表
url_list = [
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'http://www.iqiyi.com/',
    'https://www.tmall.com/',
    'http://www.ifeng.com/']


# 定义一个crawler函数
def crawler(url):
    response = requests.get(url)
    print(url, time.time() - start, response.status_code)


# 创建空的任务列表
task_list = []

# 遍历url_list
for url in url_list:
    # 使用gevent.spawn创建任务
    task = gevent.spawn(crawler, url)
    task_list.append(task)

# 执行任务列表中的所有任务，让爬虫爬取网站
gevent.joinall(task_list)

# 记录程序结束时间
end = time.time()
print(end - start)
