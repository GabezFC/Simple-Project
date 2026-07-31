import numpy as np

mundo = np.array([
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
])

#Variáveis de definição
linha, coluna = 0, 0

#Personagem
mundo[linha][coluna] = "#"
print (mundo)

def movimento():
    global linha, coluna
    
    while True:
        
        presskey = input("Use 'w/a/s/d' e 'q' para sair: ")
        
        if presskey == "q":
            break
        
        if not 0 < linha > mundo.shape[0] and 0 < coluna > mundo.shape[1]:
            print("Não pode sair do mapa!")
            continue
        
        if presskey == "w":
            mundo[linha][coluna] = "*" 
            linha -= 1
            mundo[linha][coluna] = "#"   # desenha na nova posição
            print(mundo)
            continue
        elif presskey == "s":
            mundo[linha][coluna] = "*" 
            linha += 1
            mundo[linha][coluna] = "#"   # desenha na nova posição
            print(mundo)
            continue
        elif presskey == "d":
            mundo[linha][coluna] = "*" 
            coluna += 1
            mundo[linha][coluna] = "#"   # desenha na nova posição
            print(mundo)
            continue
        elif presskey == "a":
            mundo[linha][coluna] = "*" 
            coluna -= 1
            mundo[linha][coluna] = "#"   # desenha na nova posição
            print(mundo)
            continue
        else:
            print("Digite um número válido")
            continue
        


movimento()

