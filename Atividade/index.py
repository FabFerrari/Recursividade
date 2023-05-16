from fatorial import fatorial
from mdc import calcular_mdc
from multipl import multiplicacao_por_soma

print("=== multiplicacao ===")

for i in range(11):
    result = multiplicacao_por_soma(5, i)
    print(f"5 * {i} = {result}")

print("\n\n=== fatorial ===")

for i in range(11):
    result = fatorial(i)
    print(f"{i}! = {result}")

print("\n\n=== MCD ===")

for i in range(55, 102, 5):
    result = calcular_mdc(50, i)
    print(f"MDC de 50 e {i} = {result}")

