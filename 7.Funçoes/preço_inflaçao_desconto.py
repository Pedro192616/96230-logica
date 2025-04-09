import os
os.system("clear")


def inflacionar(preco):
     
    if preco < 100:
        resultado = preco * 1.10

    else:
        resultado = preco * 1.20
    return resultado

preco_produto = float(input("Digite o preço do produto: "))
preco_inflacao = inflacionar(preco_produto)
print(f"Preço final: {preco_inflacao}")

def descontar (preco):
    if preco < 100:
        resultado = preco * 0.10
        
    else:
        resultado = preco * 0.20
    return resultado
     
preco_produto = float(input("Digite o preço do produto: "))
preco_descontado = descontar(preco_produto)
print(f"Preço final: {preco_descontado}")




    

    



    