inventario=[]
resposta="S"

while resposta == "S":
    inventario.append(input("Nome do Equipamento: "))
    inventario.append(float(input("Valor do equipamento: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta=input("Digite S para continuar: ").upper()

for elemento in inventario:
    print(elemento)