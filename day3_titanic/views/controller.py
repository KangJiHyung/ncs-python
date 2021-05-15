from titanic.models.dataset import Dataset
from titanic.models.service import Service
import pandas as pd

class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train()

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        print(f'트레인 드랍 전 컬럼 : {this.train.colums}')