# 2.	Задано чотирицифрове натуральне число. 
# a.	Знайти добуток цифр цього числа. 
# b.	Записати число в реверсному порядку. 
# c.	Посортувати цифри, що входять в дане число 

# print("2.a")
# number=int(input("Input a four-digit number: "))
# thousands=number // 1000
# hundreds=(number-thousands*1000) // 100
# dozens=(number-thousands*1000-hundreds*100) // 10
# units=number-thousands*1000-hundreds*100-dozens*10
# print("The product of the digits is ", thousands*hundreds*dozens*units)

# print("2.b")
# number=int(input("Input a four-digit number: "))
# thousands=number // 1000
# hundreds=(number-thousands*1000) // 100
# dozens=(number-thousands*1000-hundreds*100) // 10
# units=number-thousands*1000-hundreds*100-dozens*10
# print("Reverse order is ", units, dozens, hundreds, thousands)

print("2.c")
number=int(input("Input a four-digit number: "))
thousands=number // 1000
hundreds=(number-thousands*1000) // 100
dozens=(number-thousands*1000-hundreds*100) // 10
units=number-thousands*1000-hundreds*100-dozens*10
number_list=[thousands, hundreds, dozens, units]
order_list=[]
for i in range(4):
    x=min(number_list)
    order_list.append(x)
    number_list.remove(x)
print("Sorted order is ", order_list)
