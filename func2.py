def sayhello (name, age):
    if age < 14:
        print("안녕 " + name + ". 너는 초등학교에 다니겠구나.")
    elif age < 17:
        print("안녕 " + name + ". 너는 중학교에 다니겠구나.")
    else:
        print("안녕 " + name + ". 너는 고등학교에 다니겠구나")

sayhello ("철수", 9)
sayhello ("영희", 15)
sayhello ("강호", 18)