a1 = int(input("Digite um número: "))
a2 =int(input("Digite o segundo número: "))
r= a2-a1
n = 0
for c in range(0,20):
 n += 1
 an = a1+(n-1)*r
 print(f"{n}º termo: {an}")