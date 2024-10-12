

# Import the scrapy library
import scrapy
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    url_short = "https://www.datacamp.com/courses/all"
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css('p.course-block__author-name::text')
    # Here we will just return the list of Authors
    return author_names
  

process = CrawlerProcess()
process.crawl(DCspider)
process.start()
