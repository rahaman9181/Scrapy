# from scrapy.utils.response import open_in_browser
import scrapy
from ..items import QuotetutorialItem


class Quotes(scrapy.Spider):

    name='quotes'
    start_urls = [
                 'https://jntukresults.edu.in/',
                 'https://jntukresults.edu.in/view-results-56736077.html',
                 # 'https://jntukresults.edu.in/results/res.php'
    ]
    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }

    # def parse(self,response):
    #     all_links = response.css('div.col-md-9 a::attr(href)').extract()
    #     print(len(all_links))

    li=[]
    d=""
    for i in range(501,599):
        b=0
        b=b+i
        d="17H71A0"+str(b)
        li.append(d)
        d=""
    # i='17H71A1201'

    def start_requests(self):
        for ht in self.li:
            print(ht)
            yield scrapy.Request(url=self.start_urls[0],callback=self.parse,meta={'ht':ht})




    def parse(self,response):
        print(type(response),"1")
        ht = response.meta['ht']
        print(ht,"in Parse")
        yield scrapy.Request(url=self.start_urls[1],callback=self.call_first,meta={'ht': ht})

    def call_first(self,response):

        ht = response.meta['ht']
        print(ht,"in call_first")
        # print(response.body)
        access = response.css('head script::text').extract()
        # print(access[1])
        data ={
               'ht' : ht,
               'id' : '56736077',
               'accessToken' : access[1][720:727],
               # 'accessToken' : '1234567',
                     }

        print(access[1][720:727],"accessToken")
        yield scrapy.FormRequest(url='https://jntukresults.edu.in/results/res.php',formdata=data,method='GET',
                                        callback=self.after_request,meta={'ht': ht})

    def after_request(self,response):
        print(type(response),'response body')
        str1 = str(response.body)
        print(response.meta['ht'])
        ht = response.meta['ht']
        print(str)
        # print(response.meta[ht],"In after_request method meta")
        # if 'Invalid Token' in str1:
        #     print("Self Parse")
        #     print(str(response.body),"Invalid")
        #     response = scrapy.http.response.html.HtmlResponse(url=self.start_urls[0],status=200)
        #     # response = yield scrapy.http.Request(url='https://jntukresults.edu.in/view-results-56736077.html')
        #     # response = scrapy.http.response.html.HtmlResponse(url='https://jntukresults.edu.in/')
        #     # print(type(response),"Invalid Response type in if statement")
        #     # print(response.body,"5")
        #     # self.parse(response)
        #     # return self.parse(response)
        #     # yield scrapy.Request(response,callback=self.parse,meta={'ht':ht})
        #     # print("After yield in after_request")
        #     yield scrapy.Request(response.url,callback=self.parse,meta={'ht':ht})
        #     # yield response.follow(callback=self.call_first,meta={'ht':ht},dont_filter=True)
        #     # yield scrapy.Request(url='https://jntukresults.edu.in/',callback=self.parse,meta={'ht':ht})
        #     # yield response.follow(callback=self.parse,meta={'ht':ht})
        # else:
            # print(response.css('table.ui th::text').extract())
            # print(response.css('table.ui td::text').extract())
        item = QuotetutorialItem()
        p = response.css('table.ui th::text').extract()
        q = response.css('table.ui td::text').extract()
                    # item['sheet'] = p
        item['result'] = q
        item['rollno'] = response.meta['ht']
        yield item
        print("After yield in after_request")
