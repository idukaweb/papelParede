# - ----------------------------------------------------
# Programa para calcular a metragem de papel parede  - -
# Link    : https://github.com/idukaweb/papelParede  - -
# Author  : MWebRJ                  Version : 0.0.2  - -
# - ----------------------------------------------------

# - Importação de bibliotecas
from math import ceil
from tkinter import *


# - Funções Utilizadas

def calc_area(par):
    tam = len(par)
    
    alt = 0
    lar = 0

# - Sistema calcula a quantidade de papel para cada parede e a soma destas áreas
    for i in range(0,tam,2):
        alt += par[i]
        lar += par[i+1]
    
    print('\nTotal da área a ser coberta:')
    print(f'Altura: {alt:6.2f}m²\tLargura: {lar:6.2f}m²')
    resposta = f'Altura: {alt:6.2f}m²\tLargura: {lar:6.2f}m²'
# - Sistema calcula a área total a ser coberta
    area_total = alt * lar
    print(f'Área total: {area_total:5.2f}m²')
    resposta += f'\nÁrea total: {area_total:5.2f}m²'

# - ---------------------------------------------------- HEADER
# - Início da execução do programa
# - Vendedor informa os tipos de papéis disponíveis
lista_papeis = [[2.5, 0.5], [2.4, 0.75], [1.7, 0.5]]
# - Sistema mostra a altura e comprimento de cada tipo de papel usado
mensagem = f'\n- Sistema de cálculo de papel de parede -'
print(mensagem)
print(f'\nMetragem dos Papéis disponíveis')
for i in lista_papeis:
    print(f'Tipo (alt|comp):{i}')

# - Cliente escolhe o papel

# - Cliente informa a quantidade de paredes a serem cobertas

qtd_paredes = int(input("Informe a quantidade de paredes: "))
paredes = []
# - Cliente informa a metragem (altura x comprimento) de cada parede
# - Vendedor insere os dados de cada parede no sistema

i = 0
while i < qtd_paredes:
    print('Parede', i+1)
    altura = float(input('Altura: '))
    comprimento = float(input('Comprimento: '))

    # Lista com as metragens das paredes é atualizada
    paredes.append(altura)
    paredes.append(comprimento)
    i += 1


# - Sistema mostra a metragem de cada parede
print('Metragem cadastrada com sucesso \n>>',paredes)

# - Chamada da função de calcular a área a ser coberta



# - Sistema apresenta relatório com quantidade de papel usado e o valor a ser pago

''' Aqui podemos ter dois métodos: 
    Calcular a área total, colocar 10% a mais de margem, dividir pela largura do papel escolhido
    Ou Calcular a área total e e dividir pela área do papel (acho que não dá certo o cálculo)
'''

# Próximo passo, criar versão com GUI