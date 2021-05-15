from day3_titanic.views.controller import Controller
from day3_titanic.templates.plot import Plot

if __name__ == '__main__':
    def print_menu():
        print('0. EXIT')
        print('1. 시각화')
        print('2. 모델링')
        print('3. 머신러닝')
        print('4. 머신생성')
        return input('메뉴 입력 >> ')

    app = Controller()

    while True:
        menu = print_menu()

        if menu == '1':
            print('----- 1. 시각화 실행 -----')
            plot = Plot('train.csv')
            menu = input('[차트]\n'
                         '1. 생존자 vs 사망자\n'
                         '2. 생존자 성별 대비\n'
                         '차트 선택 >> ')
            if menu == '1':
                plot.plot_survived_dead()
            elif menu == '2':
                plot.plot_sex()

        elif menu == '2':
            print('----- 2. 모델링 -----')
            app.modeling('train.csv', 'test.csv')

        elif menu == '3':
            print('----- 3. 머신러닝 -----')
            app.learning('train.csv', 'test.csv')

        elif menu == '4':
            print('----- 4. 머신생성 -----')
            app.submit('train.csv', 'test.csv')

        else:
            break