# -*- coding: utf-8 -*-
import requests
from bs4 import *
import time
'''
#course
res =requests.get('http://www.geog.psu.edu/academics/courses').text.encode('utf-8')
soup = BeautifulSoup(res,"html.parser")
hrefs= soup.select('.views-field-title a')
outFile = open('D:/abroad/courseData/pennstate/course.txt','w')
for href in hrefs:
    link = href['href'].encode('utf-8')
    title=href.text.encode('utf-8')
    resC =requests.get('http://www.geog.psu.edu/'+link).text.strip().encode('utf-8')
    soupC = BeautifulSoup(resC, "html.parser")
    dis=soupC.select('#body p')[0].text.encode('utf-8').strip().replace('\n', ' ')
    field = soupC.select('#field_course_geo_field p')[0].text.strip().encode('utf-8')
    lv = soupC.select('#field_course_audience p')[0].text.strip().encode('utf-8')
    print title, field , lv , dis
    outFile.write(title+'\t'+field+'\t'+lv +'\t'+dis+'\n')
outFile.close()
'''

'''--------------faculty-----------------'''
outFile = open('D:/abroad/courseData/pennstate/faculty.txt','w')
res =requests.get('http://www.geog.psu.edu/people/Faculty').text.encode('utf-8')
soup = BeautifulSoup(res,"html.parser")
tableF = soup.select('tbody')[0]
hrefFs = tableF.select('.views-field-path a')
for hrefF in hrefFs:
    name = hrefF.text.encode('utf-8').replace('\n','') #明子
    if True:
        link = hrefF['href'].encode('utf-8')
        resF = requests.get('http://www.geog.psu.edu/'+link).text.encode('utf-8')
        soupF = BeautifulSoup(resF,'html.parser')
        basic = soupF.select('.views-row.views-row-1.views-row-odd.views-row-first.views-row-last')[0]
        print basic
        #print basic
        #title = basic.select('.views-field-phpcode')[0].text.encode('utf-8').strip().replace('\n','/') #職稱
        resField =  basic.select('.views-field-field-research-area-value div')[0].text.encode('utf-8') #研究領域
        intersts = ''
        for interst in basic.select('.views-field-field-t-r-interests-value .field-content div'):
            intersts += interst.text.encode('utf-8')+'/'
        edu= soupF.select('#field_t_r_education ul')[0].text.encode('utf-8').replace('\n','/')
        courN = '' #course
        for course in soupF.select('#field_t_r_courses li'):
            courN += course.text.encode('utf-8')+'/'


        print name, resField , intersts , edu , courN
        print '------------------'
        outFile.write(name+'\t'+resField+'\t'+intersts+'\t'+edu+'\t'+courN+'\n')
        time.sleep(0.2)
outFile.close()

