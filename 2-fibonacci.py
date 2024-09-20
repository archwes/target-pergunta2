def pertence_fibonacci(n):
    if n < 0:
        return False

    def is_perfeito(x):
        return (x ** 0.5).is_integer()

    return is_perfeito(5 * n * n + 4) or is_perfeito(5 * n * n - 4)

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
