import re

import scrapy

from movie_spider.items import MovieSpiderItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['http://www.dy2018.com/html/gndy/dyzz/index.html']
    # 主站链接 用来拼接
    base_site = 'http://www.dy2018.com'


    def parse(self, response):
        movie_list = response.xpath('//*[@id="header"]/div/div[3]/div[6]/div[2]/div[2]/div[2]/ul//table')
        for movieBody in movie_list:
            # 带下载链接的详情页url
            url = self.base_site + movieBody.xpath('tr[2]/td[2]/b/a/@href').extract()[0]
            name = movieBody.xpath('tr[2]/td[2]/b/a/@title').extract_first()
            click_count = movieBody.xpath('tr[3]//font/text()').extract_first()
            location = movieBody.xpath('tr[4]/td/text()').extract_first()
            # 解析具体变量
            movie_item = MovieSpiderItem()
            movie_item['name'] = name
            movie_item['click_count'] = click_count.split('：')[2].replace(' ', '')
            movie_item['location'] = re.sub('\s', '', location.split('◎')[4])[2:]
            movie_item['type'] = re.sub('\s', '', location.split('◎')[5])[2:]
            movie_item['show_time'] = re.sub('\s', '', location.split('◎')[8])[4:]
            movie_item['grade'] = re.sub('\s', '', location.split('◎')[9])[4:7]
            # meta可以带参数到详情页爬虫中
            yield scrapy.Request(url=url, callback=self.getInfo, meta={'item': movie_item})
        for i in range(2, 6):
            if i < 6:
                next_url = self.base_site + '/html/gndy/dyzz/index_' + str(i) + '.html'
            yield scrapy.Request(url=next_url, callback=self.parse)

    def getInfo(self, response):
        item = response.meta['item']
        # 提取下载链接
        item['link'] = response.xpath('//*[@id="downlist"]/table[1]/tbody/tr/td/a/@href').extract()
        print(item)
        yield item
