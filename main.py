import os


def create_directories(project):
	"""Creates a folder in directory for every website/project

	Args:
		project (string): Name of directory to create
	"""
	if not os.path.isdir(project): 
		os.mkdir(project)


def create_file(project, url):
	"""This function creates queue and crawled files if they are not created already

	Args:
		project (string): name of each project based on url
		url (String): home page of website
	"""	
	queue = project + "/" + "queue.txt"
	crawler = project + "/" + "crawled.txt"
	if not os.path.isfile(queue):
		make_file(queue, url)
	if not os.path.isfile(crawler):
		make_file(crawler, " ")
	

def make_file(file_name, data):
	"""This function creates a file and writes data to it

	Args:
		file_name (string): name of file
		data (string): contents of file we want to write
	"""
	f = open(file_name, "w")
	f.write(data)
	f.close()

def append_to_file(path, data):
	"""This function appends data to a file

	Args:
		path (string): file we want to add to
		data (string): data we want to add to file
	"""
	with open(path, 'a') as file: 
		file.write(data + "\n")

	file.close()

def clear_file_info(path):
	"""This function clears the contents of a file

	Args:
		path (string): file we want to clear
	"""
	with open(path, "w") as file: 
		pass
	file.close()

def unique_items_in_file(filename):
	"""searches through file and adds every link to a set

	Args:
		filename (file): file we are going to be searching through

	Returns:
		set: set of all unique links 
	"""
	unique = set(filename)
	with open(filename, "rt") as file: 
		for line in file: 
			unique.add(line.replace("\n", ""))
	file.close()
	return unique

def set_items_to_file(filename, data_links):
	"""clears our file & then adds every unique link to our file

	Args:
		filename (file): file we are going to be clearing/writing to 
		data_links (set): updated links that we are going to be adding to our file
	"""
	clear_file_info(filename)

	for link in sorted(data_links): 
		append_to_file(filename, link)





create_directories("tests")
create_file("tests", "huntermacias.net")