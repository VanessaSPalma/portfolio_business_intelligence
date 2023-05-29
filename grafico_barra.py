import matplotlib.pyplot as plt
import pandas as pd

salary_file = "salary_data.csv"
df = pd.read_csv(salary_file)

# Filtrar apenas as idades entre 22 e 31 anos
df_filtered = df[(df["Age"] >= 22) & (df["Age"] <= 31)]

# Contar a frequência dos cargos e selecionar os 10 mais frequentes
top_10_jobs = df_filtered["Job Title"].value_counts().head(10)

# Filtrar o DataFrame apenas para os 10 tipos de cargos mais frequentes
df_filtered = df_filtered[df_filtered["Job Title"].isin(top_10_jobs.index)]

# Agrupar por idade e cargo, contando a quantidade de ocorrências
grouped_data = df_filtered.groupby(["Age", "Job Title"]).size().unstack()

# Plotar as barras horizontais
grouped_data.plot(kind="barh", stacked=True, colormap="viridis")

# Configurar os eixos e legendas
plt.xlabel('Quantidade')
plt.ylabel('Cargos')
plt.title('Distribuição dos Cargos por Idade (Top 10)')
plt.legend(title='Idade')

plt.tight_layout()
plt.show()
