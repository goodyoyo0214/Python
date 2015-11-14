# coding: utf-8

import requests
from bs4 import *

url ='http://www.buffalo.edu/cas/geography/faculty/faculty_directory.html'
outFile=open('D:/abroad/courseData/Buffalo/buff_facuty.txt','w')

res=requests.get('http://www.buffalo.edu/cas/geography/faculty/faculty_directory.html')
soup=BeautifulSoup(res.text.encode('utf-8'),"html.parser")
links=soup.select('.staffdirectory.imagebase.section .staff_name_bolded a')


for link in links[:-3]:
    url_t='http://www.buffalo.edu/'+link['href']
    #print(url_t.encode('utf-8'))
    res_t=requests.get(url_t)
    soupT=BeautifulSoup(res_t.text.encode('utf-8'),"html.parser")
    title = soupT.select('.par.parsys .title.section')
    content = soupT.select('.par.parsys .text.parbase.section')
    for i in range(0,3):
        #name+detail
        if i==0:
            titleP = title[i].text.encode('utf-8')
            outFile.write(titleP.strip()+'\t')
            print titleP
            # content1的內容
            if len(content[i].select('p'))>3:
                contentP =content[i].select('p')[0].text.encode('utf-8').replace('\n','|')+'|'+content[i].select('p')[1].text.encode('utf-8').replace('\n','|')
                print contentP
                outFile.write(contentP.strip()+'\t')
            else:
                contentP = content[i].select('p')[0].text.encode('utf-8').replace('\n','|')
                print contentP
                outFile.write(contentP.strip()+'\t')
            print '-----------'

        # interest
        if i==1:
            titleP = title[i].text.encode('utf-8')
            print titleP
            contentP = content[i].select('p')[0].text.encode('utf-8').replace('\n','')
            print contentP
            print '----------------'
            outFile.write(contentP.strip()+'\t')
        #course
        if i==2:
            titleP = title[i].text.encode('utf-8')
            print titleP
            contentP = content[i].select('p')
            for course in contentP:
                courseP=course.text.encode('utf-8').strip().replace('\n','')
                print courseP.strip()+'|'
                outFile.write(courseP.strip()+'|')
    outFile.write('\n')
    print '**************'
outFile.close()

