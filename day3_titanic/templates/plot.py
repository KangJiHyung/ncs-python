from day3_titanic.models.dataset import Dataset
from day3_titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='../day2_crawling/data/D2Coding.ttf').get_name())

class Plot:
    def __init__(self, fname):
        service = Service()
        dataset = Dataset()
        dataset.context = './datas/'
        dataset.fname = fname
        self.entity = service.new_model(dataset.fname)

    def plot_survived_dead(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0. 사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0. 사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def plot_sex(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 [0. 사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0. 사망자 vs 1.생존자]')
        plt.show()