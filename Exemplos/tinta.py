import math

def calcular_tinta():
    litro_galao = 3.6

    # Recebe as dimensões da parede em centímetros
    largura_cm = float(input("Digite a largura da parede em centímetros: "))
    altura_cm = float(input("Digite a altura da parede em centímetros: "))

    # Converte centímetros para metros
    largura = largura_cm / 100
    altura = altura_cm / 100

    # Calcula a área em metros quadrados
    area = largura * altura

    # 1 litro de tinta pinta 1 m²
    litros_necessarios = area / 1

    # Galões arredondados para cima
    galoes_necessarios = math.ceil(litros_necessarios / litro_galao)

    print(f"\nVocê precisará de aproximadamente {litros_necessarios:.2f} litros de tinta.")
    print(f"Você deverá comprar {galoes_necessarios} galão(ões) de tinta de 3,6 litros.")

if __name__ == "__main__":
    calcular_tinta()
