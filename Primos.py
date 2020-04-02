primos = []
for num in range(1,101):
    count = 0
    for numb in range(1,num+1):
        if num % numb == 0:
            count += 1
    if count ==2:
        primos.append (num)
print (primos)