mundo = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]

linha = 0
coluna = 0

mundo[linha][coluna] = "#"

def movimento(loc):
    global linha

    try:
        if loc == "s":
            mundo[linha][coluna] = "*"   # apaga posição antiga
            linha += 1
            mundo[linha][coluna] = "#"   # desenha na nova posição

    except Exception as error:
        print(f"Houve um erro: {error}")

    print(mundo)

presskey = input()
movimento(presskey)