# 가상 주식 거래 시뮬레이션

# 입력 : 4개
shokisihonnkin = int(input("초기 자본금을 입력하세요: "))
kabusikikounyuugaku = int(input("주식 가격을 입력하세요: "))
kounyuusitakabusuu = int(input("구매할 주식 수를 입력하세요: "))
baikyakunokakaku = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 계산 : 예상 이익 or 손실

# 계산 : 남은 자본금

# 総購入額
total_buy_cost = kounyuusitakabusuu * kabusikikounyuugaku
# 残った資金
total_now_cost = shokisihonnkin - total_buy_cost

# 損益の計算
# 総販売金額
total_sales = baikyakunokakaku * kounyuusitakabusuu
total_cost = total_sales - total_buy_cost

print(f"구매 후 남은 자본금: {total_now_cost:.2F}")
print(f"예상 이익: {total_cost:.2F}")

if total_cost > 0 :
    print("예상되는 이익입니다")
else :
    print("예상되는 손실입니다")




