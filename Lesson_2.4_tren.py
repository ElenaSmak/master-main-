#Задача: вывести только нечетные числа.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #последовательность чисел
for n in nums: # цикл перебора последовательности
    if (n % 2 == 1): # проверка условия на четность
         print(n) # вывод результата