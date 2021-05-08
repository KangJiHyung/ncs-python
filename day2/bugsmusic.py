import ssl
from bs4 import BeautifulSoup                  # BeautifulSoup 패키지를 사용하겠다
from urllib.request import urlopen             # URL을 오픈할 때 사용할 메소드

# Class의 첫번째 글자는 대문자로 설정하는 것이 규칙
class Bugsmusic:

    page_url = ""

    def scrap(self):
        context = ssl._create_unverified_context()

        url        = urlopen(self.page_url, context = context)
        soup       = BeautifulSoup(url, "lxml")   # lxml : 파서? '번역기'라고 생각
        cnt_artist = 0
        cnt_title  = 0

        for link1 in soup.find_all(name="p", attrs=({"class":"artist"})):
            cnt_artist += 1
            print(str(cnt_artist) + "위")
            print("아티스트 : " + link1.find("a").text)

        print("---------------------------------------")

        for link2 in soup.find_all(name="p", attrs=({"class":"title"})):
            cnt_title += 1
            print(str(cnt_title) + "위")
            print("노래제목" + link2.text)

    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.page_url = "https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210508&charthour=13"
        bugs.scrap()

if __name__ == "__main__":
    Bugsmusic.main()