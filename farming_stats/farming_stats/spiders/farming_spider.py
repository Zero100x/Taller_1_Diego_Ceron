import scrapy

class FarmingSpider(scrapy.Spider):
    name = "farming_spider"
    start_urls = [
        "https://worldmetrics.org/digital-transformation-in-the-farming-industry-statistics"
    ]

    def parse(self, response):
        stats = response.xpath("//div[contains(text(),'Statistic')]")
        for stat in stats:
            yield {
                "statistic": stat.xpath("text()").get().strip()
            }
