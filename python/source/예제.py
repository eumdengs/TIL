import random
hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w") as file:
    for i in range(1000):
        #랜덤한 값으로 변수를 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(150, 200)
        #텍스틀를 쓴다
        file.write("이름 : {}, 몸무게 : {}, 키 : {} \n".format(name, weight, height))
    