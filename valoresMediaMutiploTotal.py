numero = 0
c,s,m= 0,0,0
while numero>=0:
    numero= int(input(f"Digite o {c+1}° número: "))
    if numero <0:
        break
    else:
        c+=1
        if numero%6 ==0:
            s+=1
        m+=numero
print("-=" * 20)
print(f"Total de números inteiros: {c}")
print(f"Total de números divisíveis por 6: {s}")
print(f"Média de números: {m/c:.2f}")
