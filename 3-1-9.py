# 사전 예약 시스템 시뮬레이터

# 입력: 나이 age
age = int(input("나이를 입력하세요: "))

# 입력: 이벤트코드 event_code 'E1','E2','E3'중 하나
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")

# 입력: 날짜 reservation_date 1부터 30까지
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# event_code 조건
# E1:만 18세 이상 예약 가능하다
if reservation_date < 0 or reservation_date >= 30 :
    print("잘못된 입력입니다. 프로그램을 종료합니다")
elif (event_code == "E1" and age >= 18) or \
     (event_code == "E2" and reservation_date %2 == 0) or \
     (event_code == "E3" and age >= 16 and reservation_date %7 == 0 ) :
      print("예약이 완료되었습니다! ")
elif (event_code == "E1" and age < 18) or (event_code == "E3" and age < 16) :
    print("나이 제한으로 인해 예약할 수 없습니다. ")
elif (event_code == "E2" and not reservation_date %2 == 0) or \
     (event_code == "E3" and not reservation_date %7 == 0) :
    print("선택하신 날짜에는 예약할 수 없습니다. ")
else :
    print("잘못된 입력입니다. 프로그램을 종료합니다. ")




# elif not event_code == "E1" and age >= 18 :
#     print("나이 제한으로 인해 예약할 수 없습니")
# # E2:날짜가 짝수일에만 예약할 수 있다
# elif not event_code == "E2" and reservation_date %2 == 0:
#     print("선택하신 날짜에는 예약할 수 없습니다")
# # E3:만 16세 이상 ,7의 배수인 날짜에만 예약 가능하다
# elif event_code == "E3" and age < 16 and reservation_date %7 == 0 :
#     print("나이 제한으로 인해 예약할 수 없습니")
# elif not event_code == "E3" and age >= 16 and reservation_date %7 == 0 :
#     print("선택하신 날짜에는 예약할 수 없습니다")
# else :
#     print("잘못된 입력입니다. 프로그램을 종료합니다")

# 출력 결과1:예약 성공: "예약이 완료되었습니다!"
# 출력 결과2:나이 미달: "나이 제한으로 인해 예약할 수 없습니"
# 출력 결과3:날짜 제한: "선택하신 날짜에는 예약할 수 없습니다"
# 출력 결과4:잘못된 입력: "잘못된 입력입니다. 프로그램을 종료합니다"
