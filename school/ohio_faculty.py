# -*- coding: utf-8 -*-
import requests
from bs4 import *
outFile = open('D:/abroad/courseData/Ohio/faculty.txt','w')
res = requests.get('https://geography.osu.edu/directory').text.encode('utf-8')
soup = BeautifulSoup(res,"html.parser")
rows= soup.select('tbody tr')

for row in rows:
    if len(row.text.encode('utf-8').split('Professor'))>1:
        urlF= 'http://geography.osu.edu/'+row.select('a')[0]['href']
        #每人頁面
        resF =requests.get(urlF)
        soupF= BeautifulSoup(resF.text.encode('utf-8'),"html.parser")
        #開始爬資料
        name = soupF.select('.title')[0].text.replace('\t','').encode('utf-8') #名稱
        print name
        outFile.write(name+'\t')
        content = soupF.select('.fieldset-wrapper')[0]
        title = content.select('.field-item.even')[0].text.strip().replace('\t','').encode('utf-8').replace(',','/')
        print title
        outFile.write(title+'\t')
        position = content.select('.field-item.even')[1].text.strip().replace('\t','').encode('utf-8')
        print position
        outFile.write(position+'\t')

        experts=soupF.select('.field.field-name-field-asc-areas-of-expertise.field-type-text.field-label-above li')
        for expert in experts:
            expertP =expert.text.encode('utf-8').replace('\t','').strip().replace('\n','/')
            print expertP
            outFile.write(expertP+'/')
        outFile.write('\t')


        edus= soupF.select('.field.field-name-field-asc-people-education.field-type-text.field-label-above ul')
        for edu in edus:
            eduP =edu.text.encode('utf-8').replace('\t','').strip().replace('\n','/')
            print eduP
            outFile.write(eduP+'/')
        outFile.write('\t')



        detail = content.select('.field-item.even')[2].text.strip()
        if len(detail.encode('utf-8').split('Interests:'))>1:
            interest = detail.encode('utf-8').split('Interests:')[1].split('Current Research:')
            interestP = interest[0]
            resurch = interest[1].split('Courses Taught:')
            resurchP = resurch[0].strip()
            courses = resurch[1].split('Select Publications:')[0]
            outFile.write(interestP+'\t'+resurchP+'\t'+courses+'\n')
            print interestP,resurchP,courses
        else:
            print 'none' , detail.encode('utf-8') , 'none'
            outFile.write('none'+'\t'+detail.encode('utf-8')+'\t'+'none'+'\n')
        print '---------------'
outFile.close()




