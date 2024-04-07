#Банковское приложение
x_str=input("Ввведите размер вклада в рублях :")
x= int(x_str)#Преобразование string в int
y_str=input("Ввведите срок вклада в годах :")
y= list(y_str)#Преобразование string в обьект итерации
y1=int(y_str)
def bank():
    for n in y:
        summ=x+((10*x)/100)*y1
        #print(y)
        print ("Сумма вклада в конце года :",y1,"= ",summ,"рублей")
bank()

