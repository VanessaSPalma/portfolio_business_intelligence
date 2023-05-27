#BCbwH626Z9kjaKS-PsHP
import quandl
import pandas as pd
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = 'BCbwH626Z9kjaKS-PsHP'
tesla = quandl.get('WIKI/TSLA')
ibm = quandl.get('WIKI/IBM')
plt.plot(ibm.index, ibm['Adj. Close'])
plt.title('Ações da IBM')
plt.ylabel('Preço ($)');
plt.show()
plt.plot(tesla.index, tesla['Adj. Close'], 'r')
plt.title('Ações da Tesla')
plt.ylabel('Preço ($)')
plt.show()
