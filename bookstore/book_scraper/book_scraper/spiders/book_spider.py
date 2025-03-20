import scrapy

class BookSpider(scrapy.Spider):
    name = "book_spider"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
                "availability": "In stock" in book.css("p.instock.availability::text").get(),
                "url": response.urljoin(book.css("h3 a::attr(href)").get()),
            }

        # صفحه بعدی را بررسی کن
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
