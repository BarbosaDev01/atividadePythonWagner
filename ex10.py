n = int(input("Digite um número: "))
print(f"Serão solicitados {n} valores")
print("-="*20)
for i in range(0,n):
    numero = int(input("Escolha um número: "))
    print(f"{numero} * 3 = {numero*3}")
    print("-" * 20)