from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

	def __init__(self, homepage, diff_page):
		super().__init__()
		self.homepage = homepage
		self.diff_page = diff_page
		self.links = set()

	def handle_starttag(self, tag, attrs):
		if tag == 'a': # find all anchor tags
			for (attribute, value) in attrs: # go through every attr and its value
				if attribute == "href":
					url = parse.urljoin(self.homepage, value)
					self.links.add(url)

	def page_links(self):
		return self.links

	def error(self, message):
	 return super().error(message)


 