# coding=utf-8
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl spider_1'.split())  # 这就是我们在命令行中的代码
    # cmdline.execute('scrapy crawl Spider2 -o items.csv -t csv'.split())