
# 空白に基づいて文字列内の特定の単語の出現頻度を計算する
# 입력: 문자열 입력
text = input("문자열 입력: ")

# 입력: 확인하는 단어를 입력
check_word = input("단어 입력: ")

count = 0

# 조건: 함수는 input , output , 형변환 함수만 사용
# 각 단어를 추출할 때마다 입력받은 특정 단어와 비교하고 카운트하다
for word in text.split():
    if word == check_word :
        count += 1
    

print("단어",check_word,"의 출현 번도: ",count)






"""
# 출력:count값

text = input("문자열 입력: ")

# 입력: 확인하는 단어를 입력
check_word = input("단어 입력: ")

countWord = text.count(check_word)
print(f"単語",check_word,"の出現回数は:{}".format(countWord))
"""
