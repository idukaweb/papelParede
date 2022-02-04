# - ----------------------------------------------------
# Programa para calcular a metragem de papel parede  - -
# Link    : https://github.com/idukaweb/papelParede  - -
# Author  : MWebRJ                  Version : 0.0.2  - -
# - ----------------------------------------------------

# - Importação de bibliotecas
from math import ceil


# - Funções Utilizadas

def calc_area(par):
    tam = len(par)
    
    alt = 0
    lar = 0

# - Sistema calcula a quantidade de papel para cada parede e a soma destas áreas
    for i in range(0,tam,2):
        alt += par[i]
        lar += par[i+1]
    print(f'Altura: {alt}m²\tLargura: {lar}m²')

# - Sistema calcula a área total a ser coberta
    area_total = alt * lar
    print(f'Área total: {area_total:4.2f}m²')

# - ----------------------------------------------------
# - Início da execução do programa
# - Vendedor informa os tipos de papéis disponíveis
lista_papeis = [[2.5, 0.5], [2.4, 0.75], [1.7, 0.5]]

print(f'\n\nMetragem dos Papéis disponíveis')
for i in lista_papeis:
    print(f'Tipo (alt|larg):{i}')



# 1 - Cliente informa a quantidade de paredes a serem cobertas

qtd_paredes = int(input("Informe a quantidade de paredes: "))

paredes = []
# 2 - Cliente informa a metragem (altura x comprimento) de cada parede
# 5 - Vendedor insere os dados de cada parede no sistema
i = 0
while i < qtd_paredes:
    print('Parede', i+1)
    altura = float(input('Altura: '))
    comprimento = float(input('Comprimento: '))

    # Lista com as metragens das paredes é atualizada
    paredes.append(altura)
    paredes.append(comprimento)
    i += 1

print('Paredes: ',paredes)
calc_area(paredes)


# 8 - Sistema apresenta relatório com quantidade de papel usado e o valor a ser pago
# 6 - Sistema identifica a altura e comprimento de cada tipo de papel usado

# 4 - Cliente escolhe o papel





