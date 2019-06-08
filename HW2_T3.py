# 3.	Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
value1=input("Input the first value: ")
value2=input("Input the second value: ")
value1, value2 = value2, value1
print("valu1= ", value1)
print("valu2= ", value2)
