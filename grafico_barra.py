import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

musicas = ('Vivo por Ti' , 'É o Senhor' , 'Meu amor' , 'Me escolheu' , 'Ele vem')
indice = np.arange(len(musicas))
acessos = [1068254,866216,849895,763652,758198]
plt.bar(indice, acessos, edgecolor='purple', color=["cyan","red","gray","yellow",(0.8,0.5,1.0,1.0)])
plt.xticks(indice, musicas , color='purple')
plt.ylabel('Acessos', color='purple')
plt.title('Ranking do Spotify 26.maio.2023', color='purple')
plt.show()
