# coding: utf-8

import requests
from bs4 import *
outUC=open('D:/abroad/courseData/UCSB_course.txt','w')
url = 'https://my.sa.ucsb.edu/catalog/Current/CollegesDepartments/ls-intro/geog.aspx?DeptTab=Courses' #網頁URL

'''----開始爬蟲-----'''
res = requests.get(url)
#print res.text.encode('utf-8')
soup = BeautifulSoup(res.text.encode('utf-8'),'html.parser')

'''---------Lower Division----------'''
print 'Lower Division'
courseFs=soup.select('#ctl00_ctl00_ContentPlaceHolder1_ctl00_divLowerDivision .CourseDisplay ')
for courseF in courseFs[1:]:
    outUC.write('Lower Division\t')
    #print courseF
    cName=''.join(courseF.select('b')[0].text.encode('utf-8').split()) #course_name
    outUC.write(cName+'\t')
    print cName
    contents= courseF.select('div div')
    teacher =''.join(contents[0].select('span')[0].text.encode('utf-8').split()) #teacher
    print teacher
    outUC.write(teacher+'\t')
    #inrollment data
    if len(contents[0].select('strong'))>0:
        enroll_data=contents[0].select('i')[0].text.encode('utf-8')
        prerequisite=enroll_data.split('Prerequisite:')
        recon_Pre=enroll_data.split('Preparation:')
        enril_com=enroll_data.split('Enrollment Comments:')
        if len(prerequisite)>1:
            Prerequisite=''.join(prerequisite[1].split('Recommended')[0].split('Enrollment Comments:')[0].split())
            print 'Prerequisite: '+Prerequisite
            outUC.write(Prerequisite+'\t')
        else:
            print 'Prerequisite:'+' None'
            outUC.write('None'+'\t')

        if len(recon_Pre)>1:
            recPrep=''.join(recon_Pre[1].split('Enrollment Comments')[0].split())
            print 'Recommended Preparation: '+recPrep
            outUC.write(recPrep+'\t')
        else:
            print 'Recommended Preparation:'+' None'
            outUC.write('None'+'\t')

        if len(enril_com)>1:
            enroCom=''.join(enril_com[1].split())
            print 'Enrollment Comments: '+enroCom
            outUC.write(enroCom+'\t')
        else:
            print 'Enrollment Comments:'+' None'
            outUC.write('None'+'\t')

    else:
        print 'Prerequisite: None \nRecommended Preparation: None \nEnrollment Comments: None'
        outUC.write('None'+'\t'+'None'+'\t'+'None'+'\t')
    '''
    if len(contents[0].select('strong'))>0:
        print ''.join(contents[0].select('i div')[0].text.encode('utf-8').split(':')[1].split()) #enrollment
    else:
        print 'No enrollment'
    '''
    discripsion=contents[-1].text.encode('utf-8').strip() #discripsion
    print discripsion
    outUC.write(discripsion+'\n')
    print '---------------'

'''---------Upper Division---------'''
print 'Upper Division'
courseFs=soup.select('#ctl00_ctl00_ContentPlaceHolder1_ctl00_divUpperDivision .CourseDisplay ')
for courseF in courseFs:
    outUC.write('Upper Division\t')
    cName=''.join(courseF.select('b')[0].text.encode('utf-8').split()) #course_name
    print cName
    outUC.write(cName+'\t')

    contents= courseF.select('div')
    teacher=''.join(contents[0].select('span')[0].text.encode('utf-8').split()) #teacher
    print teacher
    outUC.write(teacher+'\t')
    #enroll data
    if len(contents[0].select('strong'))>0:
        enroll_data=contents[0].select('i')[0].text.encode('utf-8')
        prerequisite=enroll_data.split('Prerequisite:')
        recon_Pre=enroll_data.split('Preparation:')
        enril_com=enroll_data.split('Enrollment Comments:')
        if len(prerequisite)>1:
            Prerequisite=''.join(prerequisite[1].split('Recommended')[0].split('Enrollment Comments:')[0].split())
            print 'Prerequisite: '+Prerequisite
            outUC.write(Prerequisite+'\t')
        else:
            print 'Prerequisite:'+' None'
            outUC.write('None'+'\t')

        if len(recon_Pre)>1:
            recPrep=''.join(recon_Pre[1].split('Enrollment Comments')[0].split())
            print 'Recommended Preparation: '+recPrep
            outUC.write(recPrep+'\t')
        else:
            print 'Recommended Preparation:'+' None'
            outUC.write('None'+'\t')

        if len(enril_com)>1:
            enroCom=''.join(enril_com[1].split())
            print 'Enrollment Comments: '+enroCom
            outUC.write(enroCom+'\t')
        else:
            print 'Enrollment Comments:'+' None'
            outUC.write('None'+'\t')

    else:
        print 'Prerequisite: None \nRecommended Preparation: None \nEnrollment Comments: None'
        outUC.write('None'+'\t'+'None'+'\t'+'None'+'\t')
    discrip=contents[-1].text.encode('utf-8').strip() #discripsion
    outUC.write(discrip+'\n')
    print '---------------'

'''-------Graduate Division--------'''
print 'Graduate Division'
courseFs=soup.select('#ctl00_ctl00_ContentPlaceHolder1_ctl00_divGrad .CourseDisplay ')
for courseF in courseFs:
    cName=''.join(courseF.select('b')[0].text.encode('utf-8').split()) #course_name
    outUC.write('Graduate Division\t')
    print cName
    outUC.write(cName+'\t')
    contents= courseF.select('div')
    teacher=''.join(contents[0].select('span')[0].text.encode('utf-8').split()) #teacher
    print teacher
    outUC.write(teacher+'\t')
    #enroll data
    if len(contents[0].select('strong'))>0:
        enroll_data=contents[0].select('i')[0].text.encode('utf-8')
        prerequisite=enroll_data.split('Prerequisite:')
        recon_Pre=enroll_data.split('Preparation:')
        enril_com=enroll_data.split('Enrollment Comments:')
        if len(prerequisite)>1:
            Prerequisite=''.join(prerequisite[1].split('Recommended')[0].split('Enrollment Comments:')[0].split())
            print 'Prerequisite: '+Prerequisite
            outUC.write(Prerequisite+'\t')
        else:
            print 'Prerequisite:'+' None'
            outUC.write('None'+'\t')

        if len(recon_Pre)>1:
            recPrep=''.join(recon_Pre[1].split('Enrollment Comments')[0].split())
            print 'Recommended Preparation: '+recPrep
            outUC.write(recPrep+'\t')
        else:
            print 'Recommended Preparation:'+' None'
            outUC.write('None'+'\t')

        if len(enril_com)>1:
            enroCom=''.join(enril_com[1].split())
            print 'Enrollment Comments: '+enroCom
            outUC.write(enroCom+'\t')
        else:
            print 'Enrollment Comments:'+' None'
            outUC.write('None'+'\t')
    else:
        print 'Prerequisite: None \nRecommended Preparation: None \nEnrollment Comments: None'
        outUC.write('None'+'\t'+'None'+'\t'+'None'+'\t')

    discrip=contents[-1].text.encode('utf-8').strip() #discripsion
    print discrip
    outUC.write(discrip+'\n')
    print '---------------'
