import pandas as pd

df = pd.read_csv("Aula05/StudentsPerformance.csv")

df.columns = df.columns.str.replace(" ", "_").str.replace("/", "_")

#27. Perguntas analíticas com filtros

#1- Quais estudantes tiveram média geral maior ou igual a 80?
df["media_geral"] = (df["math_score"] + df["writing_score"] + df["reading_score"]) / 3
# print(df[(df["media_geral"] >= 80)])



#2- Quais estudantes fizeram curso preparatório e tiveram média geral maior ou igual a 80?
# print(df[(df["media_geral"] >= 80) & (df["test_preparation_course"] == "completed")])



#3- Quais estudantes não fizeram curso preparatório e foram reprovados?
def situacao_estudante(media):
    if media >= 60:
        return "Aprovado"
    else:
        return "Reprovado"

df["situacao"] = df["media_geral"].apply(situacao_estudante)

# print(df[(df["test_preparation_course"] == "none") & (df["situacao"] == "Reprovado")])



#4- Quais estudantes tiveram nota de matemática menor que 50, mas nota de leitura maior ou igual a 70?
#print(df[(df["math_score"] < 50) & (df["reading_score"] >= 70)])

print(df[(df["math_score"] < 40) & (df["reading_score"] > 70)])
