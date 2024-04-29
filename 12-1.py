"""
# 가위,바위,보 게임
# 입력:가위,바위,보 중 하나를 선택
# 컴퓨터의 선택은 난수 발생을 이용해서 결정

usuer = input("가위,바위,보 중 하나를 선택하세요: ")

import random

choices = ["가위","바위","보"]
computer_choice = random.choice(choices)
print("computerChoice : ", computer_choice)

#もし入力値がはさみでチョイスもはさみならあいこ
if usuer == computer_choice:
    print("aiko")
else :
    print("make")
"""

import random

def janken():
    hands = ["グー","チョキ","パー"]
    player_hand = input("あなたの手を選んでください")
    computer_hand = random.choice(hands)

    print("コンピューターの手: ", computer_hand)

    if player_hand  not in hands :
        print("入力が正しくありません")
    elif player_hand == computer_hand:
        print("あいこです")
    elif (player_hand == "グー" and computer_hand == "チョキ") or \
         (player_hand == "チョキ" and computer_hand == "パー") or \
         (player_hand == "パー" and computer_hand == "グー"):
        print("勝ちです")
    else :
        print("負けです")


janken()


 
