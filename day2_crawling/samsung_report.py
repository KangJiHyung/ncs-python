from konlpy.tag import Okt                  # 비정형 데이터를 정형화 시킬 때 사용하는 패키지
from nltk.tokenize import word_tokenize     # 단어를 구분자를 이용하여 자를 때 사용하는 패키지
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class SamsungReport(object):

    def __init__(self):
        self.okt = Okt()

    def read_file(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = "./data/kr-Report_2018.txt"              # '.' : 현재위치
        with open(filename, "r", encoding="utf-8") as f:    # "삼성전자 글로벌센터 전자사업부"라는 파일을 utf8 인코딩으로 읽겠다
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')             # 줄바꿈 문자를 공백으로 변환
        tokenizer = re.compile(r'[^ ㄱ-힣]+')        # 한글인 것만 추출? 한글이 아닌 문자에 대해서는 삭제?
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    def download():
        nltk.download()

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        return tokens

    # konlpy에 한국어사전이 내장되어 있음
    # 사전적 의미를 갖는 명사 추출
    def extract_noun(self):
        noun_tokens = []
        # 영어사전에서 보면, computer Noun. com...
        tokens = self.change_token(self.extract_hangeul(self.read_file()))
        for token in tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']    # 두번째 단어가 Noun이면 이 앞의 단어는 "명사"라 판단
            if len(''.join(temp)) > 1:
                noun_tokens.append("".join(temp))
        texts = " ".join(noun_tokens)       # 명사들을 다시 한 줄로 합치는데 단어와 단어 사이에 공백
        return texts

    @staticmethod
    # stopword.txt : 보고서의 내용과 관련없는 단어들을 모아둔 파일
    def read_stopword():
        stopfile = './data/stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        return stopwords

    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
        stopwords = self.read_stopword()
        texts = [text for text in tokens if text not in stopwords]      # stopword에 없는 단어들만 리스트에 저장
        return texts

    def hook(self):
        texts = self.remove_stopword()
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)     # 단어의 빈도수를 체크하여 내림차순으로 정렬
        print(freqtxt[:30])     # 리스트에서 30개만 출력
        return freqtxt

    def draw_wordcloud(self):
        texts = self.remove_stopword()
        wcloud = WordCloud('./data/D2Coding.ttf', relative_scaling=0.2, background_color='white').generate(" ".join(texts))
        plt.figure(figsize=(10, 10))    # 이미지 사이즈
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    @staticmethod
    def main():
        #SamsungReport.download()
        samsung = SamsungReport()
        # samsung.hook()
        samsung.draw_wordcloud()

if __name__ == "__main__":
    SamsungReport.main()