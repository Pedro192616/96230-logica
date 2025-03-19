import os 
os.system("clear")

login_cadastrado = "Pedro" 
senha_cadastrada = "1234"

for i in range(3) :
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ") 
        if login == login_cadastrado and senha == senha_cadastrada:
            print("Acesso permitido.")   
            break       
        else: 
            print("Login ou senha incorretos: \n")
        
            if i == 2 :

                print("Numero de tentativas excedido")
                break
        
