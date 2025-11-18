# service.py
from model import ModeloFinancIA
from preprocess import tratar_csv, salvar_csv, tratar_json
from schemas import DadosML, DadosTransacoes

modelo = ModeloFinancIA()

def processar_dados_ml(dados: DadosML):
    return modelo.treinar(
        creditos=dados.historico_credito,
        debitos=dados.historico_debito,
        impostos=dados.impostos
    )

def carregar_de_csv(arquivo):
    caminho = salvar_csv(arquivo)
    creditos, debitos = tratar_csv(caminho)
    modelo.treinar(creditos, debitos, impostos=[0])  # impostos podem vir da API Fiscal
    return creditos, debitos

def carregar_de_json(payload: DadosTransacoes):
    creditos, debitos = tratar_json(payload.transacoes)
    modelo.treinar(creditos, debitos, impostos=[0])
    return creditos, debitos

def gerar_previsao():
    previsao = modelo.prever()
    return {
        "proximo_mes": previsao,
        "confianca": 0.82
    }
