import pickle
import numpy as np
from pathlib import Path

class ModeloFinancIA:
    def __init__(self):
        self.modelo = None
        self.modelo_path = Path("models/modelo_treinado.pkl")

    def treinar(self, creditos, debitos, impostos):
        creditos = np.array(creditos) if creditos else np.array([0])
        debitos = np.array(debitos) if debitos else np.array([0])
        impostos = np.array(impostos) if impostos else np.array([0])

        tendencia = (np.mean(creditos) - np.mean(debitos)) - np.mean(impostos)

        self.modelo = {"tendencia": float(tendencia)}
        self._salvar()

        return self.modelo

    def prever(self):
        if self.modelo is None:
            self._carregar()

        tendencia = self.modelo["tendencia"]
        previsao = tendencia * 1.12  # ajuste simples
        return previsao

    def _salvar(self):
        self.modelo_path.parent.mkdir(exist_ok=True)
        with open(self.modelo_path, "wb") as f:
            pickle.dump(self.modelo, f)

    def _carregar(self):
        if not self.modelo_path.exists():
            raise FileNotFoundError("Nenhum modelo foi treinado ainda.")
        with open(self.modelo_path, "rb") as f:
            self.modelo = pickle.load(f)
