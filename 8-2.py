# グローバル変数とローカル変数の使用

#入力:初期値baseValueを入力してグローバル変数として宣言
# グルーバル変数宣言およびユーザーから入力を受ける
baseValue = float(input("기본값을 입력하세요: "))

# 選択肢
print("1 더하기")
print("2 빼기")
print("3 곱하기")
print("4 나누기")

# ユーザーが操作を選択して数値を入力すると、selectOperation()関数で選択した操作をbaseValueに適用
operationNumber = int(input("선택: "))
number_in = int(input("숫자 입력: "))

# selectOperation()関数は、グローバル変数baseValueを参照して演算を実行
def selectOperation():
    if operationNumber == 1 :
        plus = baseValue + number_in
        print("연산 결과: ", plus)
        return plus
    
    elif operationNumber == 2 :
        minus = baseValue - number_in
        print("연산 결과: ", minus)
        return minus
    
    elif operationNumber == 3 :
        multi = baseValue * number_in
        print("연산 결과: ", multi)
        return multi
    
    elif operationNumber == 4 :
        if number_in == 0 :
            print("에러:0으로 나눌 수 없습니다. ")
            return None
        else : 
            divi = baseValue / number_in
            print("연산 결과: ", divi)
            return divi
# 除算操作で分母が0の場合エラーメッセージを出力
# エラーメッセージが出力されていない場合のみ、演算結果を出力する    

selectOperation()


