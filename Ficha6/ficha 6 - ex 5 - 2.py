def substitui(lista_recebida, velho, novo):
   lista_saida = []
   
   for elemento in lista_recebida:
      if elemento == velho:
         lista_saida += [novo]
      else:
         lista_saida += [elemento]
   return lista_saida
   
print(substitui ([1, 2, 3, 2, 4], 2, 'a'))