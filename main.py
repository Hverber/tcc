from fastapi import FastAPI, UploadFile, File
from schemas import DadosML, DadosTransacoes, PrevisaoSaida
from service import (
    processar_dados_ml,
    carregar_de_csv,
    carregar_de_json,
    gerar_previsao
)

app = FastAPI(title="FinancIA - API Machine Learning")

@app.post("/ml/treinar")
def treinar_ml(dados: DadosML):
    return {"status": "treinado", "modelo": processar_dados_ml(dados)}

@app.post("/ml/upload-csv")
def upload_csv(file: UploadFile = File(...)):
    creditos, debitos = carregar_de_csv(file)
    return {
        "status": "OK",
        "creditos_processados": len(creditos),
        "debitos_processados": len(debitos)
    }

@app.post("/ml/upload-json")
def upload_json(dados: DadosTransacoes):
    creditos, debitos = carregar_de_json(dados)
    return {
        "status": "OK",
        "creditos_processados": len(creditos),
        "debitos_processados": len(debitos)
    }

@app.get("/ml/prever", response_model=PrevisaoSaida)
def prever():
    resultado = gerar_previsao()
    return resultado

@app.get("/")
def root():
    return {"status": "API ML do FinancIA funcionando"}
