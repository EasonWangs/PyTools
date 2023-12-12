# coding: utf8

"""配置
"""

# User-Agent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 6.3; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"
)

# mongo config
DB_URI = "mongodb://127.0.0.1:27017"
# DB_URI = "mongodb://192.168.6.7:27017"
DB_NAME = "douban_group"

# 豆瓣小组URL
GROUP_LIST = [
    # "https://www.douban.com/group/510976/",
    "https://www.douban.com/group/251352/",
    # "https://www.douban.com/group/qiong/",
    # "https://www.douban.com/group/quriben/"
]

# 后缀
GROUP_SUFFIX = "discussion?start=%d"

# 抓取前多少页
MAX_PAGE = 100

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
    # "content": "//div[@class='topic-richtext']/p/text()",
    "content": "//div[@class='bg-img-green']/h4/a/text()",

}

# 并发数
POOL_SIZE = 10

# 监控周期(秒),默认10分钟
WATCH_INTERVAL = 10 * 60

# 重载代理周期
PROXY_INTERVAL = 30 * 60
