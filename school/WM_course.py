# -*- coding: utf-8 -*-
import requests
from bs4 import *

res =requests.get('http://www.geography.wisc.edu/faculty/').text.encode('utf-8')
soup = BeautifulSoup(res,"html.parser")
links = soup.select('.leftCol a')
for link in links:
    if len(link.text.encode('utf-8').split('@'))==1:
        name = link.text.encode('utf-8')
        url = link['href'].encode('utf-8')
        print name, url
