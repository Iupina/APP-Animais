from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4


# Inicializa a aplicação FastAPI
app = FastAPI()


# Define o modelo de dados para Animal
class Animal(BaseModel):
    id: Optional[str] = None
    nome: str
    idade: int
    sexo: str
    cor: str 


# Inicializa uma lista vazia para armazenar os animais
banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    """
    Endpoint para listar todos os animais.
    
    Retorna:
        List[Animal]: Lista de todos os animais cadastrados.
    """
    return banco


@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    """
    Endpoint para obter detalhes de um animal específico pelo ID.
    
    Parâmetros:
        animal_id (str): O ID do animal a ser buscado.
    
    Retorna:
        dict: Detalhes do animal ou uma mensagem de erro se não encontrado.
    """
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'error': 'Animal não localizado'}


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    """
    Endpoint para remover um animal pelo ID.
    
    Parâmetros:
        animal_id (str): O ID do animal a ser removido.
    
    Retorna:
        dict: Mensagem de sucesso ou erro se o animal não for encontrado.
    """
    posicao = -1
    # buscar a posição do animal
    for index, animal in enumerate (banco):
        if animal_id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'error': 'Animal não localizado'}


@app.post('/animais')
def criar_animal(animal: Animal):
    """
    Endpoint para criar um novo animal.
    
    Parâmetros:
        animal (Animal): Dados do animal a ser criado.
    
    Retorna:
        dict: Mensagem de sucesso e detalhes do animal criado.
    """
    animal.id = str(uuid4())
    banco.append(animal)
    return None
