import scrapy
from ..items import JewelryItem
from ..items import DetailsItem
from ..items import NameItem
from ..items import PriceItem

class ArtyvisSpider(scrapy.Spider):
    name = 'houseofindya'
    pageNumber = 2
    start_urls = [
        'https://www.houseofindya.com/zyra/cat?depth=1&label=Jewelry'
    ]
    BASE_URL = 'http://www.houseofindya.com/'


    def parse(self, response):

        all_necklace_sets = response.css("#JsonProductList")
        detailsItem = DetailsItem()
        nameItem = NameItem()
        priceItem = PriceItem()
        index = -1
        list1 = []
        list2 = []

        for necklace_set in all_necklace_sets:
            name = all_necklace_sets.css('li a::attr(title)').extract()
            nameItem['name'] = name

            for names in nameItem['name']:
                index += 1
                if names.find("Necklace Set") >= 0:
                    details_page = necklace_set.css('a::attr(href)')[index].extract()
                    list1.append(details_page)
                    price = necklace_set.css('li::attr(data-price)')[index].extract()
                    list2.append(price)

            detailsItem['details_page'] = list1
            priceItem['price'] = list2

            for link in detailsItem['details_page']:
                absolute_url = self.BASE_URL + link
                yield scrapy.Request(absolute_url, callback=self.parse_attr)

            load_more = 'https://www.houseofindya.com/zyra/cat?depth=1&label=jewelry&page=' + str(ArtyvisSpider.pageNumber)
            if ArtyvisSpider.pageNumber < 9:
                ArtyvisSpider.pageNumber += 1
                yield response.follow(load_more,callback=self.parse)


    def parse_attr(self, response):
        items = JewelryItem()
        items['name'] = response.css('h1::text').extract()
        items['description'] = response.css('#tab-1 p::text').extract()
        items['price'] = response.css('h4 span::text')[1].extract()
        items['image_url'] = response.css('img.lazySlider::attr(data-original)').extract()

        return items



