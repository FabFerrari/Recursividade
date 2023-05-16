'''
Esta função realiza o fatorial de um número passado
Numero: o número que será calculado o fatorial
'''

#def fatorial(numero):
#    if numero <= 1:
#        return 1
#    for i in numero:
#        numero*i
# 
#
#n1 = int(input('Digite o numero: '))
#
#print(fatorial(n1))
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

n1 = int(input('Digite o número: '))
print(fatorial(n1))
