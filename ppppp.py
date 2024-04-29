# 面接単位変換器

# １平方メートル　＝　10.7639平方フィート
def convert_to_square_feet(square_meters):
    feet = square_meters * 10.7639
    return feet

# １エーカー　＝　4046.86平方メートル
def convert_to_square_acres(square_meters):
    acres = square_meters / 4046.86
    return acres 

# 入力
square_meters = float(input("土地の面積を平方メートル単位で入力： "))

if square_meters < 0 :
    print("無効な入力です。")

else :
    print(square_meters, "平方メートルは", convert_to_square_feet(square_meters), "平方フィートです")
    print(square_meters, "平方メートルは", convert_to_square_acres(square_meters), "エーカーです。")


