import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):


        books=response.css("article.product_pod h3 a::attr(title)").getall()
        for bookname in books:
           
           print()
           

           print('bookname',bookname)



           yield {
               'bookname':bookname
           }

       
