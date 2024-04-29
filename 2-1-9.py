# 면적 단위 변환기

# 평방피트로 변환
def convert_to_square_feet(square_meters):
    ft = square_meters * 10.7639
    return ft

# 에이커로 변환
def convert_to_acres(square_meters):
    ac = square_meters / 4046.86 
    return ac

# 토지의 면적을 제곱미터 단위로 입력 받기
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

# 함수 호출
ft = convert_to_square_feet(square_meters)
ac = convert_to_acres(square_meters)

# 조건:입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력
# 조건:이를 위해 if 선택문을 활용하기

if square_meters < 0 :
    print("잘못된 입력입니다")
else:
    print(f"{square_meters} 제곱미터는 {ft} 평방피트입니다. ")
    print(f"{square_meters} 제곱미터는 {ac} 에이커입니다. ")

