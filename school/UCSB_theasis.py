# coding: utf-8
import requests
from bs4 import *
years=['1977-1990','1991-2000','2001-2010','2011-2020',]
url='http://www.geog.ucsb.edu/graduates/masters-theses/{0}.html'
thesis = open('D:/abroad/courseData/UCSB_thesis.txt','w')
for year in years:
    res=requests.get(url.format(year)).text.encode('utf-8')
    soup = BeautifulSoup(res,"html.parser")
    for data in soup.select('#striped tr'):
        #print data.text.encode('utf-8')
        for prin in data.select('th'):
            print prin.text.encode('utf-8')
            thesis.write(prin.text.encode('utf-8').strip().replace('\t','')+'\t')
        for prin in data.select('td'):
            print prin.text.encode('utf-8')
            thesis.write(prin.text.encode('utf-8').strip().replace('\t','')+'\t')
        thesis.write('\n')
        print '-----------------'
thesis.close()


