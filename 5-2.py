# 星のパターンを描く　上昇と下降
# 自然数Nを受け取り、指定されたパターンで＊を出力

# １行目からN行目まで星の数を１ずつ増加させる
# N行目以降から星の数を減らし、最後の行には＊１個を出力

# 入力:
score = int(input("N 입력: "))

# 星の数を増やすパターン
for i in range(1, score + 1):
    print("*" * i)

# 星の数を減らすパターン
for i in range(score -1, 0, -1):
    print("*" * i)

print("*")





