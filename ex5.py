# Inicializa um vetor com 5 números inteiros
numeros = []

# Lê os 5 números do usuário
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Exibe os números
print("Números digitados:", numeros)

# Calcula a soma dos números
soma = 0
for numero in numeros:
  soma += numero
print("Soma dos números:", soma)

# Calcula a multiplicação dos números
multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero
print("Multiplicação dos números:", multiplicacao)