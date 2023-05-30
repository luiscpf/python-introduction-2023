def nova_pilha ():
    return []

def e_pilhas (x):
    return isinstance(x, list)
    
def pilha_vazia (pilha):
    return pilha == [] #ou len(pilha) == 0

def inserir (pilha, elemento):
    if (e_pilha(pilha)):
        return [elpemento] + pilha
    else:
        raise TypeError("Não é uma pilha")
    
def topo (pilha):
    if not e_pilha(pilha):
        raise TypeError("Não é uma pilha")
    if pilha_vazia(pilha):
        raise ValueError("A pilha está vazia")
    return pilha[0]

def tira(pilha):
    return pilha[1:]

def pilhas_iguais (pilha_1, pilha_2):
    return pilha_1 == pilha_2