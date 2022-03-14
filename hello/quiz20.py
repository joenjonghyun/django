import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from hello.domains import myMember, myRandom


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
            a.append(i) ##아 이따필기
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
        dt = {i:j for i, j in zip(ls1, ls2)}
        l = [i * j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        print(d1)

        #self.dict1(ls1, ls2)
        #self.dict2(ls1, ls2)
        #self.dict3(ls1, ls2)
        ##j는 스트링값이라 못 들어가는데 딕셔너리에는 들어갈수있음
        ##딕셔너리는 키값으로 찾고 리스트값은 인덱스로찾는다





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

    @staticmethod
    def dic3(ls1, ls2) -> None:
        dict = {}
        for i, j, in zip(ls1, ls2):
            dict[j] = ls2[i]
        return dict


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

    @staticmethod
    def quiz25dictcom() -> str:
        #students = [myMember() for i in range(5)]
        #scores = [myRandom(1, 100) for i in range(5)]
        #print(students, scores)

        a = set([myMember() for i in range(5)])
        while len(a) != 5:    #a의 길이가 5가 아닐 때
            a.add(myMember())   #a에 myMember를 더해라
        students = list(a)
        scores = [myRandom(0, 100) for i in range(5)]
        b = {i : j for i, j in zip(students, scores)}
        #stu_set = set(students)
        #students = list(stu_set)
        print(b)


        #students = [myMember() for i in (range(0, 23), 5)]
        #students = list(set(students))

        #scores = [myRandom(0, 100) for i in (range(1, 100), 5)]
        #scores = list(set(scores))
        #print(students, scores)

        return None

    '''
    my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
    my_set = set(my_list) #집합set으로 변환
    my_list = list(my_set) #list로 변환
    print(new_list)
    출력된 값은 ['D', 'B', 'A', 'E', 'C']
    '''

    '''
    li = [1, 2, 3]
    sampleList = random.sample(li, 2)
    # 리스트에서 2개 랜덤 추출  

    a = random.sample(range(1, 101), 10)  # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
    print(a)
    '''

    def quiz26map(self) -> str:

        return None

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

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bug.csv', sep=',', na_rep='NaN')

    '''
    데이터프레임 문제 Q01.
    홀짝을 구분하는 리스트컴프리헨션과 zip()으로 딕셔너리를 결합시킨
    로직으로 작성하시오. 다음 결과가 출력되야 한다.
        a   b   c
    1   1   3   5
    2   2   4   6 
   
    '''

    def quiz29_pandas_df(self) -> object:
        d = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d, index=[1, 2])
        '''
           a  b  c
        1  1  3  5
        2  2  4  6
        '''
        d2 = {'1': [1, 3, 5],
              '2': [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2)
        '''
           1  2
        0  1  2
        1  3  4
        2  5  6
        '''
        d3 = {'1': [1, 3, 5]}
        d4 = {'2': [2, 4, 6]}
        ls1 = []
        ls2 = []
        val = [ls1, ls2]
        c = ['a', 'b', 'c']
        columns = [chr(i) for i in range(97, 100)]
        [ls1.append(i) if i % 2 == 1 else ls2.append(i) for i in range(1, 7)]
        dict = {}
        for i, j in zip([1, 2], val):
            dict[i] = j
        df3 = pd.DataFrame.from_dict(dict, orient='index', columns=['a', 'b', 'c'])
        '''
           a  b  c
        1  1  3  5
        2  2  4  6
        '''
        print(df3)



        return None



