#todoList
#todos.py

print("====== 투두 리스트 ======")

todos = {}
index=0
print(todos)

while True:
    print("1.등록\t 2.수정\t 3.삭제\t 4.일정목록\t 5.전체삭제\t 6.종료")
    num = int(input("메뉴를 선택하세요: "))
    if num==6:
        print("프로그램이 종료되었습니다")
        break
    elif num==1:
        index += 1
        todos_value = str(input("벨류값 : ")) 
        todos[index] = todos_value
        # print(todos)
    elif num==3:
        index_tmp = int(input("삭제할 일정 번호 입력 : "))
        del todos[index_tmp]
    elif num==4:
        print(todos)
    elif num==2:
        index_tmp = int(input("수정할 일정 번호 입력 : "))
        todos_value = str(input("수정할 내용 입력 : "))
        todos[index_tmp] = todos_value
    elif num==5:
        index=0
        todos.clear()
    else:
        print("잘못된 번호 입력입니다")
