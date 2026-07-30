import numpy as np
mundo = np.array([
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
])
linha = 0
coluna = 0
mundo[linha][coluna] = "#"
print (mundo)
def movimento(loc):
    global linha
    global coluna
    global mundo
    
    jogando = True
    while jogando:
        try:
            if loc == "s":
                linha += 1
                mundo[linha][coluna] = "#"   # desenha na nova posição
                print(mundo)
            
    
        except Exception as error:
            print(f"Houve um erro: {error}")
    print(mundo)
presskey = input()
movimento(presskey)


Por que está dando erro
