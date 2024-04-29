def bar():                    # 1 # 6
    msg1 = "<< " + name       # 7

    msg2 = foo(msg1)          # 8 # 13
    msg2 += " "               # 14

    msg3 = pos(msg2)          # 15 # 20
    msg3 += " "               # 21

    return msg3               # 22 # 23

def foo(argF):                # 2 # 9
    msg = argF + "님"         # 10
    return msg                # 11 # 12

def pos(argP):                # 3 # 16
    msg = argP + "안녕하세요"  # 17
    return msg                # 18 # 19

name = "홍길동"               # 4

result = bar()               # 5 # 24

print(result)                # 25
