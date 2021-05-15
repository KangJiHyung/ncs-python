class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'안녕하세요. 제 이릉은 {self.name}이고, 나이는 {self.age}살이고, {self.address}에 거주하고 있습니다.')

    @staticmethod
    def main():
        maria = Person('마리아', 20, '서울')
        maria.greeting()

        tom = Person('톰', 22, '인천')
        tom.greeting()


if __name__ == '__main__':
    Person.main()