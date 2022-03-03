from hello.domains import Member
from models import Qu1z01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, \
    Quiz10LeapYear

if __name__ == '__main__':
    while 1:
        menu = (input('0.나가기 1.계산기 2.체지방측정기 3.성적표 4.자동성적표'
                      ' 5.주사위 6.RandomGenerator 7.랜덤초이스 8.가위바위보 9.'))
        if menu == '0':
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            opcode = (input('연산기호'))
            # 객체생성
            calc = Qu1z01Calculator(num1, opcode, num2)
            print('*' * 30)
            if opcode == '+':
                result = (f'{calc.num1} + {calc.num2} = {calc.add()}')
            elif opcode == '-':
                result = (f'{calc.num1} - {calc.num2} = {calc.sub()}')
            elif opcode == '*':
                result = (f'{calc.num1} * {calc.num2} = {calc.mul()}')
            elif opcode == '/':
                result = (f'{calc.num1} / {calc.num2} = {calc.div()}')
            print(result)

        elif menu == '2':
            member = Member()
            q2 = Quiz02Bmi
            member.name = (input('이름'))
            member.height = float(input('키'))
            member.weight = float(input('몸무게'))
            res = q2.getBmi(member)
            print(f'이름 : {member.name}, 키 : {member.height}, '
                  f'몸무게 : {member.weight}, 측정결과 : {res}')

        elif menu == '3':
            name = (input('이름'))
            kr = int(input('국어점수'))
            en = int(input('영어점수'))
            math = int(input('수학점수'))
            grade = Quiz03Grade(name, kr, en, math)
            result = (
                f'국어 : {grade.kr}점 영어 : {grade.en}점  수학 : {grade.math}점 \n 합계 : {grade.sum()} \n 평균 : {grade.avg()} 합격여부 : {grade.passing()}')
            print(f'{name}의 점수 {result} ')

        elif menu == '4':
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
            kr = int(input('국어점수 : '))
            en = int(input('영어점수 : '))
            math = int(input('수학점수 : '))
            # grade = Quiz04GradeAuto(name,kr, en, math)
            # print(f'{name}의 국어{kr} 영어{en} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')

        elif menu == '5':
            print(f'주사위 던지기\n{Quiz05Dice.cast()}')

        elif menu == '6':
            pass

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())

        elif menu == '8':
            q8 = Quiz08Rps()
            print(q8.game())

        elif menu == '9':
            pass

        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('년도입력')))
            print(q10.get_LeapYear)

        elif menu == '11':
            pass

        elif menu == '12':
            pass

        elif menu == '13':
            pass

        elif menu == '14':
            pass
