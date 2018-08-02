'''
Esta classe irá gerar, a partir da quantidade de linhas e colunas uma matriz (linhas) X (colunas)
onde suas bordas são adicionadas o elemento '-1'. A partir de então, será gerado um dicionario
onde cada chave é um vertece do grafo e os valores contidos são os vertices adjacentes a ele
pela vizinhança esquerda, acima, direta, abaixo.
Nesta classe também serão inicializadas outras dependências como:
    Os vertices das bordas;
    Os vertices iniciais e finais;
@linnoramon & @hrnwendel
'''

from random import randint

class start_grafo(object):
    def __init__(self, linhas, colunas):
        # Todos os atributos estão sendo inicializados dentro do construtor.
        # proporções do labinto.
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = self.geraMatriz()             # matriz de auxilio para construção do Dicionario.
        self.grafo_raiz = self.geraDicionario()     # Dicionario de vertices e suas adjacencias.
        self.bordas = self.capturaBordas()          # Captura os vertices das bordas da matriz/labirinto.
        self.entrada = self.bordas[randint(0, len(self.bordas) - 1)]   # Atributo que guarda o vertice da entrada do labirinto
        # Método para sortear a entrada e saida do labirinto


    def geraMatriz(self):
        aux = []
        matriz = []
        cont = 0
        '''
        A matriz é gerada na proporção (linha +2) X (coluna +2) onde os dois indices adicionais são as bordas extra
        da matriz, onde será adicionado elementos negativos representativos.
        '''
        for lin in range(self.linhas + 2):
            for col in range(self.colunas + 2):
                # Caso esteja na linha 0 ou na ultima linha ou na coluna 0 ou na ultima coluna
                #  adicione o elemento representativo '-1'.
                if lin == 0 or col == 0 or  lin == self.linhas + 1 or col == self.colunas + 1:
                    aux.append('-1')
                else:
                    # Os vertices do grafo, serão representados numericamente de 1 ate (linha x coluna).
                    # Todos os vertices são representações numericas, no entanto são do tipo string.
                    aux.append(str(cont))
                    cont += 1
            matriz.append(aux)
            aux = []

        return matriz

    def geraDicionario(self):
        # Gera dicionario de adjacência a partir da matriz de vertices.
        indc = 0
        grafo = {}
        for lin in range(self.linhas + 2):
            for col in range(self.colunas + 2):
                if self.matriz[lin][col] == "-1":
                    continue
                else:
                    esqd = self.matriz[lin][col - 1]    # Captura elemento adjacente a esquerda do vertice atual.
                    cima = self.matriz[lin - 1][col]    # Captura elemento adjacente acima do vertice atual.
                    dirt = self.matriz[lin][col + 1]    # Captura elemento adjacente a direita do vertice atual.
                    baix = self.matriz[lin + 1][col]    # Captura elemento adjacente abaixo do vertice atual.
                    '''
                    O vertice atual recebe uma lista de adjacência com os vertices adjacentes a ele pela vizinhança
                    esquerda - acima - direita - abaixo, no sentido horario a partir da vizinhança esquerda.
                    '''
                    grafo[str(indc)] = [esqd, cima, dirt, baix, 0]
                    indc += 1  # Numero correspondente ao elemento a ser adicionado, no tipo INTEIRO.

        return grafo

    def capturaBordas(self):
        bordas = []
        for i in range(self.linhas + 2):
            # Se estiver na borda de cima ( 1 ) ou na penultima borda ( self.linhas ) adicione os elementos
            # em Bordas caso ele seja diferente de '-1'
            # OBS: Os indices ZERO e o ULTIMO da matriz são compostos de elementos negativos por este motivo
            # os indices a ser analisaddos são o indice ( 1 e o PENULTIMO )
            if (i == 1) or (i == self.linhas):

                for j in range(self.colunas + 2):
                    if self.matriz[i][j] != '-1':
                        bordas.append(self.matriz[i][j])
            # Caso não esteja na linha 1 ou penultima, será adicionado as bordas laterias esquerda <> direita
            # que segue o mesmo padrão das bordas superior <> inferior com elementos negativos nos indices ZERO e Ultimo
            else:
                    if self.matriz[i][1] != '-1' and self.matriz[i][self.colunas] != '-1':
                        bordas.append(self.matriz[i][1])
                        bordas.append(self.matriz[i][self.colunas])

        return bordas
