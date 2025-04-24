a1 = int(input("Digite um número: "))
a2 =int(input("Digite o segundo número: "))
r= a2/a1
for n in range(0,6):
    an = a1*(r**(n-1))
    if an>0:
        print("{}º termo: {}".format(n,an))
    else:
        print(f" Valor negativo \n Razão dos termos: {r}")
        break