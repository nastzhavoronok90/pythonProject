import scrapy
from scrapy.http import HtmlResponse
from parser_job_hh.items import ParserJobHhItem

class HhRuSpider(scrapy.Spider):
    name = "hh_ru"
    allowed_domains = ["hh.ru"]
    start_urls = [
        'https://spb.hh.ru/search/vacancy?area=88&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20'
    ]

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vacancies_links = response.xpath("//div[@class ='serp-item']//a[@data-qa='serp-item__title']/@href").getall()
        for link in vacancies_links:
            yield response.follow(link, callback=self.parse_vacancy)

    def parse_vacancy(self, response:HtmlResponse):
        vacancy_name = response.css("h1::text").get()
        vacancy_salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        vacancy_url = response.url

        yield ParserJobHhItem(
            name=vacancy_name,
            salary=vacancy_salary,
            url=vacancy_url
        )


