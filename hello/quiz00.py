from hello.domains import myRandom, my100, Member, members, myMember


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
        '''year = myRandom(2000, 2022)
        if year % 4 == 0 & year % 100 != 0 | year % 400 == 0:
            res = '윤년'
        else:
            res = '평년'
        print(year)
        print(res)'''


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
        Account.main()



    def quiz09gugudan(self):  # 책받침구구단
        pass

'''
08번 문제 해결을 위한 클래스는 다음과 같다.
[요구사항(RFP)]
은행이름은 비트은행이다.
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
예를들면 123-12-123456 이다.
금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다)
'''
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = myMember() if name == None else name
        #a = myRandom(0, 999)
        #b = myRandom(0, 99)
        #c = myRandom(0, 999999)
        self.account_number = self.create_account_number() if account_number == None else account_number
        # f'{str(a).rjust(3, "0")} - {str(b).rjust(2, "0")} - {str(c).rjust(6, "0")}'

        self.money = myRandom(100,999) if money == None else money


    def to_string(self):
        return f'은행 : {self.BANK_NAME}, '\
               f'입금자 : {self.name}, '\
               f'계좌번호 : {self.account_number}, '\
               f'금액 : {self.money} 만원\n'

    #[i <조건절> for i in range()]
    def create_account_number(self):
        '''ls = [str(myRandom(0,10) for i in range(3))]
        ls.append("-")
        ls += [str(myRandom(0,10) for i in range(2))]
        ls.append("-")
        ls += [str(myRandom(0,10) for i in range(6))]
        return "".join()'''
        return "".join(['-' if i == 3 or i == 6 else str(myRandom(0, 9)) for i in range(13)])

    def deposit(self):
        pass

    @staticmethod
    def find_account(ls, account_number):
        #return ''.join([j.to_string() if j.account_number == account_number else '찾는 계좌가 아님' for i, j in enumerate(ls)])
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                a = ls[i]
            return a


    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]



    @staticmethod
    def main():
        ls = []
        while 1 :
            menu = input('0.종료 1.계좌개설 2.계좌목록 3. 입금 4. 출금 .5계좌해지 6.계좌조회')
            if menu == '0':
                break
            if menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()}개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a = '\n'.join(i.to_string() for i in ls)
                print(f'{a}')
            elif menu == '3':
                Account.deposit(ls, input('입금액'))
                account_number = input('입금할 계좌번호')
            elif menu == '4':
                account_number = input('출금할 계좌번호')
                money = input('출금액')
            elif menu == '5':
                Account.del_account(ls,input('탈퇴할 계좌번호'))
            elif menu == '6':
                print(Account.find_account(ls,input('검색할 계좌번호')))
            else:
                print('Worng number..Try Again')
                continue





