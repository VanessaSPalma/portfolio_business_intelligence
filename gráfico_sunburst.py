import pandas as pd
import plotly.graph_objects as go

salary_file = "salary_data.csv"
df = pd.read_csv(salary_file)
df["Gender"] = df["Gender"].str.strip()  # Remove espaços em branco extras
df["Job Title"] = df["Job Title"].str.strip().str.lower()  # Remove espaços e converte para minúsculas
df["Gender"] = df["Gender"].str.lower()  # Converte para minúsculas

df_filtered = df[(df["Age"] == 27) & (df["Job Title"] == "software engineer")]

if not df_filtered.empty:
    count_male = df_filtered[df_filtered["Gender"] == "male"].shape[0]
    count_female = df_filtered[df_filtered["Gender"] == "female"].shape[0]
else:
    count_male = 0
    count_female = 0

fig = go.Figure(go.Sunburst(
    labels=["Total", "Homens", "Mulheres"],
    parents=["", "Total", "Total"],
    values=[count_male + count_female, count_male, count_female],
    branchvalues="total",
))

fig.update_layout(
    title={
        "text": "Quantidade de Homens e Mulheres com 27 anos em cargo de Software Engineer",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top"
    },
    sunburstcolorway=["blue", "magenta"],
)

# Adiciona a legenda no canto inferior direito
fig.add_annotation(
    x=1,
    y=-0.1,
    text="Legenda:<br>"
         "<span style='color:blue'>Azul:</span> Quantidade Total<br>"
         "<span style='color:magenta'>Magenta:</span> Quantidade de Homens<br>"
         "Valor: Quantidade de Mulheres",
    showarrow=False,
    font=dict(size=12),
    align="right",
)

fig.show()
