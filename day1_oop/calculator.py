# 교재 p.188
class Calculator:

    # 가장 먼저 실행되는 함수 (생략가능)
    def __init__(self, first_num, second_num):
        self.first = first_num
        self.second = second_num


    # 덧셈
    def sum(self):
        return self.first + self.second

    # 뺄셈
    def sub(self):
        return self.first - self.second

    # 곱셈
    def mul(self):
        return self.first * self.second

    # 나눗셈
    def div(self):
        return self.first / self.second

    # 나머지
    def mod(self):
        return self.first % self.second


    # @ 데코레이터 : 하단의 메소드가 무슨 역할을 하는지 명시해주는 역할
    @staticmethod
    def execute():  # staticmethod에서는 self를 사용하지 않음
        calc = Calculator(int(input(">> 첫번째수 입력 : ")), int(input(">> 두번째수 입력 : ")))

        print(f'첫번째수 : {calc.first}')
        print(f'두번째수 : {calc.second}')

        print(f'{calc.first} + {calc.second} = {calc.sum()}')
        print(f'{calc.first} - {calc.second} = {calc.sub()}')
        print(f'{calc.first} * {calc.second} = {calc.mul()}')
        print(f'{calc.first} / {calc.second} = {calc.div()}')
        print(f'{calc.first} % {calc.second} = {calc.mod()}')


if __name__ == '__main__':
    Calculator.execute()