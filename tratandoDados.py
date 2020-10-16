#Importando libraries necessárias 
import requests
import json
import re as regex

#Estabelecendo conexão com a nossa API
response = requests.get('http://127.0.0.1:5000/')
jason = response.json()


#Serializando json em dictionary
y = response.json()



#Inserindo dados de entrada

#mapa = input("Digite o mapa em que se deseja viajar: \n")

origem = input("Digite a origem da rota: \n")

destino = input("Digite o destino da rota: \n")

#autonomia = input("Digite a autonomia do caminhão: \n")

common = []
for rota, km in  y["MG"].items():
    
    if rota.startswith(origem):
        common.append(rota)
        
    if rota.endswith(destino):
        if not rota in common:
            common.append(rota)

rotasPossiveis=[]

for i in common:
    print(i)
    if i.startswith(origem) and i.endswith(destino):
        print(i)
        print(y["MG"][i])  
        rotasPossiveis.append(i)
    
        
    

    

