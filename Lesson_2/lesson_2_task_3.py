x_str=input("Ввведите сторону квадрата")
x= float(x_str)#Преобразование string во float
import math
x=math.ceil(x)#округляем в большую сторону
def square():
    c=x*x
    print(c)
square()

