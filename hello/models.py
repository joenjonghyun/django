import random
class Qu1z01Calculator:
    def __init__(self, num1,opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2

class Quiz02Bmi:
    @staticmethod
    def getBmi(member):
        this = member
        bmires = this.weight/(this.height*this.height)*10000
        if bmires > 25:
            return f'비만'
        elif bmires > 23:
            return f'과체중'
        elif bmires > 18.5:
            return f'정상'
        else:
            return f'저체중'

class Quiz03Grade(object):
    def __init__(self,name,kr,en,math):
        self.name = name
        self.kr = kr
        self.en = en
        self.math = math
    def sum(self):
        return self.kr + self.en + self.math
    def avg(self):
        return self.sum() /3
    def passing(self):
        if self.avg()>=60:
            return '합격'
        else:
            return '불합격'

class Quiz04GradeAuto(object):
    def __init__(self, name, kr, en, math):
        self.name = name
        self.kr = kr
        self.en = en
        self.math = math

    def sum(self):
        return self.kr + self.en + self.math
    def avg(self):
        return sum() /3
    def getGrade(self):
        pass
    def chkPass(self):
        pass

def myRandom(start, end):
    return random.randint(start,end)

class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1,6)


class Quiz07RandomChoice(object):
    def __init__(self):#803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']
    def chooseMember(self):
        return self.members[myRandom(0,23)]
        #리턴사용의 이유는 리엑트로 보내주라는 소리임

class Quiz08Rps(object):
    def game(self):
        c = myRandom(0,2)
        p = int(input('0가위,1바위,2보'))
        if c-p == -1 or c-p == 2:
            print(f'플레이어 : {p} 승리 \n 컴퓨터 {c} : 패배')
        elif c-p == 1 or c-p == -2:
            print(f'플레이어 : {p} 패배 \n 컴퓨터 {c} : 승리')
        else:
            print('무승부')

        '''
           <게이머 승리일때>
            컴퓨터0(가위) / 게이머1(바위)(win) = -1
            컴퓨터1(바위) / 게이머2(보)(win) = -1
            컴퓨터2(보) / 게이머0(가위)(win) = 2
           <컴퓨터 승리일때>
            컴퓨터0(가위) / 게이머2(보)(lose) = -2
            컴퓨터1(바위) / 게이머0(가위)(lose) = 1
            컴퓨터2(보) / 게이머1(바위)(lose) = 1 '''


class Quiz09GetPrime(object):
    def __init__(self):
        pass

class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year
    def get_LeapYear(self):
        if self.year % 4 == 0 & self.year % 100 != 0 | self.year % 400 == 0:
            return '윤년'
        else:
            return '평년'


class Quiz11NumberGolf(object):
    def __init__(self):
        pass

class Quiz12Lotto(object):
    def __init__(self):
        pass

class Quiz13Bank(object):
    def __init__(self):
        pass

class Quiz14Gugudan(object):
    def __init__(self):
        pass






