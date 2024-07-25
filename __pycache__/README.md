
# FastAPI Animal API

Este projeto é uma API simples desenvolvida com FastAPI para gerenciar uma lista de animais. A API permite listar, adicionar, obter e remover animais. 

## Endpoints

### Listar Animais

- URL: '/animais'
- Método HTTP: 'GET'
- Descrição: Retorna a lista de todos os animais.

### Obter Animal por ID

- URL: '/animais/{animal_id}'
- Método HTTP: 'GET'
- Descrição: Retorna os detalhes de um animal específico pelo seu ID.
- Parâmetros: 'animal_id' (str) - O ID do animal.

### Criar Animal

- URL: '/animais'
- Método HTTP: 'POST'
- Descrição: Adiciona um novo animal à lista. O ID do animal é gerado automaticamente.
- Corpo da Requisição (JSON):
```http
{
    "nome": "string",
    "idade": 0,
    "sexo": "string",
    "cor": "string"
}
```
### Remover Animal por ID
- URL: '/animais/{animal_id}'
- Método HTTP: 'DELETE'
- Descrição: Remove um animal específico da lista pelo seu ID.
- Parâmetros: 'animal_id' (str): O ID do animal.
### Observações
- A API usa uma lista em memória (banco) para armazenar os animais, o que significa que os dados serão perdidos quando o servidor for reiniciado.
- O campo 'id' é gerado automaticamente usando UUID ao criar um novo animal.





