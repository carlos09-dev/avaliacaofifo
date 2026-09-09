# Lista ordenada
lista = [1, 2, 3, 4, 5, 6, 7]

# Número que vamos procurar
numero = 5

# Início e fim da busca
inicio = 0
fim = len(lista) - 1

# Enquanto houver números para procurar
while inicio <= fim:

    # Encontra o meio
    meio = (inicio + fim) // 2

    # Verifica se encontrou
    if lista[meio] == numero:
        print("Número encontrado:", lista[meio])
        break

    # Procura na direita
    elif lista[meio] < numero:
        inicio = meio + 1

    # Procura na esquerda
    else:
        fim = meio - 1

