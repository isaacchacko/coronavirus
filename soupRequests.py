# note: "lxml" is required
import requests
from bs4 import BeautifulSoup as bs
import lxml
class RequestBot():
	def __init__(self, url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}):
		self.url = url
		self.headers = headers
		self.page = requests.get(self.url, headers = self.headers)
		self.soup = bs(self.page.content, 'lxml')


if __name__ == '__main__':
	pass