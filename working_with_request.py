from scrapy import Selector
import requests

# link = 'https://en.wikipedia.org/wiki/Web_scraping'
# html = requests.get(link).content
# # print(html)
# sel = Selector(text = html)

# print(len(sel.xpath('//*')))


html = """
<p id="p-example">
Hello World!
Try <a href="http://www/datacamp.com">DataCamp</a>Today!
</p>
"""

print(html)
sel = Selector(text = html)

## using text
print(sel.xpath('//p[@id="p-example"]/text()').extract())

print(sel.xpath('//p[@id="p-example"]//text()').extract())

##  using css locator
print(sel.css('p#p-example::text').extract())
print(sel.css('p#p-example ::text').extract())
