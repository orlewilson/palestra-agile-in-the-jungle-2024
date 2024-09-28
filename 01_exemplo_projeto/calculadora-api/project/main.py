"""
Exemplo de Calculadora com as 4 operações

"""

# Bibliotecas
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

# Classe para representar os valores usados em cada operação
class Valores(BaseModel):
    a: int 
    b: int 

# Classe para representar a reposta após execução da operação
class Resposta(BaseModel):
    a: int = Field(default=1)
    b: int = Field(default=1)
    result: int = Field(default=1)

# @app.post('/somar') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /somar
@app.post('/somar')
async def somar(valores: Valores) -> Resposta:
    """Método que será chamado quando for requisitada a rota /somar"""
    resultado = valores.a + valores.b

    return Resposta(a=valores.a, b=valores.b, result=resultado)

# @app.post('/subtrair') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /subtrair
@app.post('/subtrair')
async def subtrair(valores: Valores) -> Resposta:
    """Método que será chamado quando for requisitada a rota /subtrair"""
    resultado = valores.a - valores.b
    
    return Resposta(a=valores.a, b=valores.b, result=resultado)

# @app.post('/multiplicar') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /multiplicar
@app.post('/multiplicar')
async def multiplicar(valores: Valores) -> Resposta:
    """Método que será chamado quando for requisitada a rota /multiplicar"""
    resultado = valores.a * valores.b
    
    return Resposta(a=valores.a, b=valores.b, result=resultado)

# @app.post('/dividir') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /dividir
@app.post('/dividir')
async def dividir(valores: Valores) -> Resposta:
    """Método que será chamado quando for requisitada a rota /dividir"""

    # # sem correção
    # resultado = int(valores.a / valores.b)
    
    # com correção
    if valores.b == 0:
        return JSONResponse(
            status_code = 422,
            content = {
                "detail": [
                    {
                    "type": "zero_division_error",
                    "loc": [
                        "body",
                        "b"
                    ],
                    "msg": "Input should be non-zero, got zero number",
                    "input": valores.b
                    }
                ]
            }
        )
    else:
        resultado = int(valores.a / valores.b)

    return Resposta(a=valores.a, b=valores.b, result=resultado)
