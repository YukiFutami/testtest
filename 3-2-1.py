# 出席点数の計算方法を関数にまとめる
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    total_class_hours = hours_per_week * 15

    total_absence_hours = absence_hours + tardy_count // 3   # += tardy_count // 3

    attendance_score = 20 - (20 * total_absence_hours / total_class_hours )

    return round (attendance_score, 2)  # 小数点第二桁まで丸める

# 週当たりの授業時間（時数/週）
hours_per_week = int(input("週の授業時間を入力せよ"))
# 欠席した合計時間
absence_hours = int(input("欠席した時間を入力せよ"))
# 遅刻の回数を入力
tardy_count = int(input("遅刻の回数を入力せよ"))

score = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)

if score < 0 or absence_hours > hours_per_week * 15 / 4 :
    result = "F(単位未付与)"

else :
    result = score

print("あなたの出席スコアは",result,"点です。")

