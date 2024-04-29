
def event_code_1(age):
    age1 = age >= 18
    return age1

def event_code_2(reservation_date):
    date1 = reservation_date % 2 == 0
    return date1

def event_code_3(age,reservation_date):
    dateAge = age >= 16 and reservation_date % 7 == 0
    return dateAge

age = int(input("年齢を入力してください"))
event_code = input("予約したいイベントコードを入力してください")
reservation_date = int(input("希望する日にちを入力してください"))

if reservation_date < 1 and reservation_date > 30 :
    print("無効な入力です。予約できません")

if event_code == "E1":
    if event_code_1(age):
        print("予約が完了しました")
    else :
        print("年齢制限のため予約できません")
elif event_code == "E2":
    if event_code_2(reservation_date) :
        print("予約が完了しました")
    else :
        print("選択した日付には予約できません")
elif event_code == "E3":
    if event_code_3(age, reservation_date):
        print("予約が完了しました")
    elif not event_code_3(age, reservation_date):
        print("年齢制限のため予約できません")
    else :
        print("選択した日付には予約できません")
else :
    print("無効な入力です、プログラムを終了します。")


