import pandas as pd

df = pd.read_csv("Aula04/dados.csv")

df["Receita"] = df["Quantity"] * df["Price per Unit"]

def classificar_idade (idade):
    if pd.isna(idade):
        return 'Sem informação'
    elif idade >= 60:
        return 'Sênior'
    elif 40 <= idade < 60:
        return 'Adulto Maduro'
    elif 25 <= idade < 40:
        return 'Adulto'
    else:
        return 'Jovem'

df["Classificação"] = df["Age"].apply(classificar_idade)

valor_total_vendido = df["Receita"].sum()
valor_medio_venda = df["Receita"].mean()
maior_venda = df["Receita"].max()
menor_venda = df["Receita"].min()
categoria_maxima = df["Product Category"].value_counts()
vendas_genero = df["Gender"].value_counts()
media_idade = df["Age"].mean()

print(f"Receita Total: {valor_total_vendido:.2f}\n")
print(f"Receita Média: {valor_medio_venda:.2f}\n")
print(f"Maior Venda: {maior_venda:.2f}\n")
print(f"Menor Venda: {menor_venda:.2f}\n")
print(f"Categoria com mais vendas: {categoria_maxima}\n")
print(f"Vendas por gênero: {vendas_genero}\n")
print(f"Média das idades: {media_idade:.2f}")



