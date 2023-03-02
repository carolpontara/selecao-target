# Definindo o número informado pelo usuário
num = int(input("Digite um número: "))

# Inicializando a sequência de Fibonacci
fib = [0, 1]

# Calculando a sequência de Fibonacci até o número informado pelo usuário
while fib[-1] < num:
    proximo = fib[-1] + fib[-2]
    fib.append(proximo)

# Verificando se o número informado pelo usuário pertence à sequência
if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci até {fib[-1]}.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci até {fib[-1]}.")