#Grafo utilizando arquivo Pajek
import matplotlib.pyplot as plt
import networkx as nx

G=nx.read_pajek("football.net")
G1=nx.DiGraph(G)
pos=nx.circular_layout(G1) # layouts pré-definidos

# nós
nx.draw_networkx_nodes(G1,pos,
 node_color='#C0C0F0',
 node_size=500,
 alpha=0.8)

# arestas
nx.draw_networkx_edges(G1,pos,width=1.0,alpha=0.5)

# colocando rótulos nos nós
labels=nx.draw_networkx_labels(G1,pos,font_size=10)
plt.axis('off')
plt.show() # display