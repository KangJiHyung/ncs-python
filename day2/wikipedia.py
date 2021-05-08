from bs4 import BeautifulSoup
import requests

class Wikipedia:

    page_url = ""

    def scrap(self):
        con = requests.get(self.page_url)
        soup = BeautifulSoup(con.content, 'lxml')
        #print(soup)

        infoTable = soup.find("table", {"class":"wikitable sortable"})
        infoPrint = []
        for i in infoTable.find_all('tr'):
            infolist = []
            for j in i.find_all('td'):
                info = j.get_text()
                infolist.append(info)
            infoPrint.append(infolist)
        print(infoPrint)


    @staticmethod
    def main():
        wiki = Wikipedia()
        wiki.page_url = "http://dh.aks.ac.kr/Encyves/wiki/index.php/%EC%A1%B0%EC%84%A0_%EC%84%B8%EC%A2%85"
        wiki.scrap()

if __name__ == "__main__":
    Wikipedia.main()