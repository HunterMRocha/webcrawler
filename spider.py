from urllib.request import urlopen
from link_finder import LinkFinder as lk 
from util import * 


class Spider: 

	# Class variables (shared amoung all instances)
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()


	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.project_name + "/queue.txt"
		Spider.crawled_file = Spider.project_name + "/crawled.txt"
		self.load_page()
		self.crawl_page('Mother Spider', Spider.base_url)

	@staticmethod
	def load_page():
		create_directories(Spider.project_name)
		create_file(Spider.project_name, Spider.base_url) 
		Spider.queue = unique_items_in_file(Spider.queue_file)
		Spider.crawled = unique_items_in_file(Spider.crawled_file)

