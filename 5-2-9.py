# 星のパターン

# 1行目からNgyoumemade 星の数を１ずつ増加
# N行目以降から星の数を減らし最後の行には星１個を出力

num = int(input("N入力:"))

for n in range(1, num + 1):
    print("*" * n)

for n in range(num - 1, 0, -1):
    print("*" * n)
    
print("*")
