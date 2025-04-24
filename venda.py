numero = float(input("Digite um valor: \n"))
if numero>50:
    numero -= 0.18*numero
print(f"Valor a ser cobrado: R${numero}")