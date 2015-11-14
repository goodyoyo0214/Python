# -*- coding: utf-8 -*-
import codecs
#處理編碼的套件
import operator
#處理字典檔排序的套件
import time

cutlist = "<>/:：;；,、＂’，.。！？｢\"\'\\\n\r《》“”!@#$%^&*()".decode("utf-8")

start = time.time()
#text_new =""

def cutSentence(text_path, keywords): ##放入原始文章路徑, 增加斷詞的list
    text = codecs.open(text_path,"r","utf-8")   #開檔 #讀取存成TXT檔的文字，讀入後統一轉成UTF-8格式
    sentence = ""
    textList = []

    for line in text.readlines():
        line = line.strip() ##清除空白

        for keyword in keywords:  #清除關鍵字
            line = "".join(line.split(keyword))

        for word in line:
            if word not in cutlist: #如果文字不是標點符號，就把字加到句子中
                sentence += word
                #print sentence
            else:
                textList.append(sentence) #如果遇到標點符號，把句子加到 text list中
                sentence = ""
                #print textList
    return textList#傳回一個文字陣列

def ngram(textLists,n,minFreq): #第一個參數放處理好的文章(LIST檔，utf-8編碼)，第二個參數放字詞的長度單位，第三個參數放至少要幾次以上

    words=[]     #存放擷取出來的字詞
    words_freq={}#存放字詞:計算個數
    result= []
    for textList in textLists:
        for w in range(len(textList)-(n-1)): #要讀取的長度隨字詞長度改變
            words.append(textList[w:w+n])    #抓取長度w-(n-1)的字串

    for word in words:
        if word not in words_freq:               #如果這個字詞還沒有被放在字典檔中
            words_freq[word] = words.count(word) #就開一個新的字詞，裡面放入字詞計算的頻次

    words_freq = sorted(words_freq.iteritems(),key=operator.itemgetter(1),reverse=True) #change words_freq from dict to list

    for word in words_freq:
        if word[1] >= minFreq:
            result.append(word)

    return result ##回傳一個陣列[詞,頻次]

def longTermPriority(path, maxTermLength, minFreq):
    longTerms=[]          #長詞
    longTermsFreq=[]      #長詞+次數分配

    for i in range(maxTermLength,1,-1):
        text_list = cutSentence(path,longTerms)
        #print len(text_list)
        words_freq = ngram(text_list,i, minFreq)
        #print i


        for word_freq in words_freq:
            longTerms.append(word_freq[0])
            #print word_freq[0]
            longTermsFreq.append(word_freq)
            #print word_freq

    return longTermsFreq
'''                                1.檔案路徑                                           2.最多幾個字'''
longTermFreq = longTermPriority("G:/OneDrive/ETL/downloadFile/testAll/Gps.txt",4,3) ##最長詞5個字、出現頻次3次以上

outPut = open("G:/OneDrive/ETL/downloadFile/testAll/GpsCount.txt",'w')#寫出去的檔案位置
for i in longTermFreq:
    outPut.write(str(i[0].encode('utf-8'))+'\t'+str(i[1])+'\n')
    print str(i[0].encode('utf-8'))+'\t'+str(i[1])
outPut.close()
end = time.time()
count = start-end
print count