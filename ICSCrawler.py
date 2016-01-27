'''
@Author: Ryan Atkins
'''

from Crawler4py.Crawler import Crawler
from CrawlerConfig import CrawlerConfig

crawler = Crawler(CrawlerConfig())

print (crawler.StartCrawling())

exit(0)