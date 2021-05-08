'''
    opp/contacts.py의 간소화 버전
'''
class Contacts:

    # 메모리의 필드영역
    # python의 Getter, Setter 간소화
    name    = ''
    phone   = ''
    email   = ''
    address = ''

    # String 메소드 간소화
    def __str__(self):
        # f'~\n 에서 바로 엔터하게 되면 형식 자동생성
        return '----------------\n'\
               f'이름 : {self.name} \n' \
               f'전화번호 : {self.phone} \n' \
               f'이메일 : {self.email} \n' \
               f'주소 : {self.address} \n' \
               '----------------'


class ContactsService:

    def set_contacts(self):
        obj = Contacts()
        obj.name = input(">> 이름을 입력해 주세요 : ")
        obj.phone = input(">> 전화번호를 입력해 주세요 : ")
        obj.email = input(">> 이메일을 입력해 주세요 : ")
        obj.address = input(">> 주소를 입력해 주세요 : ")
        return obj

    def get_contacts(self, contList):
        for info in contList:
            print(info)

    def del_contacts(self, contList, name):
        for i, j in enumerate(contList):  # i = index, j = element 리스트내부의 주소
            if j.name == name:
                del contList[i]

    def print_menu(self):
        print("1. 연락처 입력 \n"
              "2. 연락처 출력 \n"
              "3. 연락처 삭제 \n"
              "4. 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        service = ContactsService()
        while 1:
            menu = service.print_menu()
            if menu == 1:
                t = service.set_contacts()
                ls.append(t)
            elif menu == 2:
                service.get_contacts(ls)
            elif menu == 3:
                name = input("삭제할 이름 : ")
                service.del_contacts(ls, name)
            elif menu == 4:
                break

if __name__ == '__main__':
    ContactsService.main()