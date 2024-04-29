# 교수님 해설 시간의 해답
# text = input("문자열을 입력하세요: ")
# 入力:住民番号を入力してもらう

# 住民番号データ 13桁の数字で構成されている

# 番号を乗算[2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# 全ての合計を出す
input_number = "990295-1234567" 
check_number = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

sum = 0
count = 0
for num in input_number :
    if num != "-" and count < 12 :
        sum += int(num) * check_number[count]
        count += 1

# 結果を11で割った残りを、１１から引く、結果が２桁の場合１０桁は捨てて１桁のみ(%10)
# (11 - (sum % 11)) % 10 == input_number[-1]
check_value = (11 - (sum % 11)) % 10 == input_number[-1]

# 最終結果が住民番号の最後の数字と一致すると有効な住民番号
# 出力:有効な住民番号です　or 有効でない住民番号です
if check_value == int(input_number[-1]):
    print("有効な住民番号です")
else :
    print("有効でない住民番号です")