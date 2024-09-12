import scrapy
from comments_project.items import CommentItem


class CommentsSpider(scrapy.Spider):
    name = "comments"
    start_urls = ['http://example.com/comments_page']

    def parse(self, response):
        for comment in response.css('div.comment'):
            item = CommentItem()
            item['author'] = comment.css('span.author::text').get()
            item['comment_text'] = comment.css('div.text::text').get()
            item['date_posted'] = comment.css('span.date::text').get()
            yield item
        
        # Example for pagination
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)