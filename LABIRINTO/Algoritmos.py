'''
Classe que contém todos os algoritmos de interação sobre os grafos que formam o labirinto
Algoritmos como gerar o caminho de resolução do labirinto, caminhos de distração do labirinto
Algoritmo de construir as arestas do grafo final do labirinto com todas as suas adjacências.
@linnoramon & @hrnwendel
'''
import random
class algoritmos_(object):
    def __init__(self, dic = {}, ini = str, bordas = []):
        self.G = dic    # Grafo Primitivo
        self.ini = ini
        self.range = self.__range() # Intervalo aceito para tamanho do caminho resolutorio

        self.__tamanhoCaminho = {}  # Guarda o tamanho do caminho do vertice inicial até o vertice no qual se encontra
        self.__rotuloVertice  = {}  # Guarda o rotulo do vertice, caso seja 1 ele é permanente e ja foi verificado, caso 0 é temporario
        self.__vertAnterior   = {}  # Armazena o vertice anterior de cada vertice
        self.__pesoArestas    = {}  # Armazena o peso de todas as arestas! que vale 1

        self.caminho_resolutorio = self.algoritmos_caminhoEntradaSaida(ini, bordas, dic, self.range)
        self.entrada = self.caminho_resolutorio[0]  # Vertice de Entrada do labirinto
        self.saida  = self.caminho_resolutorio[-1]  # Vertice de Saida do labirinto
        self.todos_caminhos = self.algoritmos_caminhosErrados([self.caminho_resolutorio], dic)

    def __range(self):
        total = len(self.G) # Total de vertices do grafo
        r = []  # Lista auxiliar para retornar o range
        '''
        Laço que vai da metade dos vertices do grafo ( -10% ) até metade dos vertices ( +10% )
        para que o caminho resolutorio tenha tamanho dentro do range com 10% pra mais ou pra menos
        '''
        for i in range( (int(total / 2) - int(total*0.1)), int(total / 2) + int(total*0.1)):
            r.append(i)
        return r

    def algoritmos_caminhoEntradaSaida(self, ini, bordas = [], grafo = {}, range = []):
        # Método para criar um caminho resolutorio do labirinto
        caminho = [ini] # Caminho começa no vertice de entrada, ja estabelecido na classe: GrafoRaiz
        atual = ini     # Variavel temporaria que armazena o vertice a ser analizado
        grafo[ini][4] = 1   # Tornando o vertice atual como "ja verificado"

        while True:
            possibilidades = grafo[atual]   # Lista de possiveis Vertices no qual o vertice atual pode ir
            ir_para = atual                 # Variavel que armazena para onde ele irá/ OBS: inicializada no vertice atual

            '''
            Condição de parada! Caso o ultimo vertice no qual ele verificou esteja na borda AND o tamanho do caminho esteja
            dentro do RANGE ou o tamanho do caminho seja maior que o tamanho maximo permitido pelo RANGE... BREAK o laço
            '''
            if (caminho[-1] in bordas) and ((len(caminho) in range) == True or len(caminho) > range[-1]):
                break

            cont = 0
            # Enquanto o vertice sorteado para IR seja igual a '-1 ou O vertice sorteado para IR ja tenha sido verificado..
            # Continue procurando um vertice para ir
            while ir_para == '-1' or grafo[ir_para][4] == 1:
                # Caso o laço tenha rodado 8x significa que ele esta procurando um proximo vertice mas nn esta encontrando
                # pois todos os vertices possiveis ja foram verificados.
                if cont == 8:

                    caminho.pop()           # Remove o ultimo elemento do caminho, fazendo com que vá retornar ate um lugar que possa continuar
                    atual = caminho[-1]     # atual também vai regredindo ate um vertice com possibilidade de IDA
                    possibilidades = grafo[atual]   # As possibilidades também vão mudando conforme atual é atualizado

                    cont = 0

                cont += 1
                # Sorteando um novo vertice para ir
                ir_para = possibilidades[random.randint(0, 3)]

            caminho.append(ir_para) # Adiciona ao caminho o vertice no qual ele vai
            grafo[ir_para][4] = 1   # O vertice que ele vai, se tornará ATUAL, então ele recebe como "Ja verificado"
            atual = ir_para         # Atual se torna o vertice que foi escolhido para ir

        return caminho

    def __naoUtilizados(self, grafo, todos_cam):
        # Método para separar todos os vertices que não fazem parte do caminho resolutorio
        nao_utl = []
        for i in grafo:
            # Caso o vertice em questão não esteja no caminho ZERO, que representa o caminho de resolução do labirinto
            # e não seja uma representação negativa, adicione a lista de vertices ainda não utilizados
            if i not in todos_cam[0] and i != '-1':
                nao_utl.append(i)

        return nao_utl

    def algoritmos_caminhosErrados(self, todos_caminhos = [], grafo = {}):
        '''
        Método para gerar todos os caminhos aleatorios do labirinto, que não dão em resultado nenhum..
        consiste em escolher um vertice aleatorio e a partir dele ir percorrendo ate se conectar a um caminho ja feito
        :param todos_caminhos: inicialmente começa apenas com o caminho resolutorio do grafo no indice [0]
        :param grafo: Grafo primitivo com todos os vertices e as adjacencias verticais e orizontais
        :return: Lista de listas de caminhos
        '''

        # Tomando a precação de ZERAR (constar como não verificado)
        # todos os vertices que não fazem parte do caminho resolutorio
        for i in grafo:
            if i not in todos_caminhos[0]:
                grafo[i][4] = 0

        # Lista de vertices que ainda não fazem parte de algum caminho do labirinto
        nao_utilz = self.__naoUtilizados(grafo, todos_caminhos)
        atual = nao_utilz[random.randint(0, len(nao_utilz) - 1)]    # Escolhe aleatoriamente um dos vertices que não fazem parte de um caminho
        caminho_atual = [atual]     # Lista que armazena o caminho que esta sendo gerando. Começa pelo vertice que foi escolhido aleatoriamente
        grafo[atual][4] = 2         # A principio, os vertices que não fazem parte do caminho resolutorio do labirinto, serão constado como 2
        # caso ele ja tenha sido verificado, pois assim será distinguido dos vertices que fazem parte do caminho resolutorio do labirinto
        # posteriormente todos esses vertices receberão 1, quando o caminho aleatorio for estabelecido.

        while True:
            possibilidades = grafo[atual]   # Lista de vertices para onde o ATUAL pode ir
            ir_para = possibilidades[random.randint(0, 3)]  # Escolhe um dos vertices, aleatoriamente, para onde ele pode ir

            cont = 0
            # Enquanto o vertice escolhido uma representação negativa OU o vertice que ele queira ir ja tenha sido verificado
            while ir_para == '-1' or grafo[ir_para][4] == 2 or ir_para == todos_caminhos[0][-1]:

                if cont == 8:   # Caso o laço rode 8x significa que ele não encontrou nenhum possivel vertice para ir, então deve resetar o caminho
                                # no qual estava gerando e começar um novo
                    for i in caminho_atual:
                        if i in grafo:
                                # Resetando os indices de verificação dos vertices ja usados no caminho que estava sendo gerado
                            grafo[i][4] = 0

                    caminho_atual = [atual] # Caminho volta para o vertice primitivo (atual) onde começará a fazer uma nova analise de caminho
                    grafo[atual][4] = 2     # indice de verificação o vertice torn-se 2, ja que anteriormente tinha sido resetado

                # Sorteia um novo vertice para ir, ja que o sorteado não satisfaz a condição
                ir_para = possibilidades[random.randint(0, 3)]
                cont += 1
            # Caso o vertice de IR seja aceito, adiciona ao caminho
            caminho_atual.append(ir_para)

            if grafo[ir_para][4] == 1:  # Caso tenha encontrado um vertice (Permanente) no qual pode conectar e finalizar o caminho, adicione esse caminho
                todos_caminhos.append(caminho_atual)

                # Tornando o caminho permanente; Todos os indices verificadores dos vertices do caminho gerado se tornam 1
                for i in caminho_atual:
                    grafo[i][4] = 1

                    if i in nao_utilz:
                        # Removendo os vertices do caminho que foi gerado de Não Utilizados
                        nao_utilz.remove(i)

                if len(nao_utilz) == 0:
                    # Caso todos os vertices tenham sido atilizados, a geração de caminhos aleatorios terminou
                    break

                atual = nao_utilz[random.randint(0, len(nao_utilz) - 1)]    # Escolhendo novo vertice para gerar caminho.
                caminho_atual = [atual]     # iniciando o caminho com esse vertice.
                grafo[atual][4] = 2         # Tornando ele como verificado não permanente.

            else:
                # Caso ele ainda nn tenha encontrado um caminho permanente para se conectar, atualize a posição para o proximo vertice
                # e torne ele como verificado não permanente.
                grafo[ir_para][4] = 2
                atual = ir_para

        return todos_caminhos

    def algoritmos_ConstroiGrafoFinal(self, todos_caminhos):
        # Método para contruir o GRAFO do labiritino com as adjacencias possiveis a partir dos caminhos aleatoriamente gerados
        dic_arestas = {}
        cont = 0

        # Interando cada lista contida dentro de ' todos_caminhos ', que representa um caminho ao interador ' caminho '
        for caminho in todos_caminhos:

            # Interando cada um dos vertices do caminho até o penultimo vertice
            for vert in range(len(caminho) - 1):
                aresta = [caminho[vert], caminho[vert + 1]] # Construindo a aresta
                dic_arestas['A' + str(cont)] = aresta   # Adicionando a aresta ao dicionario
                cont += 1                               # Contador de enumeração das arestas

        return dic_arestas

    def __definindoVariaveis_dePercorrer(self, dic_arestas = {}):
        # Inicia todos os dificionarios necessario para o algortimo de Dijkstra, que será usado para percorrer o labirinto
        for i in self.G.keys():
            self.__tamanhoCaminho[i] = float("inf")
            self.__rotuloVertice[i] = 0
            self.__vertAnterior[i] = 0

        for i in dic_arestas.keys():
            self.__pesoArestas[i] = 1

        self.__rotuloVertice[self.entrada] = 1
        self.__tamanhoCaminho[self.entrada] = 0

    def algoritmos_PercorrerCaminho(self, dic_arestas = {}):
        '''
        Método para percorrer o caminho resolutorio no grafo gerado!
        O algoritmo é baseado em Dijkstra
        :param dic_arestas: dicionario com todas as arestas do grafo labiritino
        :return: retorna o caminho resolutorio
        '''
        self.__definindoVariaveis_dePercorrer(dic_arestas)

        W = self.entrada

        while True:

            for i in dic_arestas:
                if dic_arestas[i][0] == W:
                    R = dic_arestas[i][1]

                    if (self.__rotuloVertice[R] == 0 and self.__tamanhoCaminho[R]
                                > self.__tamanhoCaminho[W] + self.__pesoArestas[i]):
                        self.__tamanhoCaminho[R] = self.__tamanhoCaminho[W] + self.__pesoArestas[i]
                        self.__vertAnterior[R] = W

            menor = float("inf")
            chave = ""

            for i in self.G.keys():
                if self.__tamanhoCaminho[i] < menor and self.__rotuloVertice[i] == 0:
                    menor = self.__tamanhoCaminho[i]
                    chave = i

            if chave == self.saida or menor == float("inf"):
                break

            self.__rotuloVertice[chave] = 1
            W = chave

        caminho = [self.saida]
        aux = self.saida

        while True:
            caminho.append(self.__vertAnterior[aux])

            if self.__vertAnterior[aux] == self.entrada:
                break

            aux = self.__vertAnterior[aux]

        return caminho[::- 1]