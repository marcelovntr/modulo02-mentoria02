"""
Exemplo básico de uso do pandas

Este código demonstra as operações mais básicas com pandas:
1. Criação de um DataFrame simples
2. Visualização dos dados
3. Operações básicas com colunas

Como usar:
1. Execute o programa
2. Observe os diferentes outputs no console
"""

import pandas as pd

def main():
    # Criando um DataFrame simples com notas de alunos
    dados = {
        'Aluno': ['João', 'Maria', 'Pedro', 'Ana'],
        'Nota': [8.5, 9.0, 7.5, 8.0]
    }
    
    # Criando o DataFrame
    df = pd.DataFrame(dados)
    
    print("\nDataFrame com notas dos alunos:")
    print(df)
    
    # Calculando a média das notas
    media = df['Nota'].mean()
    print(f"\nMédia das notas: {media:.2f}")
    
    # Mostrando a maior nota
    maior_nota = df['Nota'].max()
    print(f"Maior nota: {maior_nota}")
    
    # Mostrando a menor nota
    menor_nota = df['Nota'].min()
    print(f"Menor nota: {menor_nota}")

if __name__ == "__main__":
    main() 