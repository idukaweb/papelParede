# -------------------------------------------------- -
# Programa para calcular a metragem de papel parede  -
# Link    : https://github.com/idukaweb/papelParede  -
# Author  : MWebRJ                  Version : 0.0.2  -
# -------------------------------------------------- -

# 0 - Importar bibliotecas
from math import ceil


# 0 - Funções

def calc_area(par):
    tam = len(par)
    
    alt = 0
    lar = 0
# 7 - Sistema calcula a quantidade de papel para cada parede
    for i in range(0,tam,2):
        alt += par[i]
        lar += par[i+1]
    print(f'Altura: {alt}m²\tLargura: {lar}m²')
    area_total = alt * lar
    print(f'Área total: {area_total:4.2f}m²')


# 1 - Cliente informa a quantidade de paredes a serem cobertas


qtd_paredes = int(input("Informe a quantidade de paredes: "))
paredes = []
i = 0
# 2 - Cliente informa a metragem (altura x comprimento) de cada parede

# 5 - Vendedor insere os dados de cada parede no sistema

while i < qtd_paredes:
    print('Parede', i+1)
    altura = float(input('Altura: '))
    comprimento = float(input('Comprimento: '))

    # Lista com as metragens utilizadas é atualizada
    paredes.append(altura)
    paredes.append(comprimento)
    i += 1

print('Paredes: ',paredes)

# 8 - Sistema apresenta relatório com quantidade de papel usado e o valor a ser pago
calc_area(paredes)


# 6 - Sistema identifica a altura e comprimento de cada tipo de papel usado

# 3 - Vendedor informa os tipos de papéis disponíveis
# 4 - Cliente escolhe o papel





