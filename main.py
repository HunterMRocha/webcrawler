import os


def create_directories(project):
	if not os.path.isdir(project): 
		os.mkdir(project)


def create_file(project, url):
	"""[This function creates queue and crawled files if they are not created already]

	Args:
		project ([string]): [name of each project based on url]
		url ([String]): [home page of website]
	"""	
	queue = project + "/" + "queue.txt"
	crawler = project + "/" + "crawled.txt"
	if not os.path.isfile(queue):
		make_file(queue, url)
	if not os.path.isfile(crawler):
		make_file(crawler, " ")
	

def make_file(file_name, data):
	f = open(file_name, "w")
	f.write(data)
	f.close()

create_directories("tests")
create_file("tests", "huntermacias.net")