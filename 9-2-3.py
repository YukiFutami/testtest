# 韓国住民番号データ
# 13桁の数字で構成されている

# 入力:住民番号を入力してもらう
text = input("문자열을 입력하세요: ")

# 番号を乗算[2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# checkNumber = [num * mult for num, mult in zip(text, multipliers)]
# print(checkNumber)

# totalNumber = 
for character in text :
    for mult in multipliers :
        result = character * mult
        results.append(result)

print(results)


# 出力:有効な住民番号です　or 有効でない住民番号です

# 全ての合計を出す
# 結果を11で割った残りを、１１から引く、結果が２桁の場合１０桁は捨てて１桁のみ(%10)
# 最終結果が住民番号の最後の数字と一致すると有効な住民番号