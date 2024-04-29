# 事前予約シミュレーター

# E1 : 18歳以上
def event_code_1(age):
    return age >= 18

# E2 :偶数日付
def event_code_2(reservation_date):
    return reservation_date % 2 == 0

# E3 :１６歳以上、７の倍数の日付のみ
def event_code_3(age, reservation_date):
    return age >= 16 and reservation_date % 7 == 0

# 入力内容：年齢、イベントコード
age = int(input("나이를 입력하세요: "))
event_code = str(input("예약하려는 이벤트 코드를 입력하세요: "))
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 日付は１から30の数字
if  reservation_date <= 1 and reservation_date >= 30:
    print("無効な入力です、プログラムを終了します")

if event_code == "E1":
    if event_code_1(age) and reservation_date:
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
        if not event_code_1(age) :
            print("年齢制限のため予約できません")
        elif not event_code_2(reservation_date) :
            print("選択した日付には予約できません")

else :
    print("無効な入力です、プログラムを終了します")

