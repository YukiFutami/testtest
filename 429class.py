# #정수와 부동 소수점 수 연산
# num_int = 10
# num_float = 3.14

# # 연산 수행
# result = num_int + num_float # 점수와 부등 소수점 수의 합

# # result = float(num_int) + num_float # 여기에 이 계산식이 들어가다

# print("결과: ", result) # 출력: 결과: 3.14
# print("결과의 자료형: ", type(result)) # 출력: 결과의 자료형: <class 'float'>

# # 산술 연산자: 수(Number)를 계산하는 연산자
# # 시칙 연산자 포함: 더하기(+), 빼기(-), 곱하기(*), 나누기(/)

# # 더하기: 정수와 정수의 합
# result_1 = 100 + 90

# # 빼기: 정수와 실수의 차
# result_2 = 13 - 1.25

# # 곱하기: 정수의 곱
# result_3 = 13 * 13

# # 나누기: 정수의 나눗셈 결과는 실수
# result_4 = 9 / 3

# print(result_1, result_2, result_3, result_4)

# print(type(result_1), type(result_2), type(result_3), type(result_4))

# 산술연산자
# +, -, *, /

# bar = 4
# foo = 2

# print(bar + foo)
# print(bar - foo)
# print(bar * foo)

# print(bar / foo)
# print(float(bar) / float(foo))

# print(3 / 2)
# print(3 % 2)
# print(3 // 2)

# print(2 ** 3) # 2^3 -> 2*2*2 

# # 목시적 형번환
# print(type(2 + 3.0)) # Output result: <class 'float'>
# # type conversion!! : 2 + 3.0 -> float(2) + 3.0

# #　ここでどのような問題が起こるか
# # Binary operationで、左右に矢印が向いたとき両サイドの数値が違うため問題が起きる

# # 2   + 3.0
# # int + float -> float
# # float ? (int -> float) 형을 변환한다. type conversion(형변환)

# input_str = input("정수를 입력하세요: ")

#                             # 명시적 형변환
# input_int = int(input_str)  # type conversion!!
# # input_str: str -> integer by using int() function

# print(2 + "3")

for value in range(1, 11):
    print(str(value) + "入力")