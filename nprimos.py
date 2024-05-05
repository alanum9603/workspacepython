n = int(input('Digite un número entero -> '))
c = ''
s = 0
for i in range (n) : 
    if (n % (i + 1)) == 0 :
        c += str(i + 1) 
        s += 1
        if (i + 1) != n : 
            c += ', '
print(c)
if s == 2 : 
    print('Es primo')
else : 
    print('No es primo')
    