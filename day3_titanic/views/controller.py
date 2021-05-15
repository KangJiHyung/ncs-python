from sklearn.ensemble import RandomForestClassifier

from day3_titanic.models.dataset import Dataset
from day3_titanic.models.service import Service
import pandas as pd

class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        #print(f'트레인 드랍 전 컬럼 : {this.train.columns}')
        '''
            ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        '''

        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        #print(f'트레인 드랍 후 컬럼 : {this.train.columns}')
        '''
            ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
        '''

        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        this = service.sex_nominal(this)
        this = service.fare_ordinal(this)
        this = service.fareBand_nominal(this)
        this = service.drop_feature(this, 'Fare')
        this = service.drop_feature(this, 'Age')
        this = service.drop_feature(this, 'SibSp')
        this = service.drop_feature(this, 'Parch')
        # print(f'전처리 마감 후 컬럼 : {this.train.columns}')
        # print(f'train의 Null 수량 : {this.train.isnull().sum()}')
        # print(f'test의 Null 수량 : {this.test.isnull().sum()}')
        '''
            전처리 마감 후 컬럼 : Index(['Survived', 'Pclass', 'Sex', 'Embarked', 'Title', 'AgeGroup', 'FareBand'], dtype='object')
            train의 Null 수량 : Survived    0
            Pclass      0
            Sex         0
            Embarked    0
            Title       0
            AgeGroup    0
            FareBand    0
            dtype: int64
            test의 Null 수량 : Pclass      0
            Sex         0
            Embarked    0
            Title       0
            AgeGroup    0
            FareBand    0
        '''
        return this

    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        print(f'결정트리 검증 정확도 {service.accuracy_by_dtree(this)}')
        print(f'랜덤포레스트 검증 정확도 {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증 정확도 {service.accuracy_by_nb(this)}')
        print(f'KNN 검증 정확도 {service.accuracy_by_knn(this)}')
        print(f'SVM 검증 정확도 {service.accuracy_by_svm(this)}')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId' : this.id, 'Survived' : prediction}).to_csv('./data/submission.csv', index=False)

