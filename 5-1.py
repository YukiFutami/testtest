# ３つの数の比較－類似性と違いを見つける
# print(), input(), int()のみ使用可

# 入力：ユーザーから３つの整数
number_1 = int(input("첫 번째 수 입력: "))
number_2 = int(input("두 번째 수 입력: "))
number_3 = int(input("세 번째 수 입력: "))

# 出力1:全ての数が同じであれば、すべての数が同じです。
if number_1 == number_2 == number_3 :
    print("모든 수가 같습니다.")

# 出力2:全ての数が違うと、全数が違う、Xです。Xは最大の数値
elif number_1 != number_2 != number_3 != number_1 :
    max_number = max(number_1, number_2, number_3)
    print("모든 수가 다릅니다. 가장 큰 수는", max_number,"입니다.")

# 出力3:２つの数が等しい場合は、２つの数が等しいです。（〇と　〇）
else :
    if number_1 == number_2 :
        print("두 수가 같습니다.", number_1,"와", number_2)
    elif number_2 == number_3 :
        print("두 수가 같습니다.", number_2,"와", number_3)
    elif number_1 == number_3 :
        print("두 수가 같습니다.", number_1,"와", number_3)



