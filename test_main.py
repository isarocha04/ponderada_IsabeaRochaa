from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/create-user", json={"name": "Teste", "password": "teste", "email": ""})
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário Teste foi cadastrado(a) com sucesso!"}


def test_get_users():
    response = client.get("/get-users")
    assert response.status_code == 200
                                                 

def test_update_user():
    response = client.put("/update-user/1", json={"name": "Teste", "password": "teste", "email": ""})
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário Teste foi atualizado(a) com sucesso!"}

def test_delete_user():
    response = client.delete("/delete-user/3")
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário 3 foi deletado(a) com sucesso!"}

def test_create_story():
    response = client.post("/create-story", json={"title": "Teste", "description": "teste", "category": "teste"}, headers={"Authorization" : "Bearer 5"})
    assert response.status_code == 200

def test_get_stories():
    response = client.get("/get-stories")
    assert response.status_code == 200

def test_update_story():
    response = client.put("/update-story/2", json={"title": "Teste", "description": "teste", "category": ""})
    assert response.status_code == 200
    assert response.json() == {"message": "História Teste foi atualizada com sucesso!"}

def test_delete_story():
    response = client.delete("/delete-story/2")
    assert response.status_code == 200
    assert response.json() == {"message": "História 2 foi deletada com sucesso!"}
