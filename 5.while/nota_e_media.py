import os
os.system("clear")

QUANTIDADE_NOTAS = 2
soma = 0
for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite a nota do aluno: "))

        if nota < 0 or nota > 10:
            print("A nota deve ser entr 0 e 10.\n")
        else :
            soma += nota
            break
media = soma / QUANTIDADE_NOTAS

print(f"Media: {media}")
print("FIM")
