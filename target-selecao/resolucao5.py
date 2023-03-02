# Definindo a string
string = "target"

# Convertendo a string em uma lista de caracteres
lista_caracteres = list(string)

# Invertendo a lista de caracteres
for i in range(len(lista_caracteres) // 2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[-i - 1]
    lista_caracteres[-i - 1] = temp

# Convertendo a lista de caracteres de volta para uma string
string_invertida = "".join(lista_caracteres)

# Imprimindo a string invertida
print(string_invertida)