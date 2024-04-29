# 출석 점수 프로그램

# 주당 수업 시간(시수/주), 결석한 총 시간, 지각 횟수를 계산하는 함수
# 出席点数を求める計算式
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    # 총 수업 시간 계삼법: 시수 / 주 * 15
    #　週の授業時間
    total_hours_per_week = hours_per_week * 15 

    # 지각 3화는 결석 1시간으로 처리
    # トータル欠席数の式
    total_absence_hours = absence_hours + ( tardy_count // 3 )


    # 출석점수 계산법: 20점에서 결석시간에 비례하는 점수를 차감합니다
    # 계산식: 20점 - (20 * 결석시간 수 / 총 수업시간 수)
    # 出席点数の計算式
    attendance_score =  20 - (20 * total_absence_hours / total_hours_per_week)
    return round (attendance_score, 2)

# 입력: 주당 수업 시간(시수/주), 결석한 총 시간, 지각 횟수를 입력 받기
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

total = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)

# 결석시수가 총 수업시수의 1/4을 초과할 경우 학점 미부여(F처리)
if absence_hours > hours_per_week * 15 / 4 :
    print("당신의 출석 점수는 F(単位未付与) 점입니다. ")
else :
    print(f"당신의 출석 점수는 {total} 점입니다. ")

# 출력 결과 방법2
if absence_hours > hours_per_week * 15 / 4 :
    result = "F"
else :
    result = total

print(f"당신의 출석 점수는 {result} 점입니다. ")
