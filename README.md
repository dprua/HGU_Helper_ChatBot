# OSS_Final_Project
 
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
2-1. Send a "/newbot" message to BotFather.
2-2. Set the name of the chatbot.
2-3. Write down your name again.
2-4. Check the issued chatbot TOKEN value.
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

**텍스트**

# 6. 인용
> 인용1

> 인용2
>> 인용안의 인용

# 7. 수평선 넣기

---
  
# 8. 링크 달기
(1) 인라인 링크  

[블로그 주소](https://lsh424.tistory.com/)

(2) 참조 링크  

[블로그 주소][blog]

[blog]: https://lsh424.tistory.com/

# 9. 이미지 추가하기
![이탈리아 포지타노](https://user-images.githubusercontent.com/31477658/85016059-f962aa80-b1a3-11ea-8c91-dacba2666b78.jpeg)

### 이미지 사이즈 조절
<img src="https://user-images.githubusercontent.com/31477658/85016059-f962aa80-b1a3-11ea-8c91-dacba2666b78.jpeg"  width="700" height="370">

### 이미지 파일로 추가하기
<img src="Capri_Island.jpeg" width="700">

# 10. 코드블럭 추가하기

```swift
public struct CGSize {
  public var width: CGFloat
  public var heigth: CGFloat
  ...
}
```

# etc

**텍스트 굵게**  
~~텍스트 취소선~~

### [개행]  

스페이스바를 통한 문장개행  
스페이스바를 통한 문장개행  

br태그를 사용한 문장개행
<br>
<br>
br태그를 사용한 문장개행


### [체크박스]

다음과 같이 체크박스를 표현 할 수 있습니다. 
* [x] 체크박스
* [ ] 빈 체크박스
* [ ] 빈 체크박스

### [이모지 넣기]
❤️💜💙🤍

### [표 넣기]
|왼쪽 정렬|가운데 정렬|오른쪽 정렬| 
|:---|:---:|---:| 
|내용1|내용2|내용3| 
|내용1|내용2|내용3| 

<br>

### 정리내용
[정리 내용 보기](https://lsh424.tistory.com/37)
