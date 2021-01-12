# text data 출력
write_file = open("hello.txt", "w")
write_file.write("Hello Python... \n")
write_file.close() # 자원반납 -> 메모리 누수

# with open(파일명, 모드) as 파일객체
# 모드 : "w", "a"(appen write), "r"
# 자원반납 필요없이 사용이 가능하다
with open("hello.txt", "a") as file:
    file.write("File Write Test")
    

# file read => console 출력
with open("hello.txt", "r") as read_file:
    print(read_file.read())

# console 입력 => file 출력
read_data = input("파일에 저장할 데이터 입력: ")
with open("console input.txt", "w") as console_file:
    console_file.write(read_data)

# file 입력 => file 출력(copy)
file_read = open("hello.txt", "r")
file_copy = open("hello_copy.txt", "w")
file_copy.write(file_read.read())
file_read.close()
file_copy.close()