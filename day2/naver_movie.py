from selenium import webdriver
from bs4 import BeautifulSoup

class NaverMovie(object):

    chromedriver = "/Users/KJH/PycharmProjects/chromedriver"
    page_url = ""

    def scrap(self):
        driver = webdriver.Chrome(self.chromedriver)
        driver.get(self.page_url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class', 'tit3'})
        for i in [div.a.string for div in all_div]:
            print(i)
        driver.close()

    @staticmethod
    def main():
        naver = NaverMovie()
        naver.page_url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
        naver.scrap()

if __name__ == "__main__":
    NaverMovie.main()