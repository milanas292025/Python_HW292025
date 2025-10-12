import math

def square (num):
    return math.ceil(num * num)

sq_num = int(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(sq_num)}")


