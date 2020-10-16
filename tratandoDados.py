#Importando libraries necessárias 
import requests
import json
import re as regex

#Estabelecendo conexão com a nossa API
response = requests.get('http://127.0.0.1:5000/')
jason = response.json()


#Serializando json em dictionary
y = response.json()

#print(response)
#print(y["MG"]



#mapa = input("Digite o mapa em que se deseja viajar: \n")

origem = input("Digite a origem da rota: \n")
#A
destino = input("Digite o destino da rota: \n")
#D
#autonomia = input("Digite a autonomia do caminhão: \n")

#valordolitro = input("Digite o valor do litro: \n")

#A-B
#B-D


# y["MG"].keys())
x = y["MG"].keys()

origens = []
destinos = []

common = []

for rota, km in  y["MG"].items():
    
    if rota.startswith(origem):
        origens.append(rota)
        
        rota = rota.strip()
        common.append(rota)
        #print(rota +": " +str(km))
        #common.replaces(origem, "")
    
    if rota.endswith(destino):
        destinos.append(rota)
        
        rota = rota.strip()
        common.append(rota)
        #print(rota +": " +str(km))
    
counter = 0

for i in common:
    
    print(i+ " ")
    print(y["MG"][i])




'''
for i in origens:
    print(y["MG"][i])   
for i in destinos:
    print(y["MG"][i]) 
'''

# print(y[mapa].keys())

# extracted = regex.findall("A", y["SP"])

