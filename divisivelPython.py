print("Digite [s] para sair")
numero = input("Digite um número:\n")
while numero!= "s":
    if int(numero)%2 == 0 and int(numero)%10==0 and int(numero)%5==0:
        print("Número {} é divisivel por 2,5 e 10".format(numero))
    else:
        print("Número {} NÃO é divisivel por 2,5 e 10".format(numero))
    numero = input("Digite um número:\n")