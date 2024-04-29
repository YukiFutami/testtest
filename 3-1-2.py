# 사용자로부터 나이를 입력 받기
age = int(input("나이를 입력하세요: "))
# 사용자가 예약하는 이벤트 코드(event_code) : E1 , E2 , E3
event_code = str(input("예약하려는 이벤트 코드를 입력하세요: "))
# 사용자로부터 원하는 예약 날짜를 입력받기
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

if reservation_date <= 1 or reservation_date >= 30 :
      print("無効な入力です。プログラムを終了します。")

elif event_code == "E1":
        if age >= 18 :
             print("予約が完了しました")
        else :
             print("年齢制限のため予約できません")

elif event_code == "E2":
        if reservation_date % 2 == 0 :
             print("予約が完了しました")
        else :
             print("選択した日付には予約できません")

elif event_code == "E3":
        if age >= 16 and reservation_date % 7 == 0 :
             print("予約が完了しました")
        elif age <= 16 :
             print("年齢制限のため予約できません")
        else :
             print("選択した日付には予約できません")
else :
      print("無効な入力です。プログラムを終了します。")
      



"""
# 사전 예약 시스템 시뮬레이터 작성

# E1、満１８歳以上飲み予約可能
def event_code_1(age):
    return age >= 18

# E2、すべての年齢層が可能、しかし日付は偶数のみ予約できる
def event_code_2(reservation_date):
    return reservation_date % 2 == 0

# E3、16歳以上のみ、7の倍数の日付のみ予約できる
def event_code_3(age,reservation_date):
    return age >= 16 and reservation_date % 7 == 0



# E1、満１８歳以上飲み予約可能
# E2、すべての年齢層が可能、しかし日付は偶数のみ予約できる
# E3、16歳以上のみ、7の倍数の日付のみ予約できる

"""

