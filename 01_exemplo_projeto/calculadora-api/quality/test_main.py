from fastapi.testclient import TestClient
from project.main import app

client = TestClient(app)

def test_somar_a_b_validos():
    response = client.post(
        "/somar",
        json={"a": 1, "b": 2},
    )
    assert response.status_code == 200

    assert response.json() == {"a": 1, "b": 2, "result" :3 }

def test_somar_a_invalido_b_valido():
    response = client.post(
        "/somar",
        json={"a": 2.2, "b": 2},
    )
    assert response.status_code == 422
    
    assert response.json() == {"detail": [
        {
            "type": "int_from_float",
            "loc": [
                "body",
                "a"
            ],
            "msg": "Input should be a valid integer, got a number with a fractional part",
            "input": 2.2
        }
    ]}

def test_subtrair_a_b_validos():
    response = client.post(
        "/subtrair",
        json={"a": 3, "b": 2},
    )
    assert response.status_code == 200
    assert response.json() == {"a": 3, "b": 2, "result" : 1 }

def test_subtrarir_a_invalido_b_valido():
    response = client.post(
        "/subtrair",
        json={"a": 2.2, "b": 2},
    )
    assert response.status_code == 422
    
    assert response.json() == {"detail": [
        {
            "type": "int_from_float",
            "loc": [
                "body",
                "a"
            ],
            "msg": "Input should be a valid integer, got a number with a fractional part",
            "input": 2.2
        }
    ]}

def test_multiplicar_a_b_validos():
    response = client.post(
        "/multiplicar",
        json={"a": 2, "b": 2},
    )
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 2, "result" : 4 }

def test_multiplicar_a_invalido_b_valido():
    response = client.post(
        "/multiplicar",
        json={"a": 2.2, "b": 2},
    )
    assert response.status_code == 422
    
    assert response.json() == {"detail": [
        {
            "type": "int_from_float",
            "loc": [
                "body",
                "a"
            ],
            "msg": "Input should be a valid integer, got a number with a fractional part",
            "input": 2.2
        }
    ]}

def test_dividir_a_b_validos():
    response = client.post(
        "/dividir",
        json={"a": 2, "b": 2},
    )
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 2, "result" : 1 }

def test_dividir_a_invalido_b_valido():
    response = client.post(
        "/dividir",
        json={"a": 2.2, "b": 2},
    )
    assert response.status_code == 422
    
    assert response.json() == {"detail": [
        {
            "type": "int_from_float",
            "loc": [
                "body",
                "a"
            ],
            "msg": "Input should be a valid integer, got a number with a fractional part",
            "input": 2.2
        }
    ]}