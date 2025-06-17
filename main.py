import pandas as pd

def lire_csv(chemin):
    return pd.read_csv(chemin, sep=';')

def match_plus_parie(chemin):
    df = lire_csv(chemin)
    df["n_mises"] = df["n_mises"].astype(str).str.replace(" ", "").astype(int)
    top = df.sort_values(by="n_mises", ascending=False).iloc[0]

    return {
        "equipe_1": top["equipe_1"],
        "equipe_2": top["equipe_2"],
        "n_mises": top["n_mises"]
    }
