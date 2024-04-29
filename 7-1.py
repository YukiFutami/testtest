# incrementCount 함수 정의:
# - 전역 변수 count의 값을 1 중가
def incrementCount():              # 1 # 5 # 17 # 23
    global count ;
    count = count + 1              # 6 # 7 # 18 # 19 # 24 # 25

# decrementCount 함수 정의:
# - 전역 변수 count의 값을 1 감소
def decrementCount():              # 2 # 11
    global count ;
    count = count - 1              # 12 # 13

# 전역 변수 count를 1로 초기화
count = 1                          # 3

incrementCount()                   # 4 # 8
print(count)                       # 9

decrementCount()                   # 10 # 14
print(count)                       # 15

incrementCount()                   # 16 # 20
print(count)                       # 21
incrementCount()                   # 22 # 26
print(count)                       # 27
