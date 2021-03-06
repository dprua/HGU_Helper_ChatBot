
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
    "Thunderstorm" : 'π© μ²λ₯λ²κ°κ°',
    "Drizzle" : 'π¦ κ°λ²Όμ΄ λΉκ°',
    "Rain" : 'βοΈ λΉκ°',
    "Snow" : 'βοΈ λμ΄',
    "Mist": 'π¨ μκ°κ°',
    "Smoke": 'π¨ λ§€μ°μ΄',
    "Haze": 'π¨ μκ°κ°',
    "Dust": 'π· λ―ΈμΈλ¨Όμ§κ°',
    "Clear": 'βοΈ λ§μ νλμ΄',
    "Clouds": 'βοΈ κ΅¬λ¦μ΄'
}
weatherMessage_dict = {
    "Thunderstorm": 'μ€λ κ°μ λ  λ°μ μνμμ...β‘οΈβ‘οΈ',
    "Drizzle": 'μ°μ° μ±κΈ°κΈ°~ π',
    "Rain":
    'μ€λμ μ°μ°μ΄ νμ!! μΉκ΅¬λ€ννλ μλ €μ£ΌμΈμ!! π',
    "Snow":
    'νλμμμ λμ μ°Έ κ·νλ΅λλ€ λκ΅¬κ²½ν΄μ!! βοΈ',
    "Mist": 'μ€λκ°μ λ μ μμ μ΄μ  ν΄μΌλλκ±° μμμ£ ?? π»',
    "Smoke": 'μ΄λ° λ μ μλκ°λκ² μ μΌ μ’μμ!',
    "Haze": 'μ€λκ°μ λ μ μμ μ΄μ  ν΄μΌλλκ±° μμμ£ ?? π»',
    "Dust": 'λ―ΈμΈλ¨Όμ§ λλ¬΄ μ«μ΄μγ γ  λ§μ€ν¬ κΌ­ μ°κΈ°!π·',
    "Clear":
    'μ€λμ λ μ¨κ° μ λ§ μ’μμ μ°μΈ/μΉκ΅¬λ€κ³Ό λ‘μμμ μννλκ±° μ΄λμ?βοΈ',
    "Clouds": 'μ€λ κ°μ κΏκΏν λ μλ λ§μλ μΉν¨μ λ¨Ήμ΄λ΄μ!π',
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
    windDirArray = ["λΆ", "λΆλΆλ", "λΆλ", "λλΆλ", "λ", "λλ¨λ", "λ¨λ", "λ¨λ¨λ", "λ¨", "λ¨λ¨μ", "λ¨μ", "μλ¨μ", "μ", "μλΆμ", "λΆμ", "λΆλΆμ", "λΆ"]
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
        if msg['text'] in 'λ μ¨' or msg['text'] in "νλλ μ¨" or msg['text'] in "νλ λ μ¨":
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
                temp_var = "βοΈλ°λλ§μ΄ λ§κ³  λ‘±ν¨λ© μμ΄μ!!"
            elif(temp_int < 10):
                temp_var = "βοΈλ°λλ§μ΄λ νμ!!!"
            elif(temp_int < 20):
                temp_var = "π¬μΈν¬λ κΌ­ κ±ΈμΉκ³  λ°μΌλ‘ λμ€κΈ°!!"
            elif(temp_int < 25):
                temp_var = "βοΈλ μ¨λ μ’μΌλ νν ν λμ?"
            elif(temp_int < 30):
                temp_var = "π₯λ°νλ§ μμ΄μΌ μλμμ! λ°λ μ ν΅νλ μ· μκΈ°!!"
            else:
                temp_var = "π₯π₯λλ¬΄ λλ¬΄ λμμ,,, μνκΈ° κΌ­ μ±κΈ°μΈμ!!"
            
            wind_var = ""
            if(speed < 4.0):
                wind_var = "πμ½ν λ°λμ΄ λΆκ³  μμ΄μ. κΈ°λΆ μ’κ² λ°λ λ§μλ΄μ :)"
            elif(speed < 9.0):
                wind_var = "πμ½ν κ°ν λ°λμ΄ λΆκ³  μμ΄μ. μ‘°μ¬νμΈμ :)"
            elif(speed < 14.0):
                wind_var = "π­κ°ν λ°λμ΄ λΆκ³  μμ΄μ. μλ€μΉκ² μ‘°μ¬νμΈμ !"
            else:
                wind_var = "β οΈλ§€μ° κ°ν λ°λμ΄ λΆκ³  μμ΄μ. μ€λ κ°μ λ μ κΈ°μμ¬ λ°μΌλ‘ λκ°λ©΄ μνν΄μ!"
            
            msg0 = "πμ€λ νλμ κΈ°μ¨μ " + "{0:.2f}".format(temp) + "λ μ΄κ³  λ μ¨λ " + weather_condition_dic[weather_1] +" μλ λ μ΄μμ.\n"
            msg1 = "π§ββοΈμμΈν λ μ¨λ‘ μ²΄κ°κΈ°μ¨μ " +"{0:.2f}".format(feel) +"λ μ΄κ³  \nπ§ββοΈμ€λ μ΅μ  μ¨λλ "+"{0:.2f}".format(temp_min)+"λ μ΄κ³  \nπ§ββοΈμ΅κ³  μ¨λλ "+"{0:.2f}".format(temp_max)+" μμ." \
            "\nπ§ββοΈμ€λ κ°μ λ μ " + temp_var + '\n'
            msg2 = weatherMessage_dict[weather_1]+'\n'
            msg3 = "π¦νμ¬ μ΅λλ " + str(humidity) + "%μ΄κ³  \nπͺνμμ " + str(speed)+ "m/s λ‘ νμ¬ "+wind_var + '\n'
            completed_message += msg0
            completed_message += msg1
            completed_message += msg2
            completed_message += msg3
            bot.sendMessage(chat_id, completed_message)
        elif msg['text'] in 'νμ' or msg['text'] in 'νκ΄' or msg['text'] in 'νμλ©λ΄' or msg['text'] in 'νμ λ©λ΄' or msg['text'] in 'νμ μλΉ':
            url = "http://smart.handong.edu/api/service/menu"
            print(url)
            response = requests.get(url)
            print("ADGASDGAS")
            print(response)
            h_dict = json.loads(response.text)
            #νμ
            haksik = h_dict.get("haksik")
            mor = haksik[0].get("menu_kor")
            mor = mor.replace("-μμ°μ§: λ©λ΄κ²μν μ°Έμ‘°-","πμμΉ¨π")
            lun = haksik[1].get("menu_kor")
            lun = lun.replace("-μμ°μ§: λ©λ΄κ²μν μ°Έμ‘°-","π₯μ μ¬π₯")
            din = haksik[2].get("menu_kor")
            din = din.replace("-μμ°μ§: λ©λ΄κ²μν μ°Έμ‘°","π₯μ λπ₯")
            completed_message += "π₯νμμλΉ λ©λ΄π±"
            completed_message += '\n\n'
            completed_message += mor
            completed_message += '\n\n'
            completed_message += lun
            completed_message += '\n\n'
            completed_message += din
            completed_message += '\n\n'
            bot.sendMessage(chat_id, completed_message)
            flag = True
        elif msg['text'] in 'λ§μ€' or msg['text'] in 'λ§μ€ν€μΉ' or msg['text'] in 'λ§μ€ λ©λ΄' or msg['text'] in 'λ§μ€ν€μΉ λ©λ΄':
            url = "http://smart.handong.edu/api/service/menu"
            print(url)
            response = requests.get(url)
            h_dict = json.loads(response.text)
            print("DAGSDGASD")
            print(h_dict)
            #λ§μ€ν€μΉ
            moms = h_dict.get("moms")
            mor = moms[0].get("menu_kor")
            mor = "πμμΉ¨π\n" + mor
            lun = moms[1].get("menu_kor")
            lun = "π₯μ μ¬π₯\n" + lun 
            din = moms[2].get("menu_kor")
            din = "π₯μ λπ₯\n" + din

            completed_message += "π₯λ§μ€ν€μΉ λ©λ΄π±"
            completed_message += '\n\n'
            completed_message += mor 
            completed_message += '\n'
            completed_message += lun
            completed_message += '\n'
            completed_message += din
            completed_message += '\n'
            bot.sendMessage(chat_id, completed_message)
            flag = True
        elif msg['text'] in 'μ½λ‘λ' or msg['text'] in 'νμ§μ' or msg['text'] in 'μ½λ‘λ νν©':
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
            completed_message += "π»μ§μ­λ³ μ½λ‘λ νν©π±+\n"

            for i in range(19):
                countryName = 'π' 
                countryName += data[i].get("countryName")
                newCase = data[i].get("newCase")
                newCase += ' λͺ'
                completed_message += countryName
                completed_message += ' : '
                completed_message += newCase
                completed_message += '\n'
    
            bot.sendMessage(chat_id, completed_message)
            flag = True
        elif msg['text'] in "μ¬μ©λ²" or msg['text'] in "μ¬μ©":
            bot.sendMessage(chat_id, 
            "\nπSIRLab νλ μ±λ΄ μλλ€.π€ΈββοΈ"\
            "\nπμ±λ΄ μ¬μ©λ²μ λ€μκ³Ό κ°μ΅λλ€.π\n\n"\
            "βοΈνμ¬ νλλ λ μ¨κ° κΆκΈνλ©΄ π€«βοΈ\n β λ μ¨ / νλλ μ¨\n"\
            "π±μ€λ νμ λ©λ΄κ° κΆκΈνλ©΄ π€«βοΈ\n β νμ / νμ λ©λ΄ \n"\
            "π₯μ€λ λ§μ€ν€μΉ λ©λ΄κ° κΆκΈνλ©΄ π€«βοΈ \nβ λ§μ€ / λ§μ€ λ©λ΄ \n"\
            "π₯Άμ€λ μ½λ‘λ λ°μ΄λ¬μ€ νν©μ΄ κΆκΈνλ©΄ π€«βοΈ \nβ μ½λ‘λ / μ½λ‘λ νν© \n"\
            )
            flag = True
        elif msg['text'] in "/start":
            pass
        else:
            bot.sendMessage(chat_id, 'λ¬΄μ¨ λ§μΈμ§ μ λͺ¨λ₯΄κ² μ΄μπ­\nπμ¬μ©λ²π μ΄λΌκ³  λ¬Όμ΄λ΄μ£ΌμΈμβΌοΈ')
            flag = True



bot = telepot.Bot(TOKEN)


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
global flag
flag = True
# Keep the program running.
bot.sendMessage(chat_id, 
            "\nπSIRLab νλ μ±λ΄ μλλ€.π€ΈββοΈ"\
            "\nπμ±λ΄ μ¬μ©λ²μ λ€μκ³Ό κ°μ΅λλ€.π\n\n"\
            "βοΈνμ¬ νλλ λ μ¨κ° κΆκΈνλ©΄ π€«βοΈ\n β λ μ¨ / νλλ μ¨\n"\
            "π±μ€λ νμ λ©λ΄κ° κΆκΈνλ©΄ π€«βοΈ\n β νμ / νμ λ©λ΄ \n"\
            "π₯μ€λ λ§μ€ν€μΉ λ©λ΄κ° κΆκΈνλ©΄ π€«βοΈ \nβ λ§μ€ / λ§μ€ λ©λ΄ \n"\
            "π₯Άμ€λ μ½λ‘λ λ°μ΄λ¬μ€ νν©μ΄ κΆκΈνλ©΄ π€«βοΈ \nβ μ½λ‘λ / μ½λ‘λ νν© \n"\
            )
while True:
    input()
        
