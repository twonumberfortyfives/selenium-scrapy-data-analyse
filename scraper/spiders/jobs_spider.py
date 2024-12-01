from pathlib import Path

import scrapy
from scrapy.http import Response


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["jobs.dou.ua"]
    start_urls = [
        "https://jobs.dou.ua/vacancies/?category=Python"
    ]

    def parse(self, response: Response, **kwargs):
        filename = "jobs.html"
        Path(filename).write_bytes(response.body)
