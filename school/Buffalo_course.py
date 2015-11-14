# coding: utf-8

import requests
from bs4 import *

url = 'http://www.buffalo.edu/cas/geography/graduate-program/course-descriptions.html#title_32'
outTitle= open('D:/abroad/courseData/Buffalo/buff_corse_title.txt','w')
outCon =open('D:/abroad/courseData/Buffalo/buff_corse_content.txt','w')

res = requests.get(url)
soup =BeautifulSoup(res.text.encode('utf-8'),"html.parser")
titles = soup.select('.title.section')
for title in titles[1:]:
    tilPrin=title.text.encode('utf-8')

    if len(tilPrin.split('('))>1:
        credit=tilPrin.split('(')[1].split(')')[0].encode('utf-8')
        name=tilPrin.split('(')[0].encode('utf-8')
        print credit
        print name
        outTitle.write(name+'|'+credit+'\n')
    else:
        outTitle.write(tilPrin+'0\n')
contents = soup.select('.text.parbase.section')
for content in contents[1:]:
    content = content.text.encode('utf-8')
    #print content
    pre=content.split('Prerequisites:')
    if len(pre)>1:
        yPre=pre[1].split('-')[0]
        yCon=pre[1].split('-')[1]
        print 'Prerequisites:'+yPre
        print '---'
        print yCon
        outCon.write(pre[1].split('-')[0]+'|'+pre[1].split('-')[1].replace('\n',''))
    else:
        print 'Prerequisites:'+'None'
        print content
        outCon.write('None |'+content.replace('\n',''))
    outCon.write('\n')
    print '-------------'
outCon.close()
outTitle.close()