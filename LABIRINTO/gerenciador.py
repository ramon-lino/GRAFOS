from LABIRINTO.GrafoRaiz import start_grafo
from LABIRINTO.Algoritmos import algoritmos_
from LABIRINTO.plotagens import plotagem

# Proporções do grafo:
linhas = 20     # Altura do grafo
colunas = 20    # Largura do grafo

LABIRINTO_PRI = start_grafo(linhas, colunas)
ALGORITMOS_ = algoritmos_(LABIRINTO_PRI.grafo_raiz, LABIRINTO_PRI.entrada, LABIRINTO_PRI.bordas)
PLOTAGEM = plotagem((linhas*2)-1, (colunas*2)-1, ALGORITMOS_.todos_caminhos)

TODOS_CAMINHOS = ALGORITMOS_.todos_caminhos
LABIRINTO_COMP = ALGORITMOS_.algoritmos_ConstroiGrafoFinal(TODOS_CAMINHOS)
PERCORRENDO = ALGORITMOS_.algoritmos_PercorrerCaminho(LABIRINTO_COMP)

PLOTAGEM.imprime_labirinto(LABIRINTO_PRI.entrada, TODOS_CAMINHOS[0][-1])
PLOTAGEM.imprime_caminhoPercorrido(PERCORRENDO, TODOS_CAMINHOS[0])