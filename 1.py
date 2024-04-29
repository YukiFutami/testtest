# 정수를 입력 받아서, 짝수이면 "짝수"를 출력, 짝수가 아니면 아무것도 출력하지 않는다

# number = int(input("입력: "))

# if number % 2 != 0 :
#     pass
# else:
#     print("짝수")
 
# 정수를 입력 받아서, 짝수이면 "짝수"를 출력, 홀수이면 "홀수"를 출력
# 교수님 해설
# number = int(input("입력: "))

# # 1) 
# if number % 2 == 0:
#     print("짝수")
# else :
#     print("홀수")
# # 2)   
# if number % 2 == 0:
#     print("짝수")
# elif number % 2 == 1 :
#     print("홀수")
# # 3)
# if number % 2 == 0:
#     print("짝수")
# if number % 2 == 1 :
#     print("홀수")

# 정수를 입력 받아서, 0이면 "0"를 출력, 0 초과 이면 "양의 정수"라고 출력
# 0 미만이면 "음의 정수"라고 출력

# input_value = int(input("입력:"))

# if input_value < 0 :
#     print("음의 정수")
# elif input_value > 0 :
#     print("양의 정수")
# else :
#     print("0")

# # 교수님 해설
# input_value = int(input("입력:"))
# msg = ""
# if input_value < 0 :
#     msg = "음의 정수"
# elif input_value > 0 :
#     msg = "양의 정수"
# else :
#     msg = "0"

# print(msg)

# # 2) 同じことが反復するときに使用する
# input_value = int(input("입력:"))
# msg = "결과: "
# if input_value < 0 :
#     msg += "음의 정수"
# elif input_value > 0 :
#     msg += "양의 정수"
# else :
#     msg += "0"

# print(msg)

# input_value = int(input("정수 를 입력하세요: "))

# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 60점 이상이면 D
# 50점 이상이면 F

# if input_value >= 90 :
#     print("A")
# elif input_value >= 80 :
#     print("B")
# elif input_value >= 70 :
#     print("C")
# elif input_value >= 60 :
#     print("D")
# else :
#     print("F")

# score = "" 
# if input_value >= 90 :   # 90 <= input_value <= 100 NO!!!!
#     score = "A"          # 90 <= input_value OK!!!!
# elif input_value >= 80 : # 80 <= input_value < 90 OK!!!!
#     score = "B"
# elif input_value >= 70 :
#     score = "C"
# elif input_value >= 60 : # 60 > input_value
#     score = "D"
# else :
#     score = "F"
    
# print(score)

# 1에서 20까지의 정수를 출력하세요

for value in range(1, 21):
    print(value,"\t")

count = 1    
while count < 21:
    print(count,"\t",end="")
    count += 1

