from oito_rainhas import Oito_rainhas


def test_VerificaSeTemOitoElemEseEint():
    # TESTE 1
   elem = Oito_rainhas()
   a_impossivel = [0, 0, 0, 0, 0, 0, 't', 1]
   assert elem.isNumber(a_impossivel) == -1
   a_valido = [0, 0, 0, 0, 0, 1, 0, 0]
   assert elem.isNumber(a_valido) == 1
   a_invalido = [0, 0, 0, 0, 0, 0, 1, 1]
   assert elem.isNumber(a_invalido) == 0


def test_RecebeOitoxOito():
    # TESTE 2
   elem = Oito_rainhas()
   matriz_valida = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [
       0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1]]
   assert elem.matriz_rainha(matriz_valida) == 1
   matriz_impossivel = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [
       0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1]]
   assert elem.matriz_rainha(matriz_impossivel) == -1


def test_VerificaColuna():
    # TESTE 3
   elem = Oito_rainhas()
   matriz_valida = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [
       0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0]]
   assert elem.verifica_coluna(matriz_valida) == 1
   matriz_invalida = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [
       0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0]]
   assert elem.verifica_coluna(matriz_invalida) == 0


def test_VerificaOitoRainhas():
    # TESTE 4
   elem = Oito_rainhas()
   matriz = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [
       0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]]
   assert elem.verifica_oito_rainhas(matriz) == 1
   matriz_invalida = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [
       0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
   assert elem.verifica_oito_rainhas(matriz_invalida) == 0
