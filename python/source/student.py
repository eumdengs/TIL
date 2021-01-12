import os.path

students = []

#수강생 등록 : list students에 정보를 저장하고 message를 리턴
def register(student):
    index = is_exist(student["id"])
    if index < 0:
        students.append(student)
        return "{0}(이)가 등록되었습니다".format(student["name"]) 
    else:
        return "이미 등록된 정보입니다"

#수강생 목록 : list students 목록 리턴
def getAllStudents():
    return students


#수강생 수정 : id를 검색해서 전공정보를 수정하고 message를 리턴
def update(id, major):
    index = is_exist(id)
    if index > -1:
        student[index]["major"] = major
        return "{0}의 전공 정보가 수정되었습니다".format(id)
    else :
        return "{0}의 전공 정보가 존재하지 않습니다".format(id)



#수강생 삭제 : id를 검색해서 수강생 정보 삭제 message 리턴
def remove(id):
    index = is_exist(id)
    if index >-1:
        student.pop(index)
        return "{0}의 정보가 삭제되었습니다".format(id)
    
    else :
        return "{0} 정보가 존재하지 않습니다".format(id)


#수강생 존재여부 : id를 검색해서 list student의 index 값 리턴
def is_exist(id):
    for index, student in enumerate(students):
        if student["id"] == id:
            return index
    return -1

#menu display
def menu_display():
    print("-----수강관리-----")
    print("1. 수강생 정보 등록")
    print("2. 수강생 목록 보기")
    print("3. 수강생 정보 수정")
    print("4. 수강생 정보 삭제")
    print("0. 종료")

#message display
def message_display(message):
    print(message)

#프로그램 종료시 list students "students.dat" 파일 저장
def save_list():
    save_file = open("students.dat", "w")   #초기화되기 때문
    for index, student in enumerate(students):
        save_file.write("{0}번째 | {1} ,{2}, {3}, {4}\n".format(index, student["id"], student["name"], student["age"], student["age"]))
    save_file.close()


#프로그램 시작시 "students.dat" 파일이 존재하고 정보가 있는 경우 list students 초기화
def init_data_load():
    fileExist = os.path.isfile("students.dat")
    if fileExist :
        read_file = open("students.dat", "r")
        while True:
            student = read_file.readline()
            if len(student.split("|") == 2):
                student = data.split("|")[1].strip("\n").split(",")
                students.append("id":student[0].strip(), "name":student[1].strip(), "age":int(student[2].strip()), "major":student[3].strip())
            if not data : break
        read_file.close()    


init_data_load()
while True:
    menu_display()
    menu = input("메뉴를 선택하세요 : ")

    if menu =="1":
        id = input("학번 : ")
        name = input("이름 : ")
        age = input("나이 : ")
        while not age.isdecimal():
            print("나이는 숫자로 입력하세요")
            age =input("나이 :")
        major = input("전공 : ")
        student = {"id":id, "name":name, "age":int(age), "major":major}
        message_display(register(student))

    elif menu == "2":
        print("수강생목록보기")
        print(students)

    elif menu == "3":
        id = input("수정할 수강생 번호 : ")
        major = input("수정할 전공 : ")
        message_display(update(id, major))
    
    elif menu =="4":
        id = input("삭제할 수강생 번호 : ")
        message_display(remove(id))
    elif menu =="0":
        message_display("수강관리 프로그램 종료")
        break
    else:
        print()
        message_display("1,2,3,4,0번 중 선택하세요")
