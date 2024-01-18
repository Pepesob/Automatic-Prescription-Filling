import pandas as pd


df = pd.read_csv("phzpoz.csv",sep=";", index_col="Lp.")

df_target = df[(df["Wytwórca"] == "TARGET") & (df["Model"] == "CR")]

print("Target code dict:")
res_target = dict(zip(df_target["Kod środka"].apply(lambda x: x.strip()), df_target["Kod"].apply(lambda x: str(x))))
print(res_target)

print("------------------------------------")

df["Cena"] = df["Cena"].apply(lambda x: float(x.replace(',', '.')))

df_szajna = df[(df["Wytwórca"] == "SZAJNA") & (df["Cena"] <= 100)][["Wytwórca", "Model", "Kod", "Kod środka", "Cena"]]
print(df_szajna[df_szajna["Kod środka"].str.contains("O.01.02.00.D2")])
