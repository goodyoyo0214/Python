__author__ = 'Dale'# -*- coding: utf-8 -*-
import requests
from bs4 import *

res = requests.get('http://spatial.usc.edu/index.php/about-us/faculty/').text.encode('utf-8')
soup = BeautifulSoup(res,"html.parser")
links = soup.select('.row-fluid')
for link in links:
    print link
    linkU = link.select('a')[0]
    name = linkU.text.encode('utf-8')
    url = linkU['href'].encode('utf-8')
    print name, url