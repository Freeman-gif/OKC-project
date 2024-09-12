# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class CommentItem(scrapy.Item):
    author = scrapy.Field()
    comment_text = scrapy.Field()
    date_posted = scrapy.Field()

