# # from scrapy.utils.response import open_in_browser
# import scrapy
# from ..items import QuotetutorialItem
# import mysql.connector
#
#
# class Quotes2(scrapy.Spider):
#
#     name='quotes2'
#     start_urls = [
#                  'https://jntukresults.edu.in/',
#                  'https://jntukresults.edu.in/view-results-56736077.html',
#                  # 'https://jntukresults.edu.in/results/res.php'
#     ]
#     # custom_settings = {
#         # "DOWNLOAD_DELAY": 1,
#     #     "CONCURRENT_REQUESTS_PER_DOMAIN": 5
#     # }
#
#     # def parse(self,response):
#     #     all_links = response.css('div.col-md-9 a::attr(href)').extract()
#     #     print(len(all_links))
#
#     # li=[]
#     # d=""
#     # for i in range(1201,1261):
#     #     b=0
#     #     b=b+i
#     #     d="17H71A"+str(b)
#     #     li.append(d)
#     #     d=""
#     # # i='17H71A1201'
#     id = input("Enter id number ")
#
#     def start_requests(self):
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             passwd = '',
#             database = 'quotes'
#         )
#         self.curr = self.conn.cursor()
#         self.curr.execute("select distinct rollno from quotes2 where flag=0")
#         # self.curr.execute("select distinct rollno from quotes")
#         results = self.curr.fetchall()
#         print(results)
#         print(len(results))
#
#         for row in results:
#             ht = row[0]
#             # print(type(ht))
#         # print("Total number of rows is: ", self.curr.rowcount)
#         # print(list)
#         # for ht in self.li:
#             # print(type(ht))
#             yield scrapy.Request(url=self.start_urls[0],callback=self.parse,meta={'ht':ht})
#
#
#
#
#     def parse(self,response):
#         ht = response.meta['ht']
#         yield scrapy.Request(url=self.start_urls[1],callback=self.call_first,meta={'ht': ht})
#
#     def call_first(self,response):
#         ht = response.meta['ht']
#         access = response.css('head script::text').extract()
#         id = self.id
#         data ={
#                'ht' : ht,
#                'id' : id,
#                # 'id' : '56735897',#1-1 Nov - 2016
#                'accessToken' : access[1][720:727],
#                }
#         yield scrapy.FormRequest(url='https://jntukresults.edu.in/results/res.php',formdata=data,method='GET',
#                                         callback=self.after_request,meta={'ht': ht,'id': id})
#
#     def after_request(self,response):
#         str1 = str(response.body)
#         # print(str1)
#         print(response.meta['ht'])
#         ht = response.meta['ht']
#         id = response.meta['id']
#         item = QuotetutorialItem()
#         rows = response.css('table.ui tr')
#         if len(rows)!=0:
#             for row in rows:
#                 td = row.css('td')
#                 if len(td)!=0:
#                 # print(td[0].css("td::text").extract(),"Sub Code")
#                 # print(td[1].css("td::text").extract(),"Sub Name")
#                 # print(td[2].css("td::text").extract(),"Sub Grade")
#                 # print(td[3].css("td::text").extract(),"Sub Credits")
#                 # q=td[0].css("td::text").extract_first()
#                 # print(q)
#                     item['rollno'] = ht
#                     item['subjectcode'] = td[0].css("td::text").extract_first()
#                     item['subjectname'] = td[1].css("td::text").extract_first()
#                     item['grade'] = td[2].css("td::text").extract_first()
#                     item['credits'] = td[3].css("td::text").extract_first()
#                     item['flag'] = id
#                     yield item
#         if "Invalid Token" in str1:
#             print('Invalid token')
#             item['rollno'] = ht
#             item['flag'] = 0
#             yield item
#         if "Invalid Hall Ticket Number" in str1:
#             print('Invalid Hall Ticket')
#             item['rollno'] = ht
#             item['flag'] = 1
#             yield item
