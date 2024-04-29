# ３つの数を比較

# 入力：３つの数字
num1 = 50
num2 = 50
num3 = 50

# 出力1 すべて同じ　"全ての数が同じです"
if num1 == num2 == num3 :
    print("全ての数が同じです")

# 出力2 ２つが同じ　"２つの数が等しい, (_と _)"
elif num1 == num2 or num1 == num3 or num2 == num3 :
    if num1 == num2 :
        print(f"２つの数が等しい, {num1}と{num2}")
    elif num1 == num3 :
        print(f"２つの数が等しい, {num1}と{num3}")
    else :
        print(f"２つの数が等しい, {num2}と{num3}")

# 出力3 すべて違う　"全数が違う、一番大きいのは_です"
else:
    if num1 > num2 and num1 > num3 :
        print(f"全数が違う、一番大きいのは{num1}です")
    elif num2 > num1 and num2 > num3 :
        print(f"全数が違う、一番大きいのは{num2}です")
    else :
        print(f"全数が違う、一番大きいのは{num3}です")
    

