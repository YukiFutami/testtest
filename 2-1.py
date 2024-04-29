# 使用者が平方メートル(m²)単位で入力した土地の面積を平方フィートとエーカー単位に変換するプログラム
#  1平方メートル (m²) = 10.7639 平方フィート (ft²)
# 1エーカー(ac) = 4046.86平方メートル(m²)

# 使用者から土地の面積を平方メートル(m²)単位で入力されます。
input_square_meters = float(input("土地の面接を平方メートル単位で入力："))

# 2 つの関数を定義して、各単位への変換を担当します:
def convert_to_square_feet(square_meters):
    feet =  square_meters * 10.7639
    return feet

def convert_to_square_acres(square_meters):
    acres =  square_meters / 4046.86
    return acres

feet = convert_to_square_feet(input_square_meters)
acres = convert_to_square_acres(input_square_meters)

if input_square_meters > 0:
    print(input_square_meters,"平方メートルは",feet,"です")
    print(input_square_meters,"平方メートルは", acres,"です。")

else :
    print("間違っています")


    