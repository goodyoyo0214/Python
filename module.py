#coding:utf-8
import requests
from bs4 import *


#手機型號
MiDic = {1:"Mi_3",2:"MiRed_1s"}
HtcDic={1:"Desire601",2:"Desire310",3:"One_m8",4:"E8",5:"Desire610",6:"Butterfly2",7:"ButterflyS"}
SamsungDic = {1:"Note3_lte",2:"Core_Lite",3:"KZoom",4:"Core_lte",5:"S5",6:"Note3_Neo",7:"Grand_Neo",8:"Grand2",9:"J"}
SonyDic ={1:"M2",2:"T3",3:"Z1_lte",4:"Z2",5:"E1",6:"L",7:"Z1C"}
LgDic={1:"GPro2",2:"G3",3:"G2_mini",4:"GFlex"}
AsusDic = {1:"Zenfone6",2:"Zenfone5",3:"Zenfone4",4:"PadFoneS",5:"padfone_Infinity"}

#公司名稱
firmDic ={1:"Htc", 2:"Sony", 3:"Samsung", 4:"Mi", 5:"Lg", 6:"Asus"}

#機型的特色的要print的東西
dicSpec = {"module":"N/A","size":"N/A","weight":"0","sim":"N/A","ipx":"N/A","cpu":"N/A","ram":"0","rom":"0","card":"N/A","system":"N/A","dual_standby":"N/A","multimedia":"N/A","sensor_extra":"N/A","battery":"N/A","color":"N/A","special":"N/A","mainCam":"0","frontCam":"0","camFunc":"N/A","screenSize":"0","screenReso":"N/A","screenSpac":"N/A","network":"N/A"}

#開檔案
output = open("E:/project/projectData/etl/module/module.txt","w")

'''------------------------------'''
#設定公司名稱
firm = firmDic[1]
#設定型號
module = HtcDic[7] #型號
if module != "":
    dicSpec["module"] = module

html = requests.get("http://www.eprice.com.tw/mobile/intro/c01-p4788-htc-butterfly-s/")
html.encoding="utf-8"
'''------------------------------'''
soup = BeautifulSoup(html.text)
table = soup.select("ul.featurelist")[0]



size = ''.join(table.select(".size")[0].text.split()).encode("utf-8") #大小
if size != "":
    dicSpec["size"] = size
weight =''.join(table.select(".weight")[0].text.split()).split("g")[0].encode("utf-8") #重量
if weight != "":
    dicSpec["weight"] = weight
sim=''.join(table.select(".sim")[0].text.split()).encode("utf-8") #sim卡規格
if sim != "":
    dicSpec["sim"] = sim
ipx =''.join(table.select(".ipx")[0].text.split()).encode("utf-8") #防水防塵
if ipx == "無":
    dicSpec["ipx"] = "無防水防塵"
elif ipx != "":
    dicSpec["ipx"] = ipx
cpu = table.select(".cpu")[0].text.strip().encode("utf-8") #cpu
if cpu != "":
    dicSpec["cpu"] = cpu
ram = ''.join(table.select(".ram1")[0].text.split()).split("GB")[0].encode("utf-8") #ram大小
if ram != "":
    dicSpec["ram"] = ram
rom = ''.join(table.select(".rom")[0].text.split()).split("GB")[0].encode("utf-8") #rom大小
if rom != "":
    dicSpec["rom"] = rom
card =''.join(table.select(".card")[0].text.split()).encode("utf-8") #記憶卡
if card != "":
    dicSpec["card"] = card
system =''.join(table.select(".system")[0].text.split()).encode("utf-8") #通信協定
if system != "":
    dicSpec["system"] = system
dual_standby =''.join(table.select(".dual_standby")[0].text.split()).encode("utf-8") #雙卡雙待
if dual_standby == "有":
    dicSpec["dual_standby"] = "雙卡雙待"
multimedia ='|'.join([''.join(i.text.split()) for i in table.select(".multimedia li")[0::2]]).encode("utf-8") #多媒體
if multimedia != "":
    dicSpec["multimedia"] = multimedia
sensor_extra =''.join(table.select(".sensor_extra")[0].text.split()).encode("utf-8") #感應器
if sensor_extra != "":
    dicSpec["sensor_extra"] = sensor_extra
battery=''.join(str(table.select(".battery")).split(">")[1].split("<")[0].strip().split()) #電池內容
if battery != "":
    dicSpec["battery"] = battery
color =''.join(table.select(".color")[0].text.split()).encode("utf-8") #顏色
if color != "":
    dicSpec["color"] = color
special ='|'.join([''.join(i.text.split()) for i in table.select(".special li")[0::2]]).encode("utf-8")#其他功能
if special != "":
    dicSpec["special"] = special

