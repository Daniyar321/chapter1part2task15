age = int(input())
a = -1
b = -2
if age % 2 != 0:
    while a != age:
        a = a + 2
        print(a)
if age % 2 == 0: 
    while b != age:
        b += 2
        print(b)   