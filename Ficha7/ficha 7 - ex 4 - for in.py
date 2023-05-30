#Suponha que bib é uma lista cujos elementos são dicionários e que contém a informação sobre os livros existentes numa biblioteca. Cada livro é caracterizado pelos seus autores, título, casa editora, cidade de publicação, ano de publicação, número de páginas e ISBN. Escreva um programa em Python que recebe a informação de uma biblioteca e devolve o título do livro mais antigo.

def bib (biblioteca):
    
    livro_antigo = biblioteca[0]
    
    for indice in biblioteca:
        if livro_antigo["ano"] > indice["ano"]:
            livro_antigo = indice
    return livro_antigo["titulo"]

lista = [{"autor":"Luis de Camões", "titulo":"Lá se foi", "editora":"lecy", "publicação":"Funchal", "ano":2002, "paginas":200, "ISBN":111}, 
         {"autor":"Joao Kleber", "titulo":"Lá se vinha", "editora":"octupus", "publicação":"Funchal", "ano":2006, "paginas":696, "ISBN":222}, 
         {"autor":"Mia Khalifa", "titulo":"Já te vinhas", "editora":"invy", "publicação":"Funchal", "ano":2000, "paginas":105, "ISBN":333}]

print(bib(lista))