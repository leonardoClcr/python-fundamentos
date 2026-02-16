"""
CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde está o radar 1
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_maior_radar = velocidade > RADAR_1
multado_carro = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_maior_radar:
    print('Você esta acima do limite de velocidade.')

if  multado_carro and velocidade_maior_radar:
    print('Carro multado no radar.')