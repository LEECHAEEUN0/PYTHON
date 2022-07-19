class Student: #파이썬에서 클래스란 객체를 찍어내는 틀과 같다.
    def __init__(self, name, grade, student_number, sex, address, phone_number, year): #초기설정 한다.
        self.name = name #이름지정
        self.grade = grade #학년지정
        self.student_number = student_number #학번지정
        self.sex = sex #성별지정
        self.address = address #주소지정
        self.phone_number = phone_number #전화번호지정
        self.year = year #연차지정
    def introduce(self): #지정부분 가져오기
        print("이름은 {}".format(self.name)) #이름 지정부분 가져오기
        print("학년은 {}".format(self.grade)) #학년 지정부분 가져오기
        print("학번은 {}".format(self.student_number)) #학번 지정부분 가져오기
        print("성별은 {}".format(self.sex)) #성별 지정부분 가져오기
        print("주소는 {}".format(self.address)) #주소 지정부분 가져오기
        print("전화번호는 {}".format(self.phone_number)) #전화번호 지정부분 가져오기
        print("연차는 {}".format(self.year)) #연차 지정부분 가져오기
        if year == 1: #연차가 1년일 경우
           print("우와 아기사자다!") #우와 아기사자다! 로 출력

        else: #연차가 1년이 아니면
            print("멋사 {} 년차".format(self.year)) #포멧 연차 지정부분 가져오기
            print("우와 운영진이다!") #우와 운영진이다! 로 출력
    # print("%d 입니다.".format(12))

while True: #반복문
    Class_name = input("객체 명을 입력하시오. (단, 영문으로):") #Class_name 이라는 틀 안에 "객체 명을 입력하시오."를 넣음
    if Class_name == '종료':  #Class_name 틀 안에 "종료"가 입력되면 반복문이 멈춤.
        break #반복문을 멈추는 명령어
    name = input("이름을 입력하시오. (단, 한글로):") #name에 이름을 입력시킴.
    grade = int(input("학년을 입력하시오. (단, 숫자로):")) #grade에 학년을 입력시킴.
    student_number = int(input("학번을 입력하시오. (단, 숫자로):")) #student_number에 학번을 입력시킴.
    sex = input("성별을 입력하시오. (모를 때는 모른다 라고 입력.):") #sex에 성별을 입력시킴.
    if sex == "모른다": #만약 sex를 모른다고 입력하면
        sex = None #sex는 None이라는 값이 출력됨.
    address = input("주소를 입력하시오. (~시까지만):") #adress에 주소를 입력시킴.
    phone_number = input("전화번호를 입력하시오.(모를 때는 모른다 라고 입력.):") #phone_number에 전화번호를 입력시킴.
    if phone_number == "모른다": #만약 phone_number를 모른다고 입력하면
        phone_number = None #phone_number은 None으로 출력됨.
    year = int(input("멋사 몇년차인가요? (단, 숫자로):")) #year에 연차를 입력시킴.
    Class_name = Student(name, grade, student_number, sex, address, phone_number, year) #Class_name이라는 틀 안에 Student요소들을 배열시킴.
    Class_name.introduce() #Class.name안에있는 요소들을 끌고 올 수 있음.
    print() #출력