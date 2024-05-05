
num = 0
sum = 0
cont = 0
x = 'SI'
while x == 'SI' :
    num = int(input('Digite un número entero -> '))
    sum += num
    cont += 1
    x = input('¿desea ingresar otro número? (SI/NO) -> ')
    x = x.upper()
    if x == 'SI' or x == 'NO' : 
        continue
    else : 
        print('Comando no reconocido, finalizando bucle')
media = sum / cont
print(f'Media aritmética -> {media}')


