import matplotlib.pyplot as plt
import networkx as nx

G=nx.read_gml("graph.gml")
pos=nx.shell_layout(G) # layouts pré-definidos

# nós
nx.draw_networkx_nodes(G,pos,
 node_color='#00C0C0',
 node_size=500,
 alpha=0.8)

# arestas
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

# colocando rótulos nos nós e arestas
labels=nx.draw_networkx_labels(G,pos,font_size=10)
edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=10)
plt.axis('off')
plt.show() # display