
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

city_id = '1839071' # put cities id you want
api_id = '0548f5ab9366bbb53502f37d6a80e10c' # put your api id
TOKEN = "1773833039:AAFSgXt_7BmiYWCHtQ7DScUo2RPcEHhk_KM" # put your telegram token info
chat_id = 1856753360 # put your chat_id 
                    # you can get chat_id this way >> content_type, chat_type, chat_id = telepot.glance(msg)

weather_condition_dic = {
    "Thunderstorm" : '🌩 천둥번개가',
    "Drizzle" : '🌦 가벼운 비가',
    "Rain" : '☔️ 비가',
    "Snow" : '☃️ 눈이',
    "Mist": '💨 안개가',
    "Smoke": '💨 매연이',
    "Haze": '💨 안개가',
    "Dust": '😷 미세먼지가',
    "Clear": '☀️ 맑은 하늘이',
    "Clouds": '☁️ 구름이'
}
weatherMessage_dict = {
    "Thunderstorm": '오늘 같은 날 밖은 위험에요...⚡️⚡️',
    "Drizzle": '우산 챙기기~ 🌂',
    "Rain":
    '오늘은 우산이 필수!! 친구들한테도 알려주세요!! 🌂',
    "Snow":
    '한동에서의 눈은 참 귀하답니다 눈구경해요!! ☃️',
    "Mist": '오늘같은 날은 안전운전 해야되는거 아시죠?? 🛻',
    "Smoke": '이런 날은 안나가는게 제일 좋아요!',
    "Haze": '오늘같은 날은 안전운전 해야되는거 아시죠?? 🛻',
    "Dust": '미세먼지 너무 싫어요ㅠㅠ 마스크 꼭 쓰기!😷',
    "Clear":
    '오늘은 날씨가 정말 좋아요 연인/친구들과 로잔에서 소풍하는거 어때요?☀️',
    "Clouds": '오늘 같은 꿀꿀한 날에는 맛있는 치킨을 먹어봐요!😊',
}
def handle(msg):
    global flag
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

    completed_message = ""

    if content_type == 'text':
        if msg['text'] in '날씨' or msg['text'] in "한동날씨" or msg['text'] in "한동 날씨":
            url = 'http://api.openweathermap.org/data/2.5/weather?id='+city_id+'&appid='+api_id
            response = requests.get(url)
            print("=== response json data start ===")
            print(response.text)
            print("=== response json data end ===")
            r_dict = json.loads(response.text)
            weather = r_dict.get("weather")
            weather = weather[0]
            weather_1 = weather.get("main")
            weather_2 =weather.get("description")
            weather_info1 = weather_condition_dic[weather_1]
            weather_info2 = weatherMessage_dict[weather_1]
            main = r_dict.get("main")
            temp = main.get("temp") - 273.15
            temp_min = main.get("temp_min") - 273.15
            temp_max = main.get("temp_max") - 273.15
            feel = main.get("feels_like") - 273.15
            humidity = main.get("humidity")
            wind = r_dict.get("wind")
            speed = wind.get("speed")

            temp_int = int(temp)
            temp_var = ""
            if(temp_int < 5):
                temp_var = "❄️바람막이 말고 롱패딩 입어요!!"
            elif(temp_int < 10):
                temp_var = "☃️바람막이는 필수!!!"
            elif(temp_int < 20):
                temp_var = "🌬외투는 꼭 걸치고 밖으로 나오기!!"
            elif(temp_int < 25):
                temp_var = "☀️날씨도 좋으니 한한 할래요?"
            elif(temp_int < 30):
                temp_var = "🔥반팔만 입어야 안더워요! 바람 잘 통하는 옷 입기!!"
            else:
                temp_var = "🔥🔥너무 너무 더워요,,, 손풍기 꼭 챙기세요!!"
            
            wind_var = ""
            if(speed < 4.0):
                wind_var = "😁약한 바람이 불고 있어요. 기분 좋게 바람 맞아봐요 :)"
            elif(speed < 9.0):
                wind_var = "😊약한 강한 바람이 불고 있어요. 조심하세요 :)"
            elif(speed < 14.0):
                wind_var = "😭강한 바람이 불고 있어요. 안다치게 조심하세요 !"
            else:
                wind_var = "☠️매우 강한 바람이 불고 있어요. 오늘 같은 날은 기숙사 밖으로 나가면 위험해요!"
            
            msg0 = "🌈오늘 한동의 기온은 " + "{0:.2f}".format(temp) + "도 이고 날씨는 " + weather_condition_dic[weather_1] +" 있는 날이에요.\n"
            msg1 = "🧚‍♂️자세한 날씨로 체감기온은 " +"{0:.2f}".format(feel) +"도 이고 \n🧚‍♂️오늘 최저 온도는 "+"{0:.2f}".format(temp_min)+"도 이고 \n🧚‍♂️최고 온도는 "+"{0:.2f}".format(temp_max)+" 에요." \
            "\n🧚‍♂️오늘 같은 날은 " + temp_var + '\n'
            msg2 = weatherMessage_dict[weather_1]+'\n'
            msg3 = "💦현재 습도는 " + str(humidity) + "%이고 \n🪁풍속은 " + str(speed)+ "m/s 로 현재 "+wind_var + '\n'
            completed_message += msg0
            completed_message += msg1
            completed_message += msg2
            completed_message += msg3
            bot.sendMessage(chat_id, completed_message)
        elif msg['text'] in '학식' or msg['text'] in '학관' or msg['text'] in '학식메뉴' or msg['text'] in '학식 메뉴' or msg['text'] in '학생 식당':
            url = "http://smart.handong.edu/api/service/menu"
            print(url)
            response = requests.get(url)
            print("ADGASDGAS")
            print(response)
            h_dict = json.loads(response.text)
            #학식
            haksik = h_dict.get("haksik")
            mor = haksik[0].get("menu_kor")
            mor = mor.replace("-원산지: 메뉴게시판 참조-","🍙아침🍙")
            lun = haksik[1].get("menu_kor")
            lun = lun.replace("-원산지: 메뉴게시판 참조-","🥗점심🥗")
            din = haksik[2].get("menu_kor")
            din = din.replace("-원산지: 메뉴게시판 참조","🥘저녁🥘")
            completed_message += "🥗학생식당 메뉴🍱"
            completed_message += '\n\n'
            completed_message += mor
            completed_message += '\n\n'
            completed_message += lun
            completed_message += '\n\n'
            completed_message += din
            completed_message += '\n\n'
            bot.sendMessage(chat_id, completed_message)
            flag = True
        elif msg['text'] in '맘스' or msg['text'] in '맘스키친' or msg['text'] in '맘스 메뉴' or msg['text'] in '맘스키친 메뉴':
            url = "http://smart.handong.edu/api/service/menu"
            print(url)
            response = requests.get(url)
            h_dict = json.loads(response.text)
            print("DAGSDGASD")
            print(h_dict)
            #맘스키친
            moms = h_dict.get("moms")
            mor = moms[0].get("menu_kor")
            mor = "🍙아침🍙\n" + mor
            lun = moms[1].get("menu_kor")
            lun = "🥗점심🥗\n" + lun 
            din = moms[2].get("menu_kor")
            din = "🥘저녁🥘\n" + din

            completed_message += "🥗맘스키친 메뉴🍱"
            completed_message += '\n\n'
            completed_message += mor 
            completed_message += '\n'
            completed_message += lun
            completed_message += '\n'
            completed_message += din
            completed_message += '\n'
            bot.sendMessage(chat_id, completed_message)
            flag = True
        elif msg['text'] in '코로나' or msg['text'] in '확진자' or msg['text'] in '코로나 현황':
            url = "https://api.corona-19.kr/korea/country/new/?serviceKey=OGDPW5zYs62ZHcjpmglT78tkaXLb3Kdfw"
            print(url)
            response = requests.get(url)
            h_dict = json.loads(response.text)
 
            data = []
            data.append(h_dict.get("korea"))
            data.append(h_dict.get("seoul"))
            data.append(h_dict.get("busan"))
            data.append(h_dict.get("daegu"))
            data.append(h_dict.get("incheon"))
            data.append(h_dict.get("gwangju"))
            data.append(h_dict.get("daejeon"))
            data.append(h_dict.get("ulsan"))
            data.append(h_dict.get("sejong"))
            data.append(h_dict.get("gyeonggi"))
            data.append(h_dict.get("gangwon"))
            data.append(h_dict.get("chungbuk"))
            data.append(h_dict.get("chungnam"))
            data.append(h_dict.get("jeonbuk"))
            data.append(h_dict.get("jeonnam"))
            data.append(h_dict.get("gyeongbuk"))
            data.append(h_dict.get("gyeongnam"))
            data.append(h_dict.get("jeju"))
            data.append(h_dict.get("quarantine"))
            completed_message += "👻지역별 코로나 현황😱+\n"

            for i in range(19):
                countryName = '📌' 
                countryName += data[i].get("countryName")
                newCase = data[i].get("newCase")
                newCase += ' 명'
                completed_message += countryName
                completed_message += ' : '
                completed_message += newCase
                completed_message += '\n'
    
            bot.sendMessage(chat_id, completed_message)
            flag = True
        elif msg['text'] in "사용법" or msg['text'] in "사용":
            bot.sendMessage(chat_id, 
            "\n😎SIRLab 한동 챗봇 입니다.🤸‍♀️"\
            "\n😆챗봇 사용법은 다음과 같습니다.😆\n\n"\
            "☀️현재 한동대 날씨가 궁금하면 🤫⁉️\n ☞ 날씨 / 한동날씨\n"\
            "🍱오늘 학식 메뉴가 궁금하면 🤫⁉️\n ☞ 학식 / 학식 메뉴 \n"\
            "🥘오늘 맘스키친 메뉴가 궁금하면 🤫⁉️ \n☞ 맘스 / 맘스 메뉴 \n"\
            "🥶오늘 코로나 바이러스 현황이 궁금하면 🤫⁉️ \n☞ 코로나 / 코로나 현황 \n"\
            )
            flag = True
        elif msg['text'] in "/start":
            pass
        else:
            bot.sendMessage(chat_id, '무슨 말인지 잘 모르겠어요😭\n📌사용법📌 이라고 물어봐주세요‼️')
            flag = True



bot = telepot.Bot(TOKEN)


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
global flag
flag = True
# Keep the program running.
bot.sendMessage(chat_id, 
            "\n😎SIRLab 한동 챗봇 입니다.🤸‍♀️"\
            "\n😆챗봇 사용법은 다음과 같습니다.😆\n\n"\
            "☀️현재 한동대 날씨가 궁금하면 🤫⁉️\n ☞ 날씨 / 한동날씨\n"\
            "🍱오늘 학식 메뉴가 궁금하면 🤫⁉️\n ☞ 학식 / 학식 메뉴 \n"\
            "🥘오늘 맘스키친 메뉴가 궁금하면 🤫⁉️ \n☞ 맘스 / 맘스 메뉴 \n"\
            "🥶오늘 코로나 바이러스 현황이 궁금하면 🤫⁉️ \n☞ 코로나 / 코로나 현황 \n"\
            )
while True:
    input()
        
