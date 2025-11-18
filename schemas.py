from pydantic import BaseModel
from typing import List

class DadosML(BaseModel):
    historico_credito: List[float]
    historico_debito: List[float]
    impostos: List[float]

class DadosTransacoes(BaseModel):
    transacoes: List[dict]  # {data, tipo, valor}

class PrevisaoSaida(BaseModel):
    proximo_mes: float
    confianca: float
