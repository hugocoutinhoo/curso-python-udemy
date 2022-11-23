"""
CONSTANTE = "variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1 
condicao_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
condicao_2 = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 =  condicao_1 and condicao_2
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1 

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')