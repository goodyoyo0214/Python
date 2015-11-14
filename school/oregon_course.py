# -*- coding: utf-8 -*-
import requests
from bs4 import *
outFile = open('D:/abroad/courseData/oregon/course.txt','w')
res =requests.get('http://geography.uoregon.edu/courses/').text.encode('utf-8')
soup = BeautifulSoup(res,"html.parser")
courses = soup.select('.page.content p')[2:]
for course in courses:
    if len(course.select('strong'))>0:
        #print course
        title = course.select('strong')[0].text.encode('utf-8').split('(')[0].replace('\t',' ').replace('\n',' ')
        credit = course.select('strong')[0].text.split('(')[1].encode('utf-8').replace(')','').replace('\t',' ').replace('\n',' ')
        [s.extract() for s in course('strong')]
        dis = course.text.encode('utf-8').replace('\t',' ').replace('\n',' ')
        print title , credit , dis
        outFile.write(title+'\t'+credit+'\t'+dis+'\n')
        print '----------------'
outFile.close()
