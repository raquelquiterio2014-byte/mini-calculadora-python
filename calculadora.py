"""Mini calculadora: quadrado, cubo e raiz quadrada."""
import math


def calcular(opcao, numero):
    if opcao == "1":
        return numero ** 2
    if opcao == "2":
        return numero ** 3
    if opcao == "3":
        if numero < 0:
            raise ValueError("Não existe raiz real para número negativo.")
        return math.sqrt(numero)
    raise ValueError("Opção inválida.")


def main():
    while True:
        print("\n1 - Quadrado | 2 - Cubo | 3 - Raiz quadrada | 0 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            print("Encerrando programa...")
            break
        if opcao not in {"1", "2", "3"}:
            print("Opção inválida.")
            continue
        try:
            numero = float(input("Digite um número: ").replace(",", "."))
            if not math.isfinite(numero):
                raise ValueError("Número não finito.")
            print(f"Resultado: {calcular(opcao, numero):.2f}")
        except ValueError as exc:
            print(f"Entrada inválida: {exc}")


if __name__ == "__main__":
    main()
