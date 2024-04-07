x_str=input("Ввведите номер месяца от 1 до 12  :")
x= int(x_str)#Преобразование string в int

def month_to_season():#цикл
        
        if(x==12)or(x==1)or(x==2):
            print("Зима")
        elif (x==3)or(x==4)or(x==5):
            print ("Весна")  
        elif(x==6)or(x==7)or(x==8):
            print ("Лето")
        else:
            print("Осень")
month_to_season()