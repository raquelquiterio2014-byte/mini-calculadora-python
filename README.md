# mini-calculadora-python
"Mini calculadora em Python com menu interativo e validação de entrada"

# 🔢 Mini Calculadora em Python

Projeto simples desenvolvido em Python com menu interativo.

## 🚀 Funcionalidades
- Calcular quadrado
- Calcular cubo
- Calcular raiz quadrada
- Menu interativo
- Validação de entrada

## 🛠 Tecnologias
- Python 3

## ▶️ Como executar

```bash
python calculadora.py


def quadrado(n):
    return n ** 2

def cubo(n):
    return n ** 3

def raiz(n):
    if n < 0:
        print("Não existe raiz real para número negativo.")
        return None
    return n ** 0.5


def ler_numero():
    while True:
        try:
            return float(input("\nDigite um número: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")


def menu():
    while True:
        numero = ler_numero()

        print("\n=== MENU ===")
        print("1 - Quadrado")
        print("2 - Cubo")
        print("3 - Raiz quadrada")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print(f"Quadrado: {quadrado(numero):.2f}")
        elif opcao == "2":
            print(f"Cubo: {cubo(numero):.2f}")
        elif opcao == "3":
            resultado = raiz(numero)
            if resultado is not None:
                print(f"Raiz: {resultado:.2f}")
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
