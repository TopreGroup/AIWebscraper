# -*- coding: utf-8 -*-
import scrapy


class KnnSpiderSpider(scrapy.Spider):
    name = 'knn_spider'
    allowed_domains = ['knncomputers.com.au']
    start_urls = ['https://www.knncomputers.com.au/collections/computer-packages']

    def parse(self, response):
        product_name = response.css("p::text").extract()
        product_price = response.css(".medium--left > small:nth-child(2)::text").extract()
        #product_imagelink = response.css("div.product-list div.image img::attr(src)").extract()
        product_URL = response.css("a.product-grid-item::attr(href)").extract()

        row_data = zip(product_name, product_price, product_URL)

        # Making extracted data row-wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'category': 'Desktops',
                'sub-category': 'Computer Packages',
                'product_name': item[0],    # item[0] means product int the list and so on,index tells what value to assign
                'product_description': '',
                'product_price': item[1],
                'product_imageURL': '',
                'product_URL': item[2]
            }
            # yield or give the scraped info to scrapy
            yield scraped_info
