import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/")
DATA_PATH.mkdir(exist_ok=True)

def salvar_csv(uploaded_file):
    file_path = DATA_PATH / "historico.csv"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.file.read())
    return file_path

def tratar_csv(caminho):
    df = pd.read_csv(caminho)

    colunas_obrigatorias = ["data", "tipo", "valor"]
    if not all(col in df.columns for col in colunas_obrigatorias):
        raise ValueError("CSV inválido: precisa de data, tipo, valor.")

    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values("data")

    creditos = df[df["tipo"] == "receita"]["valor"].tolist()
    debitos = df[df["tipo"] == "despesa"]["valor"].tolist()

    return creditos, debitos

def tratar_json(dados):
    creditos, debitos = [], []
    for tx in dados:
        if tx["tipo"] == "receita":
            creditos.append(tx["valor"])
        elif tx["tipo"] == "despesa":
            debitos.append(tx["valor"])
    return creditos, debitos
