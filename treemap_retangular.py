import plotly.express as px
import pandas as pd

salary_file = "salary_data.csv"

df = pd.read_csv(salary_file)

salary_col = "Salary"
gender_col = "Gender"

df.dropna(subset=[salary_col], inplace=True)  # Remove as linhas com valores ausentes na coluna "Salary"

df.sort_values(by=salary_col, ascending=False, inplace=True)  # Ordena o DataFrame pelo salário em ordem decrescente

df["all"] = "all"  # Garante um único nó raiz

fig = px.treemap(df, path=[salary_col, gender_col], values=salary_col)

fig.update_layout(
    title={
        'text': 'Salário de homens x Salário de mulheres',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

fig.show()
