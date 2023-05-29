import networkx as nx
import matplotlib.pyplot as plt

# G=nx.Graph() #o método Graph cria um grafo não-orientado
# G.add_nodes_from([1,2,3,4]) #definição dos nós
# G.add_edges_from([(1,2),(1,3),(2,4),(3,4),(2,3)]) #definição das arestas
# nx.draw_random(G) #desenha os nós em posições aleatórias
# plt.show()


import matplotlib.pyplot as plt
import networkx as nx
G=nx.complete_bipartite_graph(3,3) # grafo bipartido pré-definido
pos=nx.shell_layout(G) # layout pré-definido
# nós
nx.draw_networkx_nodes(G,pos,
 nodelist=[0,1,2],
 node_color='#d82c97',
 node_size=500,
 alpha=0.8)
nx.draw_networkx_nodes(G,pos,
 nodelist=[3,4,5],
 node_color='#fbdeec',
 node_size=500,
 alpha=0.8)
# arestas
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
# colocando rótulos
labels={}
labels[0]=r'$U$'
labels[1]=r'$S$'
labels[2]=r'$❤$'
labels[3]=r'$S$'
labels[4]=r'$E$'
labels[5]=r'$J$'
nx.draw_networkx_labels(G,pos,labels,font_size=16)
plt.axis('off')
plt.show() # exibe o grafo