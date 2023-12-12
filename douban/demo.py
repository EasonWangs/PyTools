# coding: utf8

# 匹配规则
RULES = {
    # 每个帖子项
    "topic_item": "//table[@class='olt']/tr",
    "url_list": "//table[@class='olt']/tr/td[@class='title']/a/@href",
    # 列表元素
    "title": "td[@class='title']/a/@title",
    "author": "td[@nowrap='nowrap'][1]/a/text()",
    "reply": "td[@nowrap='nowrap'][2]/text()",
    "last_reply_time": "td[@class='time']/text()",
    "url": "td[@class='title']/a/@href",
    # 帖子详情
    "detail_title_sm": "//td[@class='tablecc']/text()",
    # 完整标题
    "detail_title_lg": "//div[@id='content']/h1/text()",
    "create_time": "//span[@class='color-green']/text()",
    "detail_author": "//span[@class='from']/a/text()",
    "content": "//div[@class='topic-richtext']/p/text()",
}




import time
import random
import logging

import gevent
import requests
from gevent.pool import Pool
from gevent.queue import Queue
from lxml import etree

class HTTPError(Exception):

    """ HTTP状态码不是200异常 """

    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return "%s HTTP %s" % (self.url, self.status_code)


class URLFetchError(Exception):

    """ HTTP请求结果为空异常 """

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "%s fetch failed!" % self.self.url



class RegHtmlDemo():

    def __init__(self):

        self.rules = RULES

    def fetch(self, url):
        """发起HTTP请求

        @url, str, URL
        @timeout, int, 超时时间
        @retury_num, int, 重试次数
        """
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'}
        resp = requests.get(url, headers=headers)
        return resp.content.decode("utf8")

    def extract(self, regx, body, multi=False):
        """解析元素,xpath语法

        @regx, str, 解析表达式
        @body, unicode or element, 网页源码或元素
        @multi, bool, 是否取多个
        """
        if isinstance(body, str):
            body = etree.HTML(body)
            print(body)
        res = body.xpath(regx)

        if multi:
            return res
        return res[0] if res else None

    def run(self):
        topic_url = "https://www.douban.com/group/topic/166020148/"
        # html = self.fetch(topic_url)
        html = "<!doctype><html><head><title>aaa</title></head><body><div id='content'><h1>title</h1><div class='topic-richtext'><p>p1</p></div><div class='topic-richtext'><p>p2</p></div></div></body></html>"

        topic = {}
        title = self.extract(self.rules["detail_title_sm"], html) \
                or self.extract(self.rules["detail_title_lg"], html)
        if title is None:
            return None
        topic["title"] = title.strip()
        topic["create_time"] = self.extract(
            self.rules["create_time"], html)
        topic["author"] = self.extract(
            self.rules["detail_author"], html)
        topic["content"] = '\n'.join(self.extract(self.rules["content"], html, multi=True))

        print(topic["title"])
        print(topic["content"])

def main():
    """ main """
    RegHtmlDemo().run()


if __name__ == "__main__":
    main()
