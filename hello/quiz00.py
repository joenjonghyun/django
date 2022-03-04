from hello.domains import myRandom, my100, Member, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        op = o[myRandom(0, 4)]
        if op == '+':
            result = (self.add(a, b))
        elif op == '-':
            result = (self.sub(a, b))
        elif op == '*':
            result = (self.mul(a, b))
        elif op == '/':
            result = (self.div(a, b))
        elif op == '%':
            result = (self.mod(a, b))
        print(result)
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        height = int(input('키 : '))
        weight = int(input('무게 : '))
        res = weight / (height * height) * 10000
        if res > 25:
            result = f'비만'
        elif res > 23:
            result = f'과체중'
        elif res > 18.5:
            result = f'정상'
        else:
            result = f'저체중'

        print(f'키 :{height}, 몸무게 :{weight}, 체지방 :{res}, \n 결과 :{result}')

    def quiz02dice(self):

        print(myRandom(1, 6))

    def quiz03rps(self):
        c = myRandom(0, 2)
        p = int(input('0가위,1바위,2보'))
        if c - p == -1 or c - p == 2:
            print(f'플레이어 : {p} 승리 \n 컴퓨터 : {c} 패배')
        elif c - p == 1 or c - p == -2:
            print(f'플레이어 : {p} 패배 \n 컴퓨터 : {c} 승리')
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

    def quiz04leap(self):
        year = myRandom(0, 2500)
        if year % 4 == 0 & year % 100 != 0 | year % 400 == 0:
            res = '윤년'
        else:
            res = '평년'
        print(year)
        print(res)


    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = kor + eng + math
        avg = sum / 3
        grade = 'A,B,C,D,E'
        passChk ='합격'   #여기서부터 해야됨
        return [sum, avg, grade, passChk]

    def sum(self):
        pass

    def avg(self):
        sum / 3

    def grade(self):
        pass

    def passChk(self):  # 60점이상이면 합격
        pass

    def quiz06memberChoice(self):
        pass

    def quiz07lotto(self):
        pass



    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        name = Member()
        Member.name = ''

        while 1:
            menu = int(input('0.나가기 1.이름 2.입금 3.출금'))
            if menu == '0':
                break
            elif menu == '1':
                pass
            elif menu == '2':
                pass
            elif menu == '3':
                pass



    def quiz09gugudan(self):  # 책받침구구단
        pass
