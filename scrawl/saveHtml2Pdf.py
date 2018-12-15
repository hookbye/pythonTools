#coding=utf-8

import requests
from bs4 import BeautifulSoup
import pdfkit

def parse_url_to_html(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,"html.parser")
	body = soup.find_all(class_="x-wiki-content")[0]
	html = str(body)
	with open("a.html",'wb') as f:
		f.write(html)

def get_url_list():
	#
	response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
	soup = BeautifulSoup(response.content,"html.parser")
	menu_tag = soup.find_all(class_ = "uk-nav uk-nav-side")[1]
	urls = []
	for li in menu_tag.find_all("li"):
		url = "http://www.liaoxuefeng.com" + li.a.get('href')
		urls.append(url)
	return urls

def save_pdf(htmls):
	options = {
		'page-size':'Letter',
		'encoding':"UTF-8",
		'custom-header':[
			('Accept-Encoding','gzip')
		]
	}
	pdfkit.from_file(htmls,"a.pdf",options=options)

if __name__ == '__main__':
	urls = get_url_list()

	for url in urls:
		parse_url_to_html(url)
	save_pdf("a.html")