#檢查相機內容用
dicCamera = {"LED閃光燈":0,"自動對焦":0}
camera =[''.join(i.text.split()) for i in table.select(".camera li")[0::2]]
mainCam = camera[0].encode("utf-8").split("\xe4\xb8\xbb\xe7\x9b\xb8\xe6\xa9\x9f")[1].split("\xe8\x90")[0].encode("utf-8") #主相機畫素
if mainCam != "":
    dicSpec["mainCam"] = mainCam

frontCam = camera[1].encode("utf-8").split("\xe5\x89\x8d\xe7\x9b\xb8\xe6\xa9\x9f")[1].split("\xe8\x90")[0].encode("utf-8") #相機畫素
if frontCam != "":
    dicSpec["frontCam"] = frontCam

camFunc = '|'.join(camera[2:]).encode("utf-8") #相機其他功能
if camFunc != "":
    dicSpec["camFunc"] = camFunc

#螢幕
screen=table.select(".screen li")[0].text.split(u"\u540b") #螢幕的解果
screenSize = screen[0].encode("utf-8")#螢幕大小
if screenSize != "":
    dicSpec["screenSize"] = screenSize
screenReso= screen[1].encode("utf-8")#解析度
if screenReso != "":
    dicSpec["screenReso"] = screenReso
screenSpac='|'.join([''.join(i.text.split()) for i in table.select(".screen li")[2::2]]).encode("utf-8")#剩下的螢幕資訊
if screenSpac != "":
    dicSpec["screenSpac"] = screenSpac
#網路與連線
netList = []
for ele in str(table.select(".network ul")[0]).split("<li>")[1:]:
    netList.append(''.join(ele.split("<")[0].split()))
network = '|'.join(netList)#網路與連線的結果
if network != "":
    dicSpec["network"] = network


print firm+"\t"+dicSpec["module"]+"\t"+dicSpec["size"]+"\t"+dicSpec["weight"]+"\t"+dicSpec["screenSize"]+"\t"+dicSpec["screenReso"]+"\t"+dicSpec["screenSpac"]+"\t"+"\t"+dicSpec["sim"]+"\t"+dicSpec["ipx"]+"\t"+dicSpec["cpu"]+"\t"+dicSpec["ram"]+"\t"+dicSpec["rom"]+"\t"+dicSpec["card"]+"\t"+dicSpec["system"]+"\t"+dicSpec["dual_standby"]+"\t"+dicSpec["mainCam"]+"\t"+dicSpec["frontCam"]+"\t"+dicSpec["camFunc"]+"\t"+dicSpec["multimedia"]+"\t"+dicSpec["network"]+"\t"+dicSpec["sensor_extra"]+"\t"+dicSpec["battery"]+"\t"+dicSpec["color"]+"\t"+dicSpec["special"]
output.write(firm+"\t"+dicSpec["module"]+"\t"+dicSpec["size"]+"\t"+dicSpec["weight"]+"\t"+dicSpec["screenSize"]+"\t"+dicSpec["screenReso"]+"\t"+dicSpec["screenSpac"]+"\t"+dicSpec["sim"]+"\t"+dicSpec["ipx"]+"\t"+dicSpec["cpu"]+"\t"+dicSpec["ram"]+"\t"+dicSpec["rom"]+"\t"+dicSpec["card"]+"\t"+dicSpec["system"]+"\t"+dicSpec["dual_standby"]+"\t"+dicSpec["mainCam"]+"\t"+dicSpec["frontCam"]+"\t"+dicSpec["camFunc"]+"\t"+dicSpec["multimedia"]+"\t"+dicSpec["network"]+"\t"+dicSpec["sensor_extra"]+"\t"+dicSpec["battery"]+"\t"+dicSpec["color"]+"\t"+dicSpec["special"]+"\n")
'''
print "module:"+module+"\tsize:"+size+"\tweight:"+weight+"\tsim:"+sim+"\tipx:"+ipx+"\tcpu:"+cpu+"\tram:"+ram1+"\trom:"+rom+"\tcard:"+card+"\tsystem:"+system+"\tdual_standby:"+dual_standby+"\tmainCam:"+mainCam+"\tfrontCam:"+frontCam+"\tcamFunc:"+camFunc+"\tmultimedia:"+multimedia+"\tnetwork:"+network+"\tsensor_extra:"+sensor_extra+"\tbattery:"+battery+"\tcolor:"+color+"\tspecial:"+special
'''
'''
print module+"\t"+size+"\t"+weight+"\t"+sim+"\t"+ipx+"\t"+cpu+"\t"+ram1+"\t"+rom+"\t"+card+"\t"+system+"\t"+dual_standby+"\t"+mainCam+"\t"+frontCam+"\t"+camFunc+"\t"+multimedia+"\t"+network+"\t"+sensor_extra+"\t"+battery+"\t"+color+"\t"+special
'''
output.close()

