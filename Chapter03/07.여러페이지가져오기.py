import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt('검색어 입력 : ')
lastpage = int(pyautogui.prompt('마지막 페이지번호를 입력하세요'))
# print(type(lastpage))  자료형이 str이니까 형변환 필요
page_num = 1

for i in range(1, lastpage*10, 10):  # range(시작, 끝, 단계)
    print(f'----------------------- {page_num}페이지 입니다. ----------------------- ')
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('.news_tit')

    for title in titles:
        a = title.text
        link = title.attrs['href']
        print(a, link)
        
    page_num += 1