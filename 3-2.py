# 関数を作る
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    total_hours = hours_per_week * 15
    total_absence_hours = absence_hours + tardy_count // 3
    atendance_score = 20 -(20 * total_absence_hours / total_hours)
    return round (atendance_score, 2)

# ユーザー入力
hours_per_week = int(input("週替わり授業時間を入力"))
absence_hours = int(input("欠席した総時間を入力せよ"))
tardy_count = int(input("遅刻回数を入力せよ"))  

if calculate_attendance_score(hours_per_week, absence_hours, tardy_count) < 0 or absence_hours > hours_per_week * 15 / 4 :
    print("あなたの出席スコアはF(単位未付与)です. ")
else :
    print("あなたの出勤スコアは", calculate_attendance_score(hours_per_week, absence_hours, tardy_count),"点です。")
