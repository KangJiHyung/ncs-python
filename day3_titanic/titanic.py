class Titanic:

    survival = ''   # 생존여부 (0:사망, 1:생존)
    pclass = ''     # 승선권 클래스 (1:1등석, 2:2등석, 3:3등석)
    sex = ''        # 성별
    name = ''       # 승객 이름
    age = ''        # 승객 나이
    sibsp = ''      # 동반한 형제, 자매, 배우자의 수
    parch = ''      # 동반한 부모, 자식 수
    ticket = ''     # 티켓 고유번호
    fare = ''       # 티켓 요금
    cabin = ''      # 객실 번호
    embarked = ''   # 승선한 항구명 (C:캠브릿지, Q:퀸스타운, S:사우스햄프턴)

    def __init__(self):
        pass

    def create_train(self) -> object:
        pass

    def create_model(self) -> object:
        pass

    def create_dummy(self) -> object:
        pass

    def create_random_variables(self) -> object:
        pass

    def submit(self) -> object:
        pass

    @staticmethod
    def main():
        pass

if __name__ == '__main__':
    Titanic.main()