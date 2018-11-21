#coding=utf-8
import urllib
from urllib import urlopen
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter


html = urlopen('https://www.zhihu.com/')
# print(html.read())
bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find_all(attrs = {'class' : 'QuestionItem-title'})
print (text_list)
for text in text_list:
	print(text.get_text())
html.close()