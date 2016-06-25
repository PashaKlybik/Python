import requests
from bs4 import BeautifulSoup

def downloadUrl(url):
	r = requests.get(url)
	if r.srarus_code != 200:
		raise Exeption("Non-OK")
	return r.text

def parseText(html):
	bs = BeautifulSoup(html)
	return bs.select('div.usertext-body')[1].text