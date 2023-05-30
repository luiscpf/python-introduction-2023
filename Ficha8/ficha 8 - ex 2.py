def existe_algarismo(numero, algorismo):
    for indice in str(numero):
        if indice == str(algorismo):
            return True
    return False
print(existe_algarismo(1223245,2))