# Este programa solicita ao usuário o menor e o maior número de um intervalo.
# Depois, pergunta quantos números aleatórios (sem repetição) devem ser sorteados dentro desse intervalo.
# Por fim, exibe os números sorteados. O programa garante que os números sorteados sejam únicos.

import random

# Solicita o menor e o maior número do intervalo
menor = int(input("Digite o menor número do intervalo: "))
maior = int(input("Digite o maior número do intervalo: "))

# Garante que o menor seja realmente menor que o maior
if menor > maior:
    menor, maior = maior, menor  # Inverte se estiver errado

# Calcula a quantidade máxima de números únicos possíveis
total_possiveis = maior - menor + 1

# Solicita a quantidade de números a serem sorteados
quantidade = int(input(f"Quantos números únicos você deseja sortear entre {menor} e {maior}? "))

# Verifica se é possível sortear essa quantidade de números únicos
if quantidade > total_possiveis:
    print(f"Não é possível sortear {quantidade} números únicos entre {menor} e {maior}.")
    print(f"O máximo possível é {total_possiveis}.")
else:
    # Sorteia os números únicos
    numeros_sorteados = random.sample(range(menor, maior + 1), quantidade)

    # Exibe os números sorteados
    print("\nNúmeros sorteados (sem repetição):")
    print(numeros_sorteados)
