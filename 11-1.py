# パスワードジェネレーター
# ユーザーから長さを入力し、その長さのランダムなパスワードを生成する関数generate_passwordを実装
# 大文字、小文字、数字を組み合わせてパスワードを生成する

import random # モジュールをインポート、このモジュールはランダムな選択を行うための関数を提供

def generate_password(length): 
# 関数の定義、この関数は長さを引数として受け取り、指定された長さのランダムなパスワードを生成
    uppercase_letters = 'ABCDEFGHIJKMNOPQRSTUWXYZ' # 大文字のアルファベットを表す文字列
    lowercase_letters = uppercase_letters.lower() # 大文字を小文字に変換し、小文字を表す文字列
    digits = '0123456789' # 数字を表す文字列
    all_characters = uppercase_letters + lowercase_letters + digits 
# 大文字、小文字、数字を結合してすべての文字を表す文字列を定義
    password = " " # 空の文字列passwordを初期化

    for _ in range(length): # パスワードの長さに対してループを開始
        password += random.choice(all_characters)
# all_charactersからランダムに１文字ずつ選択し、passwordに追加
    return password #生成されたランダムなパスワードを返す

# 例外：長さを入力したいときのコード
#length = int(input("希望のパスワードの長さを入力してください: "))
generate_password = generate_password(8)
print(generate_password)