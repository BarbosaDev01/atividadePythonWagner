numeroDaConta = 0
while numeroDaConta!=-999:
    print("-="*20)
    numeroDaConta= int(input("Número da conta: \n"))
    if numeroDaConta == -999:
        break
    saldo = int(input("Saldo da conta: \nR$"))
    if saldo>=0:
        print(f"R${saldo} - Saldo positivos")
    else:
        print(f"R${saldo} - Saldo positivos")


