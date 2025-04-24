while True:
    nome = input("Nome do professor: ")
    horaAula = float(input("Hora aula do professor: R$ "))
    aulasDada = int(input("Quantidade de aulas do professor: "))
    salario = (horaAula*(aulasDada*4.5))
    print("-="*25)
    if salario<1000:
        print(f"Professor {nome} está isento do sindicato \nSalario: {salario}")
        break
    else:
        print(f"Professor {nome} não está isento do sindicato \nSalario: {salario}")
    print("-="*25)