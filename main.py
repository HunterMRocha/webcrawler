import threading
from queue import Queue
from spider import Spider
from domain import *
from util import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://www.thenewboston.com/'
DOMAIN_NAME = get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 12

thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
