
# coding: utf-8

# In[11]:

# -*- coding: <encoding name>-*-

import requests,time,re
from bs4 import BeautifulSoup
format_link = 'https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=10&hl=zh_TW&prettyPrint=false&source=gcsc&gss=.tw&sig=23952f7483f1bca4119a89c020d13def&start={0}&cx=partner-pub-2614970773838551:94vq76eazbo&q={1}&googlehost=www.google.com.tw&callback=google.search.Search.apiary78&nocache=1430127546425'
outTitle = open('eprice/mi3/totaltopic.txt','w')# 另存的標題檔,改為自己的存放方式

for k in range(1,11):
    #print "----------------------------------------------------------------"
    for i in range(1,11):
        outPut = open('eprice/mi3/{}.txt'.format(str(int(k-1)*10+int(i))),'w')#1.修改此處的目錄,改為自己的存放方式
        res = requests.get(format_link.format(str(int(k-1)*10),'%22%E7%B4%85%E7%B1%B31S%22%20%7C%20%22%E7%B4%85%E7%B1%B31s%22'))#2.修改成自己的手機型號
                                                                # Network 裡 Script 中 &q= 與 &googlehost 之間的東西
        #res.encoding='utf-8'
        #print  res.text
        m = res.text.split(',\"unescapedUrl\":\"')[i] #切出每篇 url
        n = m.split('\",\"')[0] # n=每篇文章的url (unicode)
        #print n
        #print len(n.split("intro"))
       
        if len(n.split("/talk/"))>1: #去掉第一篇介紹文 避免他抓不到而error
            
            article_id = n.split('/talk/')[1].split('/1/')[0].split('/') 
            #print article_id[0]+'\t'+article_id[1]
            #以上為手機的分類ID與文章的ID
            #print page_url
            res_link = requests.get(n)
            res_link.encoding='utf-8'
            #print 'page'+page

            fsoup = BeautifulSoup(res_link.text) #為了找出 MaxPage

            if len(fsoup.select('.title'))>0: #內文裡的標題文字
                topic = fsoup.select('.title')[0]
                #topic.encoding = 'utf-8'
                #print topic.text
                outPut.write('TITLE'+'\t'+topic.text.encode("UTF-8")+'\n')
                outTitle.write(format(str(int(k-1)*10+int(i)))+'\t'+article_id[0].encode('utf-8')+'\t'+article_id[1].encode('utf-8')+'\t'+n.encode('utf-8')+'\t'+topic.text.encode('utf-8')+'\n')
                #以上為寫入標題
                #outTitle.write(n) #url寫入 TXT

                artical_url = n.split('/1/')[0] #切出頁數之前的url

                if len(fsoup.select('.pagelink a'))>0: 
                    maxpage = fsoup.select('.pagelink')[0].findAll('a')[-2].text.encode('utf-8')
                    if len(maxpage.split("..."))>1:
                        maxpage = int(maxpage.split('...')[1]) #頁數超出10頁
                    #找出最大頁數
                else:
                    maxpage = str(1) #若只有一頁 maxpage給1
                #print maxpage    
                
                    #最大頁數
                    #print maxpage
                    #print artical_url
                for page in range(1,int(maxpage)+1):

                    page_url = artical_url.encode('utf-8')+'/'+str(page)+'/'
                    #print page_url
                    content_link = requests.get(page_url)
                    content_link.encoding = 'utf-8'

                    soup = BeautifulSoup(content_link.text)
                    #print soup.text

                    contents = soup.findAll("dd",{"class":"enabled"})
                    #print contents
                    #print "_____________________________________________________"
                    for content in contents: #每一樓
                        #print content
                        #print content.text
                       
                        name = content.findAll('a',{"class":"nickname"})[0] #暱稱
                        nickname = name.text
                        nameid = str(name['href']).split('?u=')[1] #id
                        #print nicknameid
                        #暱稱 id
                        floor = content.findAll('em',{"class":"floor"})[0].text
                        #print floor
                        #幾樓
                        date = content.findAll('em',{"class":"date"})[0].text.encode('utf-8').split('發表於 ')[1]
                        #print date
                        #發表日期
                        
                        if len(content.select('.quote'))>0:
                            #print "if"
                            quoteto = content.select('.comment')[0].select('.quote')[0].decompose()
                            quoteto_split = content.select('.comment')[0].text
                            commentSplite = ''.join(quoteto_split.split())
                            print article_id[0].encode('utf-8')+'\t'+article_id[1].encode('utf-8')+'\t'+floor.encode('utf-8')+'\t'+date.encode('utf-8')+'\t'+nameid.encode('utf-8')+'\t'+nickname.encode('utf-8')+'\t'+commentSplite.encode('utf-8')+'\n'
                            
                            #print quoteto_split.text
                        #去掉引用
                            #outPut.write(article_id[0].encode('utf-8')+'\t'+article_id[1].encode('utf-8')+'\t'+floor.encode('utf-8')+'\t'+date.encode('utf-8')+'\t'+nameid.encode('utf-8')+'\t'+nickname.encode('utf-8')+'\t'+quoteto_split.encode('utf-8')+'\n')
                        else:
                            #print "else"
                            word = content.select('.user-comment-block')[0].select('.comment')[0].text #每一篇的第一則留言
                            comment = ''.join(word.split()) #融合成一行
                            print article_id[0].encode('utf-8')+'\t'+article_id[1].encode('utf-8')+'\t'+floor.encode('utf-8')+'\t'+date.encode('utf-8')+'\t'+nameid.encode('utf-8')+'\t'+nickname.encode('utf-8')+'\t'+comment.encode('utf-8')+'\n'
        
                        #內文
                        #outPut.write(article_id[0].encode('utf-8')+'\t'+article_id[1].encode('utf-8')+'\t'+floor.encode('utf-8')+'\t'+date.encode('utf-8')+'\t'+nameid.encode('utf-8')+'\t'+nickname.encode('utf-8')+'\t'+comment.encode('utf-8')+'\n')
                        
                        #fb_comment = soup.select('.fb-comment-block')[0]
                        #fb_nickname = fb_comment.select('.profilename')
                        #fb_posttext = fb_comment.select('postText')
                        #print fb_comment#+'\t'+fb_nickname+'\t'+fb_posttext
                        #print fb_nickname
                        #fb留言

                        #print type(floor),type(nameid),type(nickname),type(comment)
                        time.sleep(0.1)
                        # print quoteto
                        #print content[0].text

                        #rint content[1].text

                        #print ''.join(content.split())
                        #outPut.write(content.text.encode('utf-8')+'\n')

    outPut.close()
outTitle.close()


