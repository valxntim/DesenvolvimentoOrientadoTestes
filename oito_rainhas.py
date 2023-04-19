class Oito_rainhas:
   # teste 1
   def isNumber(self, a):
      tamanho_elem = len(a)
      count_zero = 0
      count_um = 0
      #count_nan = 0
      # se tem oito elementos
      if (tamanho_elem == 8):
         for i in range(tamanho_elem):
            # verifica se e int
            if (isinstance(a[i], int)):
               if (a[i] == 0):
                  count_zero += 1
               elif (a[i] == 1):
                  count_um += 1
               else:
                  return -1
            else:
               return -1
         # se nao tem sete '0' e um '1' nao e solucao
         if (count_um == 1 and count_zero == 7):
            count_zero = 0
            count_um = 0
            return 1
         else:
            return 0
      else:
         return -1
   # Teste 2

   def matriz_rainha(self, matriz):
      tamanho_elem = 0
      count_zero = 0
      count_um = 0
      retorno = 100
      z = 0
      # count_nan = 0
      # se tem oito elementos
      try:
         z = matriz[8][0]
         return -1
      except:
         try:
            for i in range(8):
               tamanho_elem = len(matriz[i])
               if (tamanho_elem == 8):
                  for j in range(8):
                     # verifica se e int
                     if (isinstance(matriz[i][j], int)):
                        if (matriz[i][j] == 0):
                           count_zero += 1
                        elif (matriz[i][j] == 1):
                           count_um += 1
                        else:
                           return -1
                     else:
                        return -1
                  # se nao tem sete '0' e um '1' nao e solucao
                  if (count_um == 1 and count_zero == 7):
                     retorno = 1
                  else:
                     return 0
                  count_zero = 0
                  count_um = 0
               else:
                  return -1
         except:
            return -1
      return retorno

   def verifica_coluna(self, matriz):
      tamanho_elem = 0
      count_zero = 0
      count_um = 0
      retorno = 100
      lista_pos = list()
      try:
         z = matriz[8][0]
         return -1
      except:
         try:
            for i in range(8):
               tamanho_elem = len(matriz[i])
               if (tamanho_elem == 8):
                  for j in range(8):
                     # verifica se e int
                     if (isinstance(matriz[i][j], int)):
                        if (matriz[i][j] == 0):
                           count_zero += 1
                        elif (matriz[i][j] == 1):
                           count_um += 1
                           if j in lista_pos:
                              return 0
                           else:
                              lista_pos.append(j)
                        else:
                           return -1
                     else:
                        return -1
                  # se nao tem sete '0' e um '1' nao e solucao
                  if (count_um == 1 and count_zero == 7):
                     retorno = 1
                  else:
                     return 0
                  count_zero = 0
                  count_um = 0
               else:
                  return -1
         except:
            return -1
      return retorno

   def verifica_oito_rainhas(self, matriz):
      tamanho_elem = 0
      count_zero = 0
      count_um = 0
      lista_pos = list()
      lista_diagonal_esq = list()
      lista_diagonal_dir = list()
      # testa se tem nove elementos
      try:
         z = matriz[8][0]
         return -1
      except:
         # se nao tem nove elementos ou seja matriz <=8
         try:
            # tenta rodar se der uma matriz menor que 8 vai dar erro por que matriz[i][j] nao vai existir
            for i in range(8):
               # pega o len pois tem que ser exatamente 8 se tratando de uma matriz 8x8
               tamanho_elem = len(matriz[i])
               if (tamanho_elem == 8):
                  for j in range(8):
                     # verifica se eh int
                     if (isinstance(matriz[i][j], int)):
                        if (matriz[i][j] == 0):
                           count_zero += 1
                        elif (matriz[i][j] == 1):
                           count_um += 1
                           # verificar coluna
                           if j in lista_pos:
                              # mesma coluna retorna 0
                              return 0
                           else:
                              lista_pos.append(j)
                           # vefiricar diagonal
                           if j in lista_diagonal_esq or j in lista_diagonal_dir:
                              return 0
                           else:
                              lista_diagonal_esq.append(j-1)
                              lista_diagonal_dir.append(j+1)
                              # nao pegar o  primeiro item
                              if (len(lista_diagonal_esq)-1 != 0):
                                 # len -1 pois nao queremos o ultimo item
                                 for t in range(len(lista_diagonal_esq)-1):
                                    lista_diagonal_esq[t] = lista_diagonal_esq[t]-1
                                    lista_diagonal_dir[t] = lista_diagonal_dir[t]+1
                        else:
                           # nao zero e nao um
                           return -1
                     else:
                        return -1
                  # se nao tem sete '0' e um '1' nao e solucao retorna 0
                  if ((count_um != 1 and count_zero != 7)):
                     return 0
                  count_zero = 0
                  count_um = 0
               else:
                  # se matriz diferente de 8x8
                  return -1
         except:
            # se tiver menos que oito listas retorna -1
            return -1
      # se chegou ate aqui matriz valida return 1
      return 1
