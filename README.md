# SIRLab ChatBot
 
## 1. What does this project do?
**SIRLab_ChatBot** is a Chetbot that provides useful information to students at Handong University. If you are curious about the school meal menu or the school weather, you can easily get information using this checkbot.
This chatbot uses a Telegram application, and the server runs on Raspberry Pi based on Python. Since this chatbot uses Telegram, everyone can get information through this chatbot if the server is working.
## 2. Why is this project useful?
Food information and weather information are very necessary information for Handong University students. By using this service, people will be able to save their time in busy college life.
## 3. How do I get started?
Clone GitHub at the local location you want.
After navigating to the Project folder,
```swift
cd OSS_project
```
Install the package required to operate the chatbot.
```swift
pip install -r requirement.txt
```
If the package is installed, perform the following procedure:
1. Get a default api key from https://openweathermap.org/.
2. Install Telegram and chat BotFather.

     a. Send a "/newbot" message to BotFather.

     b. Set the name of the chatbot.

     c. Write down your name again.

     d. Check the issued chatbot TOKEN value.

3. Check your own chat_id value in the source code.
```swift
content_type, chat_type, chat_id = telepot.glance(msg)
```
4. Check city.list.json for the id of the city you want.
5. Fill in the source code with the api key, TOKEN, chat_id, and city_id.
```swift
city_id = '1839071' # put cities id you want
api_id = '' # put your api id
TOKEN = '' # put your telegram token info
chat_id = 1234 # put your chat_id here
```
6. Use the following command to operate the chatbot:
```swift
python3 chatbot.py
```

## 4. Where can I get more help, if I need it?
If you need any help, please contact me via email at 21600277@handong.edu. 

You can refer to the reference below in other ways.
## 5. Presentation Video (YouTube) Link

## 6. Operation screen
<img src="https://user-images.githubusercontent.com/34247631/120386061-1ebfd880-c363-11eb-9187-c64f935c7666.png"  width="300" height="700"><img src="https://user-images.githubusercontent.com/34247631/120386491-aa396980-c363-11eb-9d13-b074967dc320.png"  width="500" height="700">
<img src="https://user-images.githubusercontent.com/34247631/120386752-00a6a800-c364-11eb-9a8c-8caac4b78fe5.png"  width="300" height="300">

## 7. Reference
**1. Openweathermap-api =>** 
[Openweathermap-api](https://openweathermap.org/api)

**2. Handong-menu-api =>** [Handong-menu-api](http://smart.handong.edu/api/service/menu)
