import threading
from queue import Queue
from spider import Spider
from domain import *
from util import *

PROJECT_NAME = 'espn'
HOMEPAGE = 'https://www.espn.com'
DOMAIN_NAME = get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 12

thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# create worker threads (will die when main exits)
def create_spiders():
	for _ in range(NUMBER_OF_THREADS):
		tr = threading.Thread(target=work)
		tr.daemon = True # add this so when main exits all of our threads die
		tr.start()

# do next job in the queue
def work():
	while True: 
		url = thread_queue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		thread_queue.task_done()

# each queue link is a new job
def create_jobs():
	for link in unique_items_in_file(QUEUE_FILE):
		thread_queue.put(link)
	thread_queue.join()
	crawl()

# check if there are items in the queue, if there are then crawl them
def crawl():
	print('running crawl...')
	queue_links = unique_items_in_file(QUEUE_FILE)
	print(f"{str(queue_links)} links remaining...\n")
	create_jobs()


create_jobs()
crawl()