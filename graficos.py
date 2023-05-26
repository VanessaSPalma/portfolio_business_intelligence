import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

musicas = ('Vivo por Ti' , 'É o Senhor' , 'Meu amor' , 'Me escolheu' , 'Ele vem')
indice = np.arange(len(musicas))
acessos = [1068254,866216,849895,763652,758198]
plt.bar(indice, acessos)
plt.xticks(indice, musicas)
plt.ylabel('Acessos')
plt.title('Ranking do Spotify 26.maio.2023')
plt.show()
