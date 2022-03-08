import random
import urllib.request
from urllib.request import urlopen

from bs4 import BeautifulSoup


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])
        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][3])
        list3 = [1, '2', [1, 2, 3]]
        print(list3)
        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)
        return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('legacy')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('comprehension')

        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        artists = soup.find_all('p', {'class' : 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        res = soup.find_all('div', {'class' : 'ellipsis rank01'})
        res = [i.get_text() for i in res]
        print(''.join(i for i in res))
        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None
