'''
#-*- coding: utf-8 -*-
import telepot, sys
from telepot.loop import MessageLoop
from urllib import parse
from urllib.request import urlopen
import datetime
import json
#import Private		#API 토큰과 공공데이터포털 API 등을 별도의 py파일로 만들어 두었다.

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == '날씨':     #날씨라는 메시지가 도착했을 때 대답
            bot.sendMessage(chat_id, '맑았으면 좋겠습니다')
        else:                        #그 외에 다른 메시지가 도착했을 때 대답
            bot.sendMessage(chat_id, '무슨 말인지 모르겠군요')

#TOKEN = Private.TOKEN    #Bot API 토큰
TOKEN = "1873396722:AAHsiIpBMSWEJySHxvbZbKPZDHNzVxOWRV0"
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# 프로그램을 계속 돌림
while True:
    input()
'''


    #-*- coding: utf-8 -*-
import telepot, sys
from telepot.loop import MessageLoop
from urllib import parse
from urllib.request import urlopen
import datetime
import json
from urllib.parse import urlencode, unquote
import requests
import json
#import Private

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    now = datetime.datetime.now()
    print(now)
    now_date = now.strftime('%Y%m%d')
    
    print(now_date)
    isitRain = False
    isitSnow = False
    windDirArray = ["북", "북북동", "북동", "동북동", "동", "동남동", "남동", "남남동", "남", "남남서", "남서", "서남서", "서", "서북서", "북서", "북북서", "북"]
    VVV = 0.0
    UUU = 0.0
    windSpd = 0
    fcstTime = 0
    fcstTimeCounter = 0

    now_time = now.strftime('%H')
    print(now_time)
    now_min = now.strftime('%M')
    print(now_min)
    if (int(now_min) >= 30):
        now_min = '30'
    else:
        now_min = '00'
    int_baseTime = int(now_time) - 2
    if(int_baseTime > 0):
        if(int_baseTime % 3 == 1):
            int_baseTime += 1
        elif(int_baseTime % 3 == 2):
            pass
        else:
            int_baseTime += 2
    else:
        int_baseTime = 23

    if(int_baseTime < 10):
        base_time = '0' + str(int_baseTime) + '00'
    else:
        base_time = str(int_baseTime) + '00'

    

    print(base_time)

    completed_message = ""

    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
    queryString = "?" + urlencode(
    {
    "ServiceKey": unquote("nrGO9uiwFI98zVR52RcpZp7O8SA%2ByDp3E8pWfgCnkXt7BaJ4%2FcHeuIDOZluisW6hz1wSFam07fGuIRZmEO6lng%3D%3D"),
    "base_date": now_date,
    "base_time": str(now_time) + now_min,
    "nx": 102, #사상구 괘법동
    "ny": 96,
    "numOfRows": "10",
    "pageNo": 1,
    "dataType": "JSON"
    }
    )
    queryURL = url + queryString
    print(queryURL)
    response = requests.get(queryURL)
    print("=== response json data start ===")
    print(response.text)
    print("=== response json data end ===")
    print()

    r_dict = json.loads(response.text)
    r_response = r_dict.get("response")
    header = r_response.get("header")
    result = header.get("resultMsg")
    print(result)
    if(result == "NO_DATA"):
        completed_message+="정보 업데이트 중입니다.😁\n 잠시 뒤에 이용해주세요!! ㅠ^ㅠ..."
    else: 
        
        r_body = r_response.get("body")
        r_items = r_body.get("items")
        r_item = r_items.get("item")

        result = {}
        for item in r_item:
            if(item.get("category") == "T1H"):
                result = item
                temp = float(result.get("obsrValue"))
                if(temp < 5):
                    var = "완전 추워요!! 바람막이 말고 롱패딩 입어요!!"
                elif(temp < 10):
                    var = "상당히 추워요 ㅠㅠ 바람막이는 필수!!!"
                elif(temp < 20):
                    var = "외투는 꼭 걸치고 밖으로 나오기!!"
                elif(temp < 25):
                    var = "날씨가 너무 좋아요~ 한한 할래요?"
                elif(temp < 30):
                    var = "반팔만 입어야 안더워요! 바람 잘 통하는 옷 입기!!"
                else:
                    var = "너무 너무 더워요,,, 손풍기 꼭 챙기세요!!"
                completed_message +=str(result.get("baseTime")[:-2]+"시 한동대의 기온은 " + result.get("obsrValue") + "C 입니다." + '\n' + var + '\n')
                break
        for item in r_item:
            if(item.get("category") == "RN1"):
                result2 = item
                temp = float(result2.get("obsrValue"))
                if(temp == 0):
                    var = "현재 한동대는 비가 오고 있지 않아요!! ^o^ !!"
                elif(temp < 3):
                    var = "현재 한동대에는 약한 비가 내리고 있어요... 우산 챙기기!!"
                elif(temp < 15):
                    var = "현재 한동대에는 꽤 비가 많이 내리고 있어요... 감기조심 ㅠ^ㅠ.."
                elif(temp < 20):
                    var = "현재 한동대에는 강한 비가 내리고 있습니다... 양말 조심,, 바지 조심 ㅠㅠ"
                elif(temp < 31):
                    var = "현재 한동대에는 매우 매우 강한 비가 내리고 있어요... 우리 살아서 만나요....!!!"
                else:
                    var = "현재 한동대에는 너무너무 많은 비가 내리고 있어요.. 그냥 긱사에 콕 박혀있어요!!!"
                completed_message +=str(result2.get("baseTime")[:-2] +" 시 한동대의 강수량은 " + result2.get("obsrValue") + "mm" + ' 입니다.\n'+var+'\n')
                break
        for item in r_item:
            if(item.get("category") == "REH"):
                result = item
                temp = float(result.get("obsrValue"))
                completed_message +=str(result.get("baseTime")[:-2]+"시 한동대의 습도는 " + result.get("obsrValue") + "% 입니다." + '\n')
                break
        for item in r_item:
            if(item.get("category") == "WSD"):
                result = item
                temp = float(result.get("obsrValue"))
                completed_message +=str(result.get("baseTime")[:-2]+"시 한동대의 풍속은 " + result.get("obsrValue") + "m/s 입니다." + '\n')
                break
        # for item in r_item:
        #     if(item.get("category") == "SKY"):
        #         result = item
        #         temp = float(result.get("obsrValue"))
        #         completed_message +=str(result.get("baseTime")[:-2]+"시 한동대의 습도는 " + result.get("obsrValue") + "% 입니다." + '\n')
        #         break

    url = "http://smart.handong.edu/api/service/menu"
    print(url)
    response = requests.get(url)
    h_dict = json.loads(response.text)
    print(h_dict)
    haksik = h_dict.get("haksik")
    print(haksik)
    if content_type == 'text':
        if msg['text'] == '날씨':
            bot.sendMessage(chat_id, completed_message)
        else:
            bot.sendMessage(chat_id, '무슨 말인지 모르겠군요')

TOKEN = "1873396722:AAHsiIpBMSWEJySHxvbZbKPZDHNzVxOWRV0"
#TOKEN = Private.TOKEN    # 텔레그램으로부터 받은 Bot API 토큰
#안드로이드 외부 편집 테스트

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while True:
    input()