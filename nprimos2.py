n = 0
esprimo = True
for i in range(2, n) : 
    if n % i == 0 :
        esprimo = False
        break
if esprimo : 
    print(f'El número {n} es primo')
else : 
    print(f'El número {n} NO es primo')