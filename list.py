# list_a = ["1 2 3"]
# print(list_a)
# 출력 결과 : ["1 2 3"]

# 前から　0 1 2 3 4
list_1 = ["a","b","c","d","e"]
list_2 = [1, 2, 3, 4, 5]
# 後ろから　-5 -4 -3 -2 -1 

print(list_1[2]) # 3番目の英字を出力
# 출력 결과 : c
print(list_2[-2]) # 後ろから２番目の数字を出力
# 출력 결과 : 4

#複数の要素を一気にとる場合[:]を使う
print(list_1[:2]) # 先頭から途中（この場合は２番目）までを取る場合
# 출력 결과 : ['a', 'b']
# :2の場合、:までの数、2は３番目のため２番目まで出したい場合は1を入れる
print(list_1[:1]) # 출력 결과 :['a']

print(list_2[2:]) # 途中から末尾までを取る場合 
# 출력 결과 : [3, 4, 5]

