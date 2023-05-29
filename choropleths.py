# #Dados de contaminação pela COVID-19 em 03/05/2020
# import plotly.graph_objects as go

# data = go.Choropleth(
#     locations=['USA', 'Spain', 'Italy', 'UK', 'France', 'Germany', 'Russia', 'Turkey', 'Brazil', 'Iran'],
#     locationmode='country names',
#     colorscale='YlOrRd',
#     z=[1188122, 247122, 210717, 186599, 168693, 165664, 134687, 126045, 101147, 97424],
# )

# layout = go.Layout(geo=dict(showframe=False, showcoastlines=False))

# fig = go.Figure(data=[data], layout=layout)
# fig.show()

import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv(r"C:\Users\vanes\Downloads\southAmerica-pop.csv")
fig = go.Figure(data=go.Choropleth(
 locations=df['name'], # Nome do país
 z = df['pop'].astype(int), # Dados para o Choropleth
 locationmode = 'country names', # Tipo de identificção geográfica
 colorscale = 'Reds', #escala contínua em tons de vermelho
 colorbar_title = "População",
))
fig.update_layout(
 title_text = 'População da América do Sul - 2019',
 geo_scope='south america', # Limita escopo para a América do Sul
)
fig.show()
