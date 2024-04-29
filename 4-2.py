# パスワード検証：パスワードが安全かを確認するプログラム def使わない

# 입력：パスワード
password = input("パスワードを入力: ")

# 条件が満たされない場合パスワードは安全ではないと評価する必要がある
# 安全基準1:パスワードの長さは８文字以上
if len(password) >= 8 :
    safety_standards_1 = True
else :
    safety_standards_1 = False

# 安全基準2:少なくとも1つの数字が含まれている必要がある
safety_standards_2 = False
for number in password :
    if number.isdigit():
        safety_standards_2 = True
        break
        
# 安全基準3:少なくとも1つの大文字が含まれている必要がある
safety_standards_3 = False
for word in password :
    if word.isupper():
        safety_standards_3 = True
        break

# 出力1:すべての条件が満たされているとき：パスワードは安全です。
# 出力2:そうでない場合：パスワードは安全ではありません.

if safety_standards_1 and safety_standards_2 and safety_standards_3 :
    print("パスワードは安全です。")
else :
    print("パスワードは安全ではありません。")