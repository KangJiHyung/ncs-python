from dataset import Dataset     # titanic/models/dataset.py
import pandas as pd             # pandas를 pd라고 부르겠다

'''
    PassengerId  고객ID,
    Survived 생존여부,
    Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
    Name,
    Sex,
    Age,
    SibSp 동반한 형제, 자매, 배우자,
    Parch 동반한 부모, 자식,
    Ticket 티켓번호,
    Fare 요금,
    Cabin 객실번호,
    Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''

class Service(object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset         # this에 dataset.py에 정의해 둔 변수들을 담은 것
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this):         # 답을 제거하는 작업
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this):         # 답을 분리하는 작업
        return this.train['Survived']