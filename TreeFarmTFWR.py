import pandas as pd

# URL do arquivo ICF
url = "https://raw.githubusercontent.com/fserb/pt-br/refs/heads/master/icf"

# Lendo o arquivo direto com pandas
df = pd.read_csv(url, sep=" ", names=["palavra", "icf"])

# Filtrar palavras de 5 letras
df_5 = df[df["palavra"].str.len() == 5]

# Ordenar pela maior probabilidade (menor ICF)
df_5_sorted = df_5.sort_values("icf")

# Transformar em lista
lista_palavras = df_5_sorted["palavra"].tolist()

print(lista_palavras[:50])   # mostra as 50 mais frequentes

