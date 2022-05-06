import scrapy
import re
import csv


class SinefilcomExportSpider(scrapy.Spider):
    name = 'sinefilcom_export'

    def start_requests(self):
        yield scrapy.Request(f'https://sinefil.com/{self.name}/all/watched')


    def parse(self, response):
        f = open(f'./export_{self.name}.csv', 'a')
        writer = csv.writer(f)
        for movie in response.css('.movie-container .movie'):
            year = movie.css('h3.hero > .year::text').extract()[0]
            if ('-' in year):
                continue
            year = re.sub("[()]","", year)
            year.strip()
            title = movie.css('.mini-hero::text').extract()[0].strip()
            if (not title):
                title = movie.css('h3.hero > a::text').extract()[0]
            writer.writerow([title, year])
        f.close()
        next_page = response.css('.pagination ul li:nth-last-child(2) a::attr(href)').extract()[0]
        yield scrapy.Request(url = f'https://sinefil.com{next_page}', callback=self.parse)
