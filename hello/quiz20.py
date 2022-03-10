import random
import urllib.request
from urllib.request import urlopen

from bs4 import BeautifulSoup
import pandas as pd


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

    def quiz24zip(self) -> {}: ##자바에서퍼블릭보이드스태틱느낌ㅇㅇ
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')

        # self.find_ranking(soup) #랭킹보기
        #cls_names = ['artist', 'title']
        #a = [i for i in cls_names]
        ls1 = self.abc(soup, 'title')
        ls2 = self.abc(soup, 'artist')
        #self.dict1(ls1, ls2)

        ##j는 스트링값이라 못 들어가는데 딕셔너리에는 들어갈수있음
        ##딕셔너리는 키값으로 찾고 리스트값은 인덱스로찾는다

        dict = {}
        for i, j, in zip(ls1, ls2):
            dict[i] = j
        return dict



    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)


    def print_music_list(self,soup) -> None:
        artist = soup.find_all('p', {'class': 'artist'})
        artist = [i.get_text() for i in artist]
        print(''.join(i for i in artist))
        title = soup.find_all('p', {'class': 'title'})
        title = [i.get_text() for i in title]
        print(''.join(i for i in title))


    def find_ranking(self, soup):
        for i, j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(self.abc(soup, j)))  #이줄은 아래abc랑같음
        print('*'*100)

    @staticmethod
    def abc(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        title = [i.get_text() for i in ls]
        #print(''.join(i for i in title))
        return title  #줄일수있는건다줄여보자

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

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    def print_music_list(self, soup) -> None:
        artist = soup.find_all('p', {'class': 'artist'})
        artist = [i.get_text() for i in artist]
        print(''.join(i for i in artist))
        title = soup.find_all('p', {'class': 'title'})
        title = [i.get_text() for i in title]
        print(''.join(i for i in title))

    def find_ranking(self, soup):
        for i, j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(self.abc(soup, j)))  # 이줄은 아래abc랑같음
        print('*' * 100)

    @staticmethod
    def abc(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        title = [i.get_text() for i in ls]
        # print(''.join(i for i in title))
        return title  # 줄일수있는건다줄여보자

    def quiz28dataframe(self) -> str:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bug.csv', sep=',', na_rep='NaN')


    def quiz29(self) -> str: return None



