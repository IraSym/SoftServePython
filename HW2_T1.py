# 1.	Записати в стрічку філософію Пайтона 
# a.	Знайти в заданій стрічці кількість входжень слів (better, never, is) 
# b.	Вивести весь текст у верхньому регістрі (всі великі літери) 
# c.	Замінити всі входження символу “і” на “&” 
#1.a
print("1.a")
row="Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you're Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it's a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let's do more of those!"
number_better=0
number_never=0
number_is=0
row_split=row.replace('.', '').split()
for i in row_split:
    if i == 'better':
        number_better += 1
    elif i == "never":
        number_never += 1
    elif i == "is":
        number_is += 1
print("Number 'better' = {}".format(number_better))
print("Number 'never' = {}".format(number_never))
print("Number 'is' = {}".format(number_is))
#1.b
print("1.b")
row_up=row.upper()
print(row_up)
#1.c
print("1.c")
row_new=row.replace('i','&')
print(row_new)