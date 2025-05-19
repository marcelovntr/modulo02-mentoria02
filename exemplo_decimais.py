"""
Exemplo simples de operações com números decimais

Este código demonstra operações básicas com números decimais:
- Pede dois números decimais ao usuário
- Faz operações básicas (soma, subtração, multiplicação, divisão)
- Mostra os resultados
"""

def main():
    try:
        # Pedindo dois números decimais
        num1 = float(input("Digite o primeiro número decimal: "))
        num2 = float(input("Digite o segundo número decimal: "))
        
        # Operações básicas
        print(f"\nResultados:")
        print(f"Soma: {num1 + num2}")
        print(f"Subtração: {num1 - num2}")
        print(f"Multiplicação: {num1 * num2}")
        print(f"Divisão: {num1 / num2}")
    
    except ValueError:
        print("Erro: Digite números válidos!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main() 