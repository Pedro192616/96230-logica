import os
os.system("clear")


def calcular_media(lista):
    return sum(lista_notas) / QUANTIDADE_NOTAS

def verificar_resultado(media):
    if media >= 7:
        resultado = "Aprovado"
    if media >= 5:
        resultado = "Recuperaçao"
    if media <= 4:
        resultado = "Reprovado"
    return resultado
        
lista_notas = []
QUANTIDADE_NOTAS = 4
        
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)


media = calcular_media(lista_notas)
resultado = verificar_resultado(media)



print()
for nota in lista_notas:
    print(nota)


print(f"Media: {media}")
print(f"Resultado: {resultado}")
