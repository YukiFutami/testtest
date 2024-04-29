# 三角形タイプ判別プログラム

# 三辺の長さがすべて同じ：正三角形
# 二辺の長さが同じ：二等辺三角形
# 三辺の長さがすべて違う：不当辺三角形
# 二辺の長さの合計が1辺の長さより短い場合："三角形を形成することはできません"と出力
def total_triangle(triangle1, triangle2, triangle3):
    # total_triangle = int(triangle1, triangle2, triangle3)
    if triangle1 + triangle2 <= triangle3 or triangle1 + triangle3 <= triangle2 or triangle2 + triangle3 <= triangle1 :
        print("入力した値では三角形を作ることはできません")
        print("三角形を作るには二つの辺の合計が違う一つの辺より長くてはいけません")
    elif triangle1 == triangle2 == triangle3 :
        print("正三角形")
    elif triangle1 == triangle2 or triangle1 == triangle3 or triangle2 == triangle3 :
        print("二等辺三角形")
    else :
        print("不当辺三角形")
    

triangle1 = int(input("1辺目の長さを入力してください"))
triangle2 = int(input("1辺目の長さを入力してください"))
triangle3 = int(input("1辺目の長さを入力してください"))

total_triangle(triangle1, triangle2, triangle3)


