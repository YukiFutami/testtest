# 平均スコアと単位評価計算プログラム

# 入力したスコアに基づいて平均スコアを計算
# 平均スコアに基づいて単位評価を計算

def calculate_average(math_score, science_score, english_score):
    total_average = (math_score + science_score + english_score) / 3 
    return total_average

# 入力：数学、科学、英語のスコアを入れる
math_score = float(input("数学の点数: "))
science_score = float(input("科学の点数: "))
english_score = float(input("英語の点数: "))

# 出力結果
average = calculate_average(math_score, science_score, english_score)
print("平均点数は", average,"で、単位は", end=" ") 
# end=" " はprint関数によって出力されるテキストの末尾に使いされる文字列を指定する

if average >= 90 :
    print ("Aです。")
elif  average >= 80 :
    print ("Bです。")
elif  average >= 70 :
    print ("Cです。")
elif  average >= 60 :
    print ("Dです。")
else :
    print ("Fです。")
    
        



