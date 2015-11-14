# -*- coding: utf-8 -*-
import requests
from bs4 import *

res= requests.get('http://catalog.illinois.edu/courses-of-instruction/geog/').text.encode('utf-8')
soup =BeautifulSoup(res,"html.parser")
courses=soup.select('.courses .courseblock')
outFile= open('D:/abroad/courseData/illinois/course.txt','w')
for course in courses:
    titleConten=course.select('.courseblocktitle')[0].text.encode('utf-8')
    #print titleConten
    credit=titleConten.split('credit:')[1].split('Hour')[0].replace('\t',' ').replace('\n',' ')
    courNo =titleConten.split('credit:')[0].split(' ')[0].replace('\t',' ').replace('\n',' ')+titleConten.split('credit:')[0].split(' ')[1].replace(' ','').replace('\t',' ').replace('\n',' ')
    title = ' '.join(titleConten.split('credit:')[0].split(' ')[2:]).replace('\t',' ').replace('\n',' ')
    dis=course.select('.courseblockdesc')[0].text.replace('\n',' ').encode('utf-8').replace('\t',' ')
    print title
    outFile.write(courNo+'\t'+title+'\t'+credit+'\t'+dis+'\n')
    print title,courNo,credit,dis
outFile.close()
