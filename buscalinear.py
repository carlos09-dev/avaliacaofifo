# Lista de clientes
clientes = ["João", "Maria", "Carlos", "Ana"]

# Nome que queremos encontrar
procurado = "Carlos"

# Procurando na lista
for cliente in clientes:

    # Verifica se encontrou
    if cliente == procurado:
        print("Cliente encontrado:", cliente)
        break
