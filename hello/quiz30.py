import random
import string

import numpy as np
import pandas as pd
from icecream import ic
from titanic.models import Model
from hello.domains import myRandom, myMember, members


class Quiz30:

    '''
            데이터프레임 문제 Q02
        ic| df:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
    '''

    def quiz30_df_4_by_3(self) -> str:
        e = [[i for i in range(j*3+1, j*3+4)] for j in range(4)]
        ##columns = [chr(i) for i in range(65, 68)]
        df = pd.DataFrame([[i for i in range(j*3+1, j*3+4)] for j in range(4)], index=range(1, 5), columns=['A', 'B', 'C'])
        #df = pd.DataFrame([[1, 2, 3],
        #                   [4, 5, 6],
        #                   [7, 8, 9],
        #                   [10, 11, 12]], index=range(1, 5), columns=['A', 'B', 'C'])
        #a = [i for i in range(1, 4)]
        #b = [i for i in range(4, 7)]
        #c = [i for i in range(7, 10)]
        #d = [i for i in range(10, 13)]
        #e = {'1' : a, '2' : b, '3' : c,}
        # 위 식을 리스트결합 형태로 분해해서 조립하시오
        ic(df)
        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''

    def quiz31_rand_2_by_3(self) -> str:
        '''
        l1 = [[myRandom(0,101) for i in range(3)] for i in range(2)]
        l2 = [i for i in range(2)]
        columns = [i for i in range(3)]
        # df = pd.DataFrame([], index=[], columns=[])구조
        df = pd.DataFrame(l1, index=l2, columns=columns)
        '''
        df = pd.DataFrame(np.random.randint(0, 101, size=(2, 3)))
        print(df)
        return None

    '''
            데이터프레임 문제 Q04.
            국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
             단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

              ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''
    @staticmethod
    def id(chr_size) -> str : return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)]) #랜덤초이스를 사용해서 무작위로 알파벳 5글자를 줌 스트링으로 받아줘야하니
    def quiz32_df_grade(self) -> object:
        data1 = (np.random.randint(0, 101, (10, 4)))
        idx = [self.id(chr_size=5) for i in range(10)]
        col1 = ['국어', '영어', '수학', '사회']
        df1 = pd.DataFrame(data1, index=idx, columns=col1)
        data2 = {i: j for i, j in zip(idx, data1)}
        col2 = ['국어', '영어', '수학', '사회']
        df2 = pd.DataFrame.from_dict(data2, orient='index', columns=col2)
        ic(df1)
        ic(df2)
        return None



    def quiz33_df_loc(self) -> str:
        df = self.createDf(keys=['a', 'b', 'c', 'd'],
                           vals=np.random.randint(0, 100, 4),
                           len=3)
        #ic(df)
        # a = [{i: j for i, j in zip(['a', 'b', 'c', 'd'], np.random.randint(0, 101, 4))}for i in range(3)]
        # print(a)
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        # grade.csv
        #df2 = pd.DataFrame(np.random.randint(0, 101, (24, 4)), index=members(), columns=['자', '파', '자.스', 'SQL'])
        #ic(df2)
        #df2.to_csv('./save/grade.csv', sep=',', na_rep='NaN')
        model = Model()
        grade_df = model.new_model('grade_backup.csv')
        ic(grade_df)






        '''
                데이터프레임 문제 Q04.
                국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                  ic| df4:         자  파  자.스 SQL
                            lDZid  57  90  55  24
                            Rnvtg  12  66  43  11
                            ljfJt  80  33  89  10
                            ZJaje  31  28  37  34
                            OnhcI  15  28  89  19
                            claDN  69  41  66  74
                            LYawb  65  16  13  20
                            QDBCw  44  32   8  29
                            PZOTP  94  78  79  96
                            GOJKU  62  17  75  49
        '''





        return None




    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz34_iloc(self) -> str:


        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a    61
                b    57
                c    63
                d    19
                Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a   b  c   d
                            0  36  24  2  12
        '''
        # ic(df.iloc[[0,1]])
        '''
        ic| df.iloc[[0,1]]:     a   b   c   d
                            0  27  73  90  71
                            1  27  73  90  71
        '''
        # ic(df.iloc[:3])
        '''
        ic| df.iloc[:3]:     a   b   c   d
                         0  92  28  64  62
                         1  92  28  64  62
                         2  92  28  64  62
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:     a  b   c   d
                                          0  96  6  77  28
                                          2  96  6  77  28
        '''

        # ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                                 0  27  30  15  18
                                                 2  27  30  15  18
        '''

        # ic(df.iloc[0, 1])
        '''
        ic| df.iloc[0, 1]: 30
        '''

        # ic(df.iloc[[0, 2], [1, 3]])
        '''
        ic| df.iloc[[0, 2], [1, 3]]:     b   d
                                     0  30  18
                                     2  30  18
        '''

        # ic(df.iloc[1:3, 0:3])
        '''
        ic| df.iloc[1:3, 0:3]:     a   b   c
                               1  27  30  15
                               2  27  30  15
        '''

        # ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                    0  27  15
                                                    1  27  15
                                                    2  27  15
        '''

        # ic(df.iloc[:, lambda df: [0, 2]])
        '''
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                           0  27  15
                                           1  27  15
                                           2  27  15
        '''

        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None