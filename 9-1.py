# 平均速度計算機 : かかった時間と移動距離に基づいて平均速度を計算するprogram

# input(total 5):出発時間/到着時間（時と分で別途入力）、移動距離
departure_time_hours = int(input("출발 시 (시간)을 입력하세요: "))
departure_time_minutes = int(input("출발 시(분)을 입력하세요: "))
arrival_time_hours = int(input("도착 시(시간)을 입력하세요: "))
arrival_time_minutes = int(input("도착 시(분)을 입력하세요: "))
moving_distance = int(input("이동 거리(km)를 입력하세요: "))

total_time = ((arrival_time_hours * 60 + arrival_time_minutes ) - (departure_time_hours * 60 + departure_time_minutes)) / 60

average_speed = moving_distance / total_time


# output:移動距離/出発時間/到着時間/平均速度(km/h)/速度状態（遅い or 普通 or 速い）

print(" ")
print(f"이동 거리: {moving_distance:.1f}")
print(f"출발 시간: {departure_time_hours}시", f"{departure_time_minutes}분")                    
print(f"도착 시간: {arrival_time_hours}시", f"{arrival_time_minutes}분")
print(f"평균 속도: {average_speed:.2F} km/h")

if average_speed < 60:
    print("속도 상태: 느림 ")
elif average_speed >= 60 and average_speed < 90 :
    print("속도 상태: 보통")
else:
    print("속도 상태: 빠름")



