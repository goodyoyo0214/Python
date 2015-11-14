# coding: utf-8
import requests
from bs4 import *

url ='http://catalog.utdallas.edu/2015/graduate/courses/gisc'
outFile=open('D:/abroad/courseData/UT-Dallas/Dallas_course.txt','w')
res = requests.get(url, "html.parser")
soup = BeautifulSoup(res.text.encode('utf-8'))
courses = soup.select('#bukku-page p')
for course in courses:
    #print course
    courNo=course.select('.course_address')[0].text.encode('utf-8').strip()
    courTit=course.select('.course_title')[0].text.encode('utf-8').strip()
    credit=course.select('.course_hours')[0].text.split('(')[1].split('semester')[0].encode('utf-8').strip()
    print courNo,courTit,credit
    outFile.write(courNo+'\t'+courTit+'\t'+credit)
    [s.extract() for s in course('span')]
    disc=course.text.split('. (')[0].replace('\t',' ').encode('utf-8')
    if len(disc.split('Prerequisite:'))>1:
        disc=disc.split('Prerequisite:')
        print 'dis: '+disc[0].encode('utf-8')
        print 'Prerequisite: '+disc[1].encode('utf-8')
        outFile.write('\t'+disc[1].encode('utf-8').strip()+'\t'+disc[0].encode('utf-8').strip())
    else:
        print 'dis: '+disc.strip()
        print 'Prerequisite: None'
        outFile.write('\t'+'None\t'+disc.strip())
    outFile.write('\n')
outFile.close()
