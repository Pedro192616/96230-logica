import os
os.system("clear")

def metros_em_centimetros(metros):
    return metros * 100


metros = float(input("Digite o valor em metros: "))
centimetros = metros_em_centimetros(metros)

print(f"{metros} metros equivalem a {centimetros} centimetros.")