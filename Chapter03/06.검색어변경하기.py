"""
프로그램을 실행하면 검색어를 입력받게 하고, 해당 검색어로 크롤링 되게 만들어보자
"""
import requests
from bs4 import BeautifulSoup

keyword = input('검색어 입력 : ')
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.news_tit')

for title in titles:
    a = title.text
    link = title.attrs['href']
    print(a, link)
    