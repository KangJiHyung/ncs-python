# 교재 p.72
'''
    클래스에 학생의 이름을 입력하면
    해당 학생이 얻은 국어, 수학, 영어 3과목의 평균점수에 따라 A ~ F까지 출력하시오.
'''
class Grade:
    def __init__(self, name):
        self.name = name
        self.marks = []     # list로 초기화

    # 점수 저장
    def addMarks(self, mark):
        self.marks.append(mark)

    # 점수 평균
    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def main():
        # 학생이름 입력받기
        student = Grade(input('>> 학생이름 입력 : '))
        # 과목 점수 입력받기
        for subject in ['국어', '수학', '영어']:
            student.addMarks(int(input('- ' + subject + '점수 입력 : ')))
        # 과목 평균 출력하기
        avg = student.avg()
        print(f'{student.name}의 과목 평균은 {int(avg)}점 입니다.')

        # 학점 매기기
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"
        # 학점 출력하기
        print(f'{student.name}의 학점은 {grade} 입니다.')


if __name__ == '__main__':
    Grade.main()