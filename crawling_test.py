#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 00:57:43 2020

@author: swsong
"""

#%% 라이브러리 호출
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

#%% 기본변수 설정
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
keyUrl = input('검색어를 입력하세요 : ')
#url = baseUrl + keyUrl  .. keyUrl 을 아스키코드로 변환해주지 않으면 인코딩되지 않음
url = baseUrl + quote_plus(keyUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

# print(img[0]) ..소스한번살펴보기

#%% 크롤링 스타트
n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./test_imgCrawling_3/' + keyUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    
print('다운로드 완료')
            

