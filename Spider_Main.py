#coding: utf-8
from scrapy.cmdline import execute
import os 
import sys
from os.path import exists

if __name__ == '__main__':
    project_name = "Wechatproject"
    spider_name = "wechat"
    results_name = "results/results.json"

    if not exists(project_name):
        print "Please Edit the project files and Run again!!!"
        sys.argv = ["scrapy", "startproject", project_name] 
        execute()
    else:
        print "Start Crawling!!!"
        path = os.getcwd() # 获取当前路径
        os.chdir(path+"/"+project_name) # 修改当前路径
        if exists(results_name):
            os.remove(results_name)
        sys.argv = ["scrapy", "crawl", spider_name]
        # sys.argv = ["scrapy", "crawl", spider_name, "-o", results_name, "-t", "json"] # 保存items，可以在pipelines.py中自定义
        execute()
    pass
