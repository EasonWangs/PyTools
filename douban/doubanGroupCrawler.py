import urllib.request
import requests
import urllib.parse
import re
# import chardet
import urllib.request, urllib.parse, http.cookiejar
from bs4 import BeautifulSoup


# urls存储url，new_urls存储待爬取的url，old_urls存储已经爬过的url
class UrlManger(object):
    """docstring for UrlManger"""

    def __init__(self):
        self.new_urls = set()  # 定义new_urls为一个集合,用来存储还未parse的urls
        self.old_urls = set()  # 定义old_urls为一个集合，用来存储已经爬取过的urls，后来发现定义成set不好，因为set里面的元素无序存储，取出的时候得到的页面是混乱的。

    def get_new_url(self):
        new_url = self.new_urls.pop()  # 用set的pop()方法取得新的new_url,pop()的好处是每次从set的最后一位取值，取得的值从set里删除
        # print('get_new_urllalalala'+ new_url)
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        else:
            for url in urls:
                self.add_new_url(url)

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return (len(self.new_urls)) != 0


class HtmlDowloader(object):
    """docstring for UrlManger"""

    def __init__(self):
        pass

    def download(self, url):
        if url is None:
            return None
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'}
        response = requests.get(url, headers=headers)
        # Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0

        if response.status_code != 200:
            print(response.status_code)  # 有几次爬的太频繁了，直接被网站禁止访问了。一直不知道哪有错，直到打印了状态码才找到问题，这句还很重要。
            return None
        return response.content


class HtmlParser(object):
    """docstring for HtmlParser"""

    def __init__(self):
        pass

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # links1=soup.find_all('a',href=re.compile(r"/topic/\d+"))
        links_discuss = soup.find_all('a', href=re.compile(r"/discussion"))  # 审查元素，表示页面的链接含有discussion
        #links_topic = soup.find_all('a', href=re.compile(r"/topic/\d+"), text=re.compile(u'女征男'))  # 找到标题中含有“男”字的链接
        links_people = soup.find_all('a', href=re.compile(r"/people"), text=re.compile('Vivi'))  # 找到标题中含有“男”字的链接
        # print(links_topic)
        for link1 in links_people:
            print(link1)  # 打印标题
        links = links_discuss
        # print(links)
        for link in links:
            # print(link.get_text())
            new_url = link['href']
            # print(page_url,new_url)

            new_full_url = urllib.parse.urljoin(page_url, new_url)  # urljoin的作用是把前一个链接和后面的链接合并成一个完整的链接
            # print(page_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # people_node=soup.find('a',href=re.compile(r"/people/\d+"))
        # print('begin get_new_data')
        people_node = soup.find('a', href=re.compile(r"/people/\d+"))
       # print(people_node)
        # res_data['people']=people_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data


class HtmlOutputer(object):
    """docstring for HtmlOutputer"""

    def __init__(self):
        pass

    def output(self):
        print('craw successfully')

    def collect_data(new_data):
        print('get new data successfully')


class SpiderMain(object):
    """docstring for SpiderMain"""

    def __init__(self):
        # super(SpiderMain, self).__init__()
        # self.arg = arg# self.arg=arg
        print('SpiderMain begin')
        self.urls = UrlManger()
        # print(type(self.urls))
        # print(self.urls)
        self.downloader = HtmlDowloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count, new_url))
                # print(new_url)
                # print(new_url.get_text())
                html_cont = self.downloader.download(new_url)
                # print('before parse')
                # print(type(new_url))
                # print(type(html_cont))

                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # print('before add')

                self.urls.add_new_urls(new_urls)
                # print('before count')
                # self.outputer.collect_data(new_data)
                if count == 200:
                    break
                count = count + 1
            except:
                print(count, 'craw failed')
        self.outputer.output()


if __name__ == '__main__':
    root_url = 'https://www.douban.com/group/510976/'
    # print('main begin')
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)