import os
os.system("clear")

while True:
    
    nota = float(input("Digite a nota do aluno: "))

    if nota < 0 or nota > 10:
        print("repetindo....")
    else :
        break
    
print(f"a nota do aluno e {nota}")
print("FIM")
