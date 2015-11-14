# -*- coding: utf-8 -*-
import requests
from bs4 import *
outFile = open('D:/abroad/courseData/george/facult.txt','w')

res=requests.get('https://cos.gmu.edu/ggs/people/faculty-staff/').text.encode('utf-8')
soup = BeautifulSoup(res, "html.parser")
links = soup.select('.one_half p a')[1::2]
#print len(links)
for link in links:
    href = link['href'].encode('utf-8')
    #print  href
    #print '------------'
    resP = requests.get(href).text.encode('utf-8')
    #print resP
    soupP = BeautifulSoup(resP, "html.parser")
    name = soupP.select('.title')[0].text.encode('utf-8')
    person = soupP.select('.one_half')[0].text.strip().encode('utf-8')
    position = person.split('Position')[1].split('Degrees')[0].strip().replace('\n','/')
    degree = person.split('Degrees')[1].strip().replace('\n','/')
    outFile.write(name+'\t'+position+'\t'+degree+'\n')
outFile.close()