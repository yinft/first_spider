from scrapy.cmdline import execute

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 如果要运行其他的网络爬虫，只需修改上面代码中字符串里面的命令即可
execute(["scrapy", "crawl", "movie", "-o", "movie.csv"])