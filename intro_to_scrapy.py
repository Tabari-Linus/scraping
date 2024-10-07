from scrapy import Selector

html = """
<html>
<body>
    <div class="hello datacamp">
    <p>Hello World!</p>
    </div>
    <p>Enjoy DataCamp!</p>
</body>
</html>
"""

sel = Selector(text=html)

print(sel.xpath('//p').extract())
print(sel.xpath('//p')[0].extract())
print(sel.xpath('//p').extract_first())