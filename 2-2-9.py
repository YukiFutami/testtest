# 평균 점수와 학점 등급 계산 프로그램

# 세 과목(수학, 영어, 과학) 점수를 입력받아 평균 점수를 계산
# 평균에 따른 학점 등급을 부여

# 평균 점수를 계산하고
# 평균 점수를 바탕으로  학점 등급을 결정하는 함수
def calculate_average(math_score, science_score, english_score):
    average = (math_score + science_score + english_score) / 3
    if average >= 90:
        print(f"평균 점수는 {average}점이고, 학점은 A임니다. ")
    elif average >= 80 and average < 90 :
        print(f"평균 점수는 {average}점이고, 학점은 B임니다. ")      
    elif average >= 70 and average < 80 :
        print(f"평균 점수는 {average}점이고, 학점은 C임니다. ")  
    elif average >= 60 and average < 70 :
        print(f"평균 점수는 {average}점이고, 학점은 D임니다. ")
    else :
        print(f"평균 점수는 {average}점이고, 학점은 F임니다. ")


# 세 과목(수학, 영어, 과학) 점수를 입력
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

calculate_average(math_score, science_score, english_score)
