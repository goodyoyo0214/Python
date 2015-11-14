# coding: utf-8
import requests
from bs4 import *

url = 'https://geography.osu.edu/courses'

res=requests.get(url).text.encode('utf-8')
soup =BeautifulSoup(res, "html.parser")
courses = soup.select('tbody tr')
outFile = open('D:/abroad/courseData/Ohio/course.text','w')
for course in courses:
    subject=course.select('.views-field.views-field-field-subject-abbreviation')[0].text.replace('\t','').strip().encode('utf-8')
    courNo = course.select('.views-field.views-field-field-course-number')[0].text.replace('\t','').strip().encode('utf-8')
    title = course.select('.views-field.views-field-title')[0].text.replace('\t','').strip().encode('utf-8')
    credit = course.select('.views-field.views-field-field-credit-hours')[0].text.replace('\t','').strip().encode('utf-8')
    href = 'https://geography.osu.edu/'+course.select('.views-field.views-field-title a')[0]['href'].encode('utf-8')
    conRes = requests.get(href).text.encode('utf-8')
    soupC= BeautifulSoup(conRes, "html.parser")
    contnet= soupC.select('.field-item.even')[0].text.strip().replace('\n',' ').replace('\t','').encode('utf-8')

    outFile.write(subject+'\t'+courNo+'\t'+title+'\t'+credit+'\t'+href+'\t'+contnet+'\n')
    print subject, courNo ,title, credit ,href , contnet