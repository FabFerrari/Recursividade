'''
Esta função realiza a multiplicação de um número através da soma contínua do número com ele mesmo
Numero: o numero base
Vezes: o tanto de vezes que o número será multiplicado
'''

def multiplicacao_por_soma(numero, vezes):
    if vezes == 0:
        return 0
    elif vezes == 1:
        return numero
    else:
        return numero + multiplicacao_por_soma(numero, vezes - 1)

n1 = int(input('Digite Nr1: '))
n2 = int(input('Digite Nr2: '))

print(multiplicacao_por_soma(n1, n2))
