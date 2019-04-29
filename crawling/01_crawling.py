from bs4 import BeautifulSoup as bs
import requests

#1. requests 네이버 실시간 검색정보 가져와줘 그리고 글로 바꿔줘

url= 'https://naver.com'
response = requests.get(url).text
# print(response)

#2 bs 객체에서 response 라고 하는 변수 안의 객체를 파싱하고 그변수를 
# bs 객체로 반환

soup = bs(response,"html.parser")
# print(type(soup))

#3 bs 객체에 담긴 변수에서 css selector를 활용해 특정 정보를 가져온다
keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div span[class*=ah_k]')

for index, keyword in enumerate(keywords): # 키값 벨류값
    print(index,keyword.text)

