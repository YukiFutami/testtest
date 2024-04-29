# password 검증기

# 安全基準　満たさない場合はパスワードは安全ではない
# 1)長さは８文字以上
# 2)１つの数字が必要
# 3)１つの大文字が必要

# 出力
# 1)全てが満たされている場合:パスワードは安全です
# 2)そうでない場合:パスワードは安全ではありません

def text(password):
    digit = False
    uppecase = False
    lengh = False

    if len(password) >= 8 :
            lengh = True

    for num in password:
        if num.isdigit():
            digit = True
        if num.isupper():
            uppecase = True
        
    return digit and uppecase and lengh

# 入力
password = input("希望パスを入力")

if text(password):
    print("安全です")
else :
    print("安全ではないです")
