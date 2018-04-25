from grafo import Grafo

g = Grafo() # Iniciando a variavel " g ", que representa um Grafo.

## Função para entrada dos vertices ##
def ent_vertices():
    try:
        vert = "J, C, E, P, M, T, Z"
        vert = vert.split(", ")     # Separando a String de entrada em uma lista com cada Vertices como elemento.

        for i in vert:
            g.adicionaVertice(i)    # Adicionando Vertices na variavel " g ".
        return vert

    except:
        print("Vertices invalidos! Formato não aceito.")
        print("Digite no formato: 'A, B, C, D'")

def ent_arestas():
    dic_aux = {}
    print("As arestas devem ser informada no modelo: a1(J-C), a2(C-E), a3(C-E)")
    ares = "a1(J-C), a2(C-E), a3(E-C), a4(C-P), a5(C-P), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)"
    ares = ares.split(", ")         # Separando a String de entrada em uma lista com cada Par de Aresta como elemento,

    try:
        for i in range(len(ares)):
            ares[i] = ares[i].replace(")","(")          # Uniformisando os parenteses na string, substituindo para um unico tipo "(" - Abre Parenteses -.
            ares[i] = ares[i].split("(")                # Separando a String que compõe as arestas pelo parenteses anteriormente uniformizado.
            g.adicionaAresta(ares[i][0], ares[i][1])    # Adicionando as Arestas na variavel " g "
            dic_aux[ares[i][0]] = ares[i][1]            # Criando Dicionario de Arestas

        return dic_aux
    except:
        print("Arestas invalidas! Formato não aceito ou não correspondentes aos vertices.")
        print("Digite no formato: 'a1(A-B), a2(C-D), a3(E-F)' - com conexões correspondentes aos vertices.")

def VerifyAres(S, DicA = {}):
    for i in DicA.keys():
        if DicA[i] == S:
            return True

    return False

def NaoAdj(V = [], A = {}):
    NaoAdjc = []
    for i in range(len(V)):
        for e in range(i, len(V)):

            if V[i] != V[e]:
                StringAres = V[i]
                StringAres += '-'
                StringAres += V[e]
                Verify = VerifyAres(StringAres, A)

                if (Verify == False):
                    NaoAdjc.append(StringAres)

    return NaoAdjc

def adjc_ele_mesmo(V = [], A = {}):
    for i in range(len(V)):
        StringAres = V[i]
        StringAres += "-"
        StringAres += V[i]

        Verify = VerifyAres(StringAres, A)

        if Verify == True:
            return Verify

    return Verify

def Grau_Vertice(v = '', A = {}):
    cont = 0

    for i in A.keys():
        if v == A[i][0] or v == A[i][2]:
            cont += 1

    return cont

def Insidencia_Arestas(v = '', A = {}):



vertices = ent_vertices()
arestas = ent_arestas()
Nao_adjcentes = NaoAdj(vertices, arestas)
AdjcEleMesmo = adjc_ele_mesmo(vertices, arestas)
GrauVertice = Grau_Vertice('C', arestas)

print(g)
print(Nao_adjcentes)
print(AdjcEleMesmo)
print(GrauVertice)

