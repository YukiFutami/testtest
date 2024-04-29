# 図書館利用権判別機

#　子供利用券：１２歳以下
#　青少年利用券：１３歳から１８歳まで
#　大人利用券：１９歳以上
def main(ticket):
   # ticket = int(ticket)
    if ticket <= 12 :
        return "子供利用券"
    elif ticket >= 13 and ticket <= 18 :
        return "青少年利用券"
    else :
        return "大人利用券"

ticket = int(input("年齢を入力: ")) #intをここに入れてもよい

Applicableticket = main(ticket)
print(Applicableticket)

