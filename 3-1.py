# 사전 예약 시스템 시뮬레이터 작성
# E1、満１８歳以上のみ予約可能
def event_code_1(age):
    return age >= 18
# E2、すべての年齢層が可能、しかし日付は偶数のみ予約できる
def event_code_2(reservation_date):
    return reservation_date % 2 == 0
# E3、16歳以上のみ、7の倍数の日付のみ予約できる
def event_code_3(age,reservation_date):
    return age >= 16 and reservation_date % 7 == 0
# 사용자로부터 나이를 입력 받기
age = int(input("나이를 입력하세요: "))
event_code = str(input("예약하려는 이벤트 코드를 입력하세요: "))
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

if reservation_date < 0 or reservation_date >= 30 :
    print("無効な入力です。予約できません。")
elif event_code == "E1":
    if event_code_1(age):
        print("予約が完了しました")
    else :
        print("年齢制限のため予約できません")
elif event_code == "E2":
    if event_code_2(reservation_date):
        print("予約が完了しました")
    else :
        print("選択した日付には予約できません")
elif event_code == "E3":
    if event_code_3(age, reservation_date):
        print("予約が完了しました")
    else :
        if not age >= 16 :
            print("年齢制限のため予約できません")
        if not reservation_date % 7 == 0 :
            print("選択した日付には予約できません")
else :
    print("無効な入力です、プログラムを終了します")



