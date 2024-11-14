# Função para verificar se um número é primo
def e_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita o valor de N
N = int(input("Digite um número inteiro N: "))

# Exibe os números primos entre 1 e N
print(f"Os números primos entre 1 e {N} são:")
for i in range(2, N + 1):
    if e_primo(i):
        print(i)
