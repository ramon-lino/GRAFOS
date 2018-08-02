'''
Classe de plotagem do labiritino e do caminho percorrido

'''
class plotagem(object):

    def __init__(self, altura, largura, labirinto):
        self.__altura = altura
        self.__largura = largura
        self.__labirinto = labirinto

    def imprime_labirinto(self, entrada, saida):
        matriz_imprime = [["0" for i in range(self.__largura)] for i in range(self.__altura)]

        for i in range(len(matriz_imprime)):
            for j in range(len(matriz_imprime[i])):
                if i % 2 != 0:
                    matriz_imprime[i][j] = " "
                if j % 2 != 0 and (i % 2 == 0 or i % 2 != 0):
                    matriz_imprime[i][j] = "     "

        for i in range(len(self.__labirinto)):

            c_correto = self.__labirinto[i]

            cont = 0
            for i in range(len(matriz_imprime)):
                for j in range(len(matriz_imprime[i])):
                    if matriz_imprime[i][j] == "0" or matriz_imprime[i][j] == "E" or matriz_imprime[i][j] == "S":

                        if (str(cont) in c_correto) == True and str(cont) != c_correto[-1]:

                            if int(c_correto[c_correto.index(str(cont)) + 1]) + 1 == cont:
                                matriz_imprime[i][j - 1] = " --- "

                            if int(c_correto[c_correto.index(str(cont)) + 1]) - 1 == cont:
                                matriz_imprime[i][j + 1] = " --- "

                            if int(c_correto[c_correto.index(str(cont)) + 1]) - 1 > cont:
                                matriz_imprime[i + 1][j] = "|"

                            if int(c_correto[c_correto.index(str(cont)) + 1]) + 1 < cont:
                                matriz_imprime[i - 1][j] = "|"

                        if str(cont) == saida:
                            matriz_imprime[i][j] = "S"

                        if str(cont) == entrada:
                            matriz_imprime[i][j] = "E"
                        cont += 1

        for i in matriz_imprime:
            for j in i:
                print(j, end="")
            print('\t')

        return matriz_imprime

    def imprime_caminhoPercorrido(self, caminho_percorrido = [], caminho_feito = []):

        print('\n Caminho gerado: ', end='')
        for i in range(len(caminho_feito)):
            if i < len(caminho_feito) -1:
                print(caminho_feito[i], end='-')
            else:
                print(caminho_feito[i])

        print("\n Caminho percorrido: ", end='')
        for i in range(len(caminho_percorrido)):
            if i < len(caminho_percorrido) -1:
                print(caminho_percorrido[i], end='-')
            else:
                print(caminho_percorrido[i])