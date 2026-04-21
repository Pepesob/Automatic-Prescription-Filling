import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)

df = pd.read_csv("phzpoz.csv",sep=";", index_col="Lp.")


glass_code_list = df["Kod środka"].unique()


for glass_code in glass_code_list:
    df_filtered = df[(df["Kod środka"] == glass_code)]
    df_filtered2 = df_filtered[(df_filtered["Wytwórca"] == "SZAJNA")]
    print("Kod środka:", glass_code, "Info:", df_filtered["Nazwa środka"].iloc[0])
    print(df_filtered2)
    print("\n\n")

print(glass_code_list)


# df_target = df[(df["Wytwórca"] == "TARGET") & (df["Model"] == "CR")]

# print("Target code dict:")
# res_target = dict(zip(df_target["Kod środka"].apply(lambda x: x.strip()), df_target["Kod"].apply(lambda x: str(x))))
# print(res_target)

# print("------------------------------------")

# df["Cena"] = df["Cena"].apply(lambda x: float(x.replace(',', '.')))

# df_szajna = df[(df["Wytwórca"] == "SZAJNA") & (df["Cena"] <= 100)][["Wytwórca", "Model", "Kod", "Kod środka", "Cena"]]
# print(df_szajna[df_szajna["Kod środka"].str.contains("O.01.02.00.D2")])
