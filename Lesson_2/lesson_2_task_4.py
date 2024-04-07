x_str=input("Ввведите число")
x= int(x_str)#Преобразование string в int

def fizz_buzz():#цикл
    for n in range (1,x):

        if(n%5==0) and (n%3==0):
            print("FizzBuzz")
        elif (n%3==0):
            print ("Fizz")  
        elif(n%5==0):
            print ("Buzz")
        else:
            print(n)
fizz_buzz()