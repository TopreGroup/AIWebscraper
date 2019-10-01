# -*- coding: utf-8 -*-
import scrapy
from ..items import AmtelectronicsItem

class AmtSpiderSpider(scrapy.Spider):
    name = 'amt_spider'
    page_number = 2
    start_urls = [
        'https://www.amtelectronics.net.au/product-category/tablets/tablet-accessories/'
    ]

    def parse(self, response):
        #items = AmtelectronicsItem()

        product_name = response.css('.woocommerce-loop-product__title::text').extract()
        product_price = response.xpath(
            "//span[@class='price']/span[@class='woocommerce-Price-amount amount']/text()").extract()
        product_imagelink = response.css('.attachment-shop_catalog.size-shop_catalog.wp-post-image::attr(src)').extract()
        product_URL = response.css('.woocommerce-LoopProduct-link.woocommerce-loop-product__link::attr(href)').extract()

        row_data = zip(product_name, product_price, product_imagelink, product_URL)

        # Making extracted data row-wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'category': 'Tablets',
                'sub-category': 'Tablet Accessories',
                'product_name': item[0],
                # item[0] means product int the list and so on,index tells what value to assign
                'product_price': item[1],
                'product_imageURL': item[2],
                'product_URL': item[3]
            }
            # yield or give the scraped info to scrapy
            yield scraped_info

        next_page = 'https://www.amtelectronics.net.au/product-category/tablets/tablet-accessories/page/' + str(AmtSpiderSpider.page_number) + '/'
        if AmtSpiderSpider.page_number<=100:
            AmtSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
