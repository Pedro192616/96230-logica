# Limpar o terminal
import os
os.system("clear")

# Entrada
peso = float(input("Digite o peso desejado em kilos: "))
valor_por_kg = input 
valor_total = 0 
desconto = valor_total * 0.10
fruta = input("""Digite a fruta desejada"
1- Morango "
2- Maça 
""")

# Processamento

match fruta :
    case "1":
      if peso <= 5 :
        valor_por_kg = 2.50
      elif peso > 5 :
        valor_por_kg = 2.20
      else :
        print("Fruta invalida.")


    case "2":
            fruta = "Maça"
            if peso <= 5:
                valor_por_kg = 1.80
            elif peso > 5 :  
                valor_por_kg = 1.50
            else :
                print("Fruta invalida.")

# Saida

if peso > 10 or valor_total > 15 :
    print(f"Desconto: R${desconto:.2f}")
else :
    print ("Sem desconto.")

valor_total = peso * valor_por_kg
if peso > 10 or valor_total > 15:
    desconto = valor_total * 0.10
    valor_total = valor_total - desconto

print(f"Fruta: {fruta}")
print(f"Peso: {peso}kg")
print(f"Valor total: R${valor_total:.2f}")
