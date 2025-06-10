# Este programa pede um número ao usuário e exibe a tabuada desse número de 1 a 10.

# Solicita o número
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:\n")

# Gera a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
