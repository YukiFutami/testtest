# ランダムを学ぶ

import random

my_list = ["pute","me-ya","nero","ave"]
random_element = random.choice(my_list)

user_input = input("member".format(random_element))

if random_element in my_list and user_input in my_list:
    if user_input == random_element:
        print("hikiwake")
    elif user_input != random_element:
        if user_input == "pute" and random_element == "me-ya":
            print("1,2desu")
        elif user_input == "me-ya" and random_element == "nero":
            print("2,3desu")
        elif user_input == "nero" and random_element == "ave":
            print("3,4desu")
    else:
        print("ore")
print("viva")  
 
