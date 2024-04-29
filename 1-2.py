line1 = int(input("첫 번째 변의 길이를 입력하세요: "))
line2 = int(input("두 번째 변의 길이를 입력하세요: "))
line3 = int(input("세 번째 변의 길이응 입력하세요: "))

# 삼각형을 만들수 있는지?:
if line1 + line2 > line3 and line2 + line3 > line1 and line3 + line1 > line2:
    # 세 변의 길이가 모두 같다 : 정삼각형
    if line1 == line2 == line3:
        print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다. ")

    # 세 변 증 두 변의 길이가 같다 : 이등변삼각형
    elif (line1 == line2 ) or (line2 == line3) or (line1 == line3) :
        print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다. ")

    # 세 변의 길이가 모두 다르다 : 부등변삼각형
    else:
        print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다. ")

    # 어느 변의 길이 합이 나머지 한 변의 길이보다 작거나 같다면, 삼각형을 형성할 수 없다
    # 왜 만들 수 없는지 이유를 포함한 메시지를 출력
else :
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다. ")
    print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다. ")