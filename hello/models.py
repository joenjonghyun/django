import random


def main():
    while 1 :
        menu =(input('0.나가기 1.계산기 2.체지방측정기 3.성적표 4.자동성적표 5.주사위 6.RandomGenerator 7.랜덤초이스 8.가위바위보 9.'))
        if menu == '0':
            break
        elif menu =='1': #계산기
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            opcode = (input('연산기호'))
            #객체생성
            calc = Qu1z01Calculator(num1,opcode,num2)
            print('*'*30)
            if opcode == '+' : result = (f'{calc.num1} + {calc.num2} = {calc.add()}')
            elif opcode == '-' : result = (f'{calc.num1} - {calc.num2} = {calc.sub()}')
            elif opcode == '*' : result = (f'{calc.num1} * {calc.num2} = {calc.mul()}')
            elif opcode == '/' : result = (f'{calc.num1} / {calc.num2} = {calc.div()}')
            print(result)

        elif menu == '2' : #BMI
            name = (input('이름'))
            height = int(input('키'))
            weight = int(input('몸무게'))
            bmi = Quiz02Bmi(name,height,weight)
            print(bmi.get_bmi())

        elif menu == '3': #성적표
            name = (input('이름'))
            kr = int(input('국어점수'))
            en = int(input('영어점수'))
            math = int(input('수학점수'))
            grade = Quiz03Grade(name, kr, en, math)
            result = (f'국어 : {grade.kr}점 영어 : {grade.en}점  수학 : {grade.math}점 \n 합계 : {grade.sum()} \n 평균 : {grade.avg()} 합격여부 : {grade.passing()}')
            print(f'{name}의 점수 {result} ')

        elif menu == '4': #자동성적표
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
            kr = int(input('국어점수 : '))
            en = int(input('영어점수 : '))
            math = int(input('수학점수 : '))
            #grade = Quiz04GradeAuto(name,kr, en, math)
            #print(f'{name}의 국어{kr} 영어{en} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')

        elif menu == '5': #주사위
           print(f'주사위 던지기\n{Quiz05Dice.cast()}')

        elif menu =='6':
            pass

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())

        elif menu =='8':
            q8 = Quiz08Rps(int(input('숫자입력')))
            print(q8.game())

        elif menu =='9':
            pass

        elif menu =='10':
            q10 = Quiz10LeapYear(int(input('년도입력')))
            res = (q10.get_LeapYear())

        elif menu =='11':
            pass

        elif menu =='12':
            pass

        elif menu =='13':
            pass

        elif menu =='14':
            pass




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
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def getBmi(self):
        bmires = self.weight/(self.height*self.height)*10000
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

class Quiz08Rps(object): #1가위2바위3보
    def __init__(self, player):
        self.player = player
        self.computer = myRandom(1,3)

    def game(self):
        c = self.computer
        p = self.player
        rps = ['가위', '바위', '보']
        if p == 1:
            if c == 1:
                res = f'플레이어 :{rps[1]} , 컴퓨터 :{rps[1]}, 결과 : 무승부'
            elif c == 2:
                res = f'플레이어 :{rps[1]} , 컴퓨터 :{rps[2]}, 결과 : 패배'
            elif c == 3 :
                res = f'플레이어 :{rps[1]} , 컴퓨터 :{rps[3]}, 결과 : 승리'
        if p == 2:
            if c == 1:
                res = f'플레이어 :{rps[2]} , 컴퓨터 :{rps[1]}, 결과 : 승리'
            elif c == 2:
                res = f'플레이어 :{rps[2]} , 컴퓨터 :{rps[2]}, 결과 : 무승부'
            elif c == 3:
                res = f'플레이어 :{rps[2]} , 컴퓨터 :{rps[3]}, 결과 : 패배'
        if p == 3:
            if c == 1:
                res = f'플레이어 :{rps[3]} , 컴퓨터 :{rps[1]}, 결과 : 패배'
            elif c == 2:
                res = f'플레이어 :{rps[3]} , 컴퓨터 :{rps[2]}, 결과 : 승리'
            elif c == 3:
                res = f'플레이어 :{rps[3]} , 컴퓨터 :{rps[3]}, 결과 : 무승부'
            return res


class Quiz09GetPrime(object):
    def __init__(self):
        pass

class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year
    def get_LeapYear(self):
        if self.year % 4 == 0 & self.year % 100 != 0 | self.year % 400 ==0:
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

if __name__ == '__main__':
    main()





