def calcarea(b : float, h : float) :
    calc = b * h 
    return calc

def main() :
    base = float(input('Digite la medida de la base: '))
    altura = float(input('Digite la medida de la altura: '))
    area = calcarea(base, altura)
    print(f'Área del rectangulo: {area}')

main()