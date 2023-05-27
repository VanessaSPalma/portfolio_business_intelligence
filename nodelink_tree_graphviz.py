import igraph as ig
from igraph import Graph, EdgeSeq
from graphviz import Digraph

nr_vertices = 25
v_label = list(map(str, range(nr_vertices)))

G = Graph.Tree(nr_vertices, 2)  # 2 é o número de filhos por nó
lay = G.layout('rt')
position = {k: lay[k] for k in range(nr_vertices)}
Y = [lay[k][1] for k in range(nr_vertices)]
M = max(Y)
es = G.es  # sequence of edges
E = [e.tuple for e in es]  # list of edges
L = len(position)

dot = Digraph(format='png', engine='dot')  # Criação do objeto Digraph
for i in range(L):
    dot.node(str(i), v_label[i])

for edge in E:
    dot.edge(str(edge[0]), str(edge[1]))

dot.render('graph', view=True)