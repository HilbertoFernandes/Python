def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def menu():
    print("===== CALCULADORA EM PYTHON =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando a calculadora.")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    

    if opcao == "1":
        print(f"Resultado: {somar(num1, num2)}")
    elif opcao == "2":
        print(f"Resultado: {subtrair(num1, num2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcao == "4":
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opção inválida. Tente novamente.")

    print()  # linha em branco para separação
