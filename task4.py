#var 1
import random

n = int(input("Enter the length of the list: "))
A = []
for i in range(n):
    b = int(random.random()*100)
    A.append(b)
print("A is", A)
a = int(input("Which element do you want to delete? "))
A.pop(a - 1)
print(A)
