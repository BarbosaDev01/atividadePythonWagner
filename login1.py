while True:
    nome = str(input("Digite o seu nome: "))
    senha = str(input("Digite sua senha: "))
    if nome == senha:
        print("Erro, nome e senhas iguais")
    else:
        print("Cadastro realizado com sucesso!")
        break
