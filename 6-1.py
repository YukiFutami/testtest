# msg 출력
msg = "프로그램 시작"
print(msg)

# 함수3:bar(argB1("정영절"),argB2("YC Jung"))에 대입
def bar (argB1, argB2):
    msg1 = "안녕!" + foo(argB1) # msg1 = "안녕! foo(정영절)" 
    print(msg1)  # "안녕!" + "*" + argB1 + "님" + "*"

    msg2 = "hello!" + foo(argB2) # msg2 = "hello! foo(YC Jung)" 
    print(msg2) # "hello!" + "*" + argB1 + "님" + "*"

# foo 이란? 함수2확인
# 함수2:foo(argF)애 foo(argB1),foo(argB2)에 대입
def foo(argF):
    msg = argF + "님" # foo = argB1 + "님", argB2 + "님"
    msg = pos (msg) # pos(argB1 + "님")
    return msg # "*" + argB1 + "님" + "*"

# pos 이란? 함수1확인
# 함수1:pos(argP)에 pos(msg)를 대입
def pos(argP):
    msg = "*" + argP + "*" # "*" + pos(msg) + "*"
    return msg # "*" + msg + "*"

bar ("정영절", "YC Jung")

# msg 출력
msg = "프로그램 종료"
print(msg)

