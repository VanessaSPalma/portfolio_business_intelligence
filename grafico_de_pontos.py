import plotly.express as pt
import pandas as pd

from pandas import read_csv
from matplotlib import pyplot
series = read_csv(r"C:\Users\vanes\Visualizaçãoda informação - Faculdade\USD_BRL_hist.csv", header=0, index_col=0, parse_dates=True)
series2019 = series["01-01-2019":"31-12-2019"]
series2019.plot(style='k.')
pyplot.show()
