# 仮想株式シミュレーション　def使用なし

# 入力1:初期資本金
initial_capital = float(input("초기 자본금: "))
# 入力2:株式の購入価格
purchase_price_per_share = float(input("주식의 구매 가격: "))
# 入力3:購入する株式の数
number_of_shares_to_purchase = float(input("구매할 주식의 수: "))
# 入力4:販売時の株価
selling_price_per_share = float(input("판매할 때 주식 가격: "))

# 株式購入費用の計算:購入の総費用 = 購入価格*株式数
total_purchase_cost = purchase_price_per_share * number_of_shares_to_purchase

# 残りの資本金の計算:株式購入後に残った資本金（出力）= 初期資本金-購入の総費用
remaining_capital = initial_capital - total_purchase_cost

# 売上予想利益の計算: 売上総額 = 販売時の株価*在庫数　予想利益または損失 = 売上総額 - 購入の総費用
total_sales = selling_price_per_share * number_of_shares_to_purchase
expected_profit_or_loss = total_sales - total_purchase_cost

# 出力1：購入後残りの資本金、小数点第二まで
# 出力2:予想利益または損失、小数点第二まで
print("구매 후 남은 자본금: {:.2F} ".format(remaining_capital)) # {:.2F} .formatに変更追加
print("예상 이익: {:.2F}".format(expected_profit_or_loss)) #{:.2F} .formatは小数点第二までの制度で出力

# 出力3: 利益が発生：予想される利益です。or 予想される損失です。
if expected_profit_or_loss >= 0:
    print("예상되는 이익입니다.")
else :
    print("예상되는 손실입니다.")



