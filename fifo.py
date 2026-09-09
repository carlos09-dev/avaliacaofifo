from collections import deque

# Criando uma fila vazia
fila = deque()

# Pessoas entrando na fila
fila.append("João")
fila.append("Maria")
fila.append("Carlos")

# Mostrando a fila
print("Fila:", fila)

# Atendendo a primeira pessoa
cliente = fila.popleft()

print("Cliente atendido:", cliente)

# Mostrando quem ficou na fila
print("Fila agora:", fila)

