

def conta_palavras (texto):
    resultado = {}
    indice_atual = 0
    
    while indice_atual < len(texto):
        
        # encontra a palavra
        
        inicio_palavra = indice_atual
        while texto[indice_atual] != " " and indice_atual < len(texto):
            indice_atual += 1
        palavra = texto[inicio_palavra:indice_atual]
        
        #adiciona a palavra ao dicionario
        
        if palavra not in resultado:
            resultado[palavra] = 1
        else:
            resultado[palavra] = +1
            
        #inicia a proxima palavra
        
        indice_atual += 1
        
        #ignora multiplos espaços
        
        while indice_atual < len(texto) and texto[indice_atual] == " ":
            indice_atual += 1
    
    return resultado

def imprime_dicionario (dicionario):
    for chave in dicionarios:
        print(chave, ":", dicionario[chave]
    print ("O tal

print(conta_palavras("Ola tudo    bem ola"))