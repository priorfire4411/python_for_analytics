#import urllib.request
import urllib
import requests
from bs4 import BeautifulSoup
import time
# https://docs.python.org/dev/library/concurrent.futures.html#threadpoolexecutor
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import pandas as pd
import io
import os
import re
from multiprocessing import Pool

def get_parsed_html(url):
	'''
	param url: string of a url to be scraped
	return: bs4.BeautifulSoup
	'''
	mybytes = urllib.request.urlopen(url).read().decode("utf8")
	return BeautifulSoup(mybytes, features="lxml")

def get_download_urls(parsed_html, download_url):
	'''
	param parsed_html: bs4.BeautifulSoup object
	return: list of url strings that download csvs, list of url 
		strings that download xlsx
	'''
	table_data = parsed_html.body.find('table', attrs={'id':'data_table'})
	urls = [download_url + i['href'] for i in table_data.find_all("a")]
	return [x for x in urls if "csv" in x], [x for x in urls if "xlsx" in x]

def get_file_names(url, pattern, directory):
	'''
	param url: string, url
	param pattern: a regex to extract the file name from the url
	return: string, the file name to be used
	https://www.ers.usda.gov/webdocs/DataFiles/51035/apples.xlsx?v=0
	returns apples.xlsx
	'''
	r = re.search(pattern, url)
	return directory + url[r.span()[0]:r.span()[1]]

def xlxs_url_to_pandas(url, path):
	'''
	param url: string, url to download xlsx file
	param path: where to save the file to disk
	return: none
	'''
	f = requests.get(url).content
	with io.BytesIO(f) as fh:
		df = pd.io.excel.read_excel(fh)
	df.to_csv(path, index = False)

def csv_url_to_pandas(url, path):
	'''
	param url: string, url to download xlsx file
	param path: where to save the file to disk
	'''
	df = pd.read_csv(url, encoding = "ISO-8859-1")
	df.to_csv(path, index = False)

def scrape_and_save(tup):
	if "csv" in tup[0]:
		csv_url_to_pandas(tup[0], tup[1])
	elif "xlsx" in tup[0]:
		xlxs_url_to_pandas(tup[0], tup[1])


if __name__ == '__main__':


	# where we save our scraped files
	parent_directory = os.path.dirname(os.getcwd())
	csv_directory = parent_directory + "/data/csv/"
	xlxs_directory = parent_directory + "/data/xlsx/"

	# regex to extract file name
	pattern = r"(\w+\.)((csv)|(xlsx))"

	# urls to use
	url = r"https://www.ers.usda.gov/data-products/fruit-and-vegetable-prices/"
	download_url = r"https://www.ers.usda.gov"

	# get beautiful soup object
	parsed_html = get_parsed_html(url)

	# get csv and xlxs files
	csv_urls, xlsx_urls = get_download_urls(parsed_html, download_url)

	# make tuples of (download url, file name)
	csv_names = [get_file_names(u,pattern,csv_directory) for u in csv_urls]
	xlsx_names = [get_file_names(u,pattern,xlxs_directory) for u in xlsx_urls]

	# list of tuples
	iterable = list(zip(csv_urls, csv_names)) + list(zip(xlsx_urls, xlsx_names)) * 4
	print(len(iterable))

	# start timer
	start = time.time()

	# single thread, single core - 27 seconds
	#for idx,i in enumerate(iterable):
	#	scrape_and_save(i)
	#	print("Complete:{}%".format(round(idx/len(iterable),2)*100))

	# multi threading 4 workers - 12 seconds
	# multi threading 8 workers - 4 seconds
	# ProcessPoolExecutor, ThreadPoolExecutor
	with ProcessPoolExecutor(8) as executor:
		results = executor.map(scrape_and_save, iterable)


	# multi threading 4 workers - 7 seconds
	# multi threading 8 workers - 4 seconds
	#with Pool(8) as executor:
	#	results = executor.map(scrape_and_save, iterable)


	print("Elapsed Time:{}".format(time.time() - start))
