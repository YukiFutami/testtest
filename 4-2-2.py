# 입력 값
password = "abcdefHIJK"

# 조건:비밀번호는 8자 이상
def password1(password):
    return len(password) >= 8               

# 조건:하나의 숫자가 포함되다
def password2(password):
    for num in password:
        if num.isdigit():
            return True
    return False

# 조건:하나의 대문자가 포함되다
def password3(password):
    for num in password:
        if num.isupper():
            return True
    return False

# 출력 :
if password1(password) and password2(password) and password3(password) :
    print("비밀번호가 안전합니다.")
else:
    print("비밀번호가 안전하지 않습니다.")