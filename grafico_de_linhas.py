import plotly.express as pt
import pandas as pd

from pandas import read_csv
from matplotlib import pyplot
series = read_csv(r"C:\Users\vanes\Visualizaçãoda informação - Faculdade\USD_BRL_hist.csv", header=0, index_col=0, parse_dates=True)
series.plot()
pyplot.show()
