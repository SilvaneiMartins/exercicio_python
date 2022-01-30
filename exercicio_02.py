equipamentos=[]
valores=[]
seriais=[]
departamento=[]
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()

for equipamento in equipamentos:
    print("Equipamentos: ", equipamento)