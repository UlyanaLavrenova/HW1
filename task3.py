c = 0
for x in range (100000, 999999):
    a = sum(map(int, str(x)))
    b = sum(map(int, str(x+1)))
    if a % 7 == 0 and b % 7 == 0:
        c += 1
        if c > 0:
          print ("Lucky tickets: ",x, " and ", x+1, "(sum of ",x," = ",a,", sum of ",x+1," = ",b)
