
# Cálculo de Tinta Necessária
# Abra o arquivo main.py. Dentro dele, localize a função resposta.

# A função deverá receber um valor numérico representando o tamanho da área a ser pintada (em metros quadrados) e retornar uma tupla contendo:

# A quantidade de latas de tinta a serem compradas
# O preço total da compra
# Regras:

# 1 litro de tinta cobre 3 m²
# Cada lata possui 18 litros
# Cada lata custa R$ 80,00
# Calcular a quantidade total de litros necessários
# Calcular a quantidade de latas necessárias (arredondando sempre para cima, pois só é possível comprar latas inteiras)
# Calcular o preço total com base na quantidade de latas
# Exemplos:

# resposta(54) → (1, 80)
# resposta(60) → (2, 160)
# Atenção: utilize return, não print.


import math


def resposta(area):

    litros_necessarios = area / 3

    latas_necessarias = math.ceil(litros_necessarios / 18)

    preco_total = latas_necessarias * 80

    return (latas_necessarias, preco_total)


print(resposta(10))
print(resposta(60))
