from urllib.request import urlopen
from link_finder import LinkFinder as lk 
from util import * 
import logging

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

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			total_remaining = str(len(Spider.queue))
			total_crawled = str(len(Spider.crawled))
			print("------------------------------------------------")
			print(f"Working on thread {thread_name}\nNow crawling {page_url}")
			print(f"Total links remaining: {total_remaining}")
			print(f"Total pages crawled {total_crawled}")
			print("------------------------------------------------\n")
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()

	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try: 
			response = urlopen(page_url)
			if response.getheader("Content-Type") == "text/html":
				html_bytes = response.read() # when we orig. read from url we are given bytes
				html_string = html_bytes.decode("utf-8") # this will convert our bytes to english
			finder = lk(Spider.base_url, page_url)
			finder.feed(html_string)
		except: 
			logging("Error: Cannot crawl page :( ")
			return set()

		return finder.page_links()

	@staticmethod
	def add_links_to_queue(links):
		for url in links: 
			if url not in Spider.queue and url not in Spider.crawled: 
				Spider.queue.add(url)	
			if Spider.domain_name not in url: # we need this so we don't crawl random links like social medias
				continue
		
	@staticmethod
	def update_files():
		print("updating files")
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)