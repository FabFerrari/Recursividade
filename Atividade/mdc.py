'''
Encontra o máximo divisor comum entre dois números

'''
'''
def calcular_mdc(numero1, numero2):
    if numero1 == 0:
        return numero2
    if numero2 == 0:
        return numero1

    while numero2 != 0:
        resto = numero1 % numero2

        numero1 = numero2
        numero2 = resto

    return numero1
'''
def calcular_mdc(numero1, numero2):
    if numero1 == 0:
        return numero2
    if numero2 == 0:
        return numero1

    resto = numero1 % numero2

    return calcular_mdc(numero2, resto)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(calcular_mdc(n1, n2))
