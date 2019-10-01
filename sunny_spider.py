# -*- coding: utf-8 -*-
import scrapy


class SunnySpiderSpider(scrapy.Spider):
    name = 'sunny_spider'
    allowed_domains = ['https://www.sunnyelectronics.com.au/']
    start_urls = ['https://www.sunnyelectronics.com.au/Fridges.html',
                  'https://www.sunnyelectronics.com.au/Washing_Machines.html',
                  'https://www.sunnyelectronics.com.au/Dryer_Combos.html',
                  'https://www.sunnyelectronics.com.au/Microwave_Vacuum_TV.html']

    def parse(self, response):
        product_name = response.css("div.name h3::text").extract()
        product_price = response.css("span.price-new::text").extract()
        product_imagelink = response.css("div.product-list div.image img::attr(src)").extract()
        product_URL = response.css("div.product-list a::attr(href)").extract()

        row_data = zip(product_name, product_price, product_imagelink, product_URL)

        # Making extracted data row-wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'category': '',
                'sub-category': '',
                'product_name': item[0],
                # item[0] means product int the list and so on,index tells what value to assign
                'product_price': item[1],
                'product_imageURL': item[2],
                'product_URL': item[3]
            }
            # yield or give the scraped info to scrapy
            yield scraped_info
