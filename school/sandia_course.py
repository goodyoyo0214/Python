# -*- coding: utf-8 -*-
import requests
from bs4 import *
import time
outFile = open('D:/abroad/courseData/sandia/courseSprin.txt','w')
res = requests.get('https://sunspot.sdsu.edu/schedule/search?mode=search&period=20152&admin_unit=R&abbrev=GEOG&number=&suffix=&courseTitle=&scheduleNumber=&units=&instructor=&facility=&space=&meetingType=&startHours=&startMins=&endHours=&endMins=&remaining_seats_at_least=&ge=&x=18&y=10').text.encode('utf-8')
soup = BeautifulSoup(res, "html.parser")
#print soup
links = soup.select('#bodySearchResults div .sectionFieldCourse.column a')[1:]

for link in links:
    name = link.text.encode('utf-8')
    url = link['href'].encode('utf-8')
    print name
    print 'https://sunspot.sdsu.edu/schedule/'+url
    resP = requests.get('https://sunspot.sdsu.edu/schedule/'+url).text.encode('utf-8')
    soupP = BeautifulSoup(resP,"html.parser")
    table = soupP.select('#sectionDetailTable tr')
    #print table
    title = table[8].select('.sectionDetailContent')[0].text.encode('utf-8').strip().replace('\n',' ').replace('\t', ' ')
    credit = table[4].select('.sectionDetailContent')[0].text.encode('utf-8').strip().replace('\n',' ').replace('\t', ' ')
    teach = table[7].select('.sectionDetailContent .sectionFieldInstructor.column')[0].text.encode('utf-8').strip().replace('\n',' ').replace('\t', ' ')
    dis = table[9].select('.sectionDetailContent')[0].text.encode('utf-8').strip().replace('\n',' ').replace('\t', ' ')
    pre = table[10].select('.sectionDetailContent')[0].text.encode('utf-8').strip().replace('\n',' ').replace('\t', ' ')
    print title,credit,dis,pre,teach
    outFile.write(title+'\t'+credit+'\t'+pre+'\t'+teach+'\t'+dis+'\n')
outFile.close()


