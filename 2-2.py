# 세 과목 점수를 입력 받아 평균 점수를 계산
# 평균에 따른 학점 등급을 부여

# 평균 점수를 계산하고 학점 등급을 반환하는 코드를 작성
def calculate_average(math_score, science_score, english_score):
    total_score = math_score + science_score + english_score
    average_score = total_score / 3
    return average_score

def determine_grade(avarage_score):
    if avarage_score >= 90:
        return "A"
    elif avarage_score >= 80:
        return "B"
    elif avarage_score >= 70 :
        return "C"
    elif avarage_score >= 60:
        return "D"
    else :
        return "F"

# 사용자로부터 수학,과학,영어의 점수를 입력받는
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

# 평균 계산
avarage_score = calculate_average(math_score, science_score, english_score)
# 학점 등급 출력
grade = determine_grade(avarage_score)

# 결과 출석
print("평균 점수는", avarage_score,"점이고, 학점은", grade,"입니다.")
