# Tarefa - Python e MongoDB (Sistema de Gestão de Atividades)

Este projeto implementa um sistema simples de gerenciamento de atividades utilizando:

- **Python 3**
- **MongoDB**
- Arquitetura organizada em camadas:
  - `models/`
  - `repositories/`
  - `services/`
  - `controllers/`
  - `config/`
  - `main.py`
  - `docker-compose.yml`

## Funcionalidades

- CRUD de **Usuários**
- CRUD de **Atividades**
- Consultas complexas utilizando *aggregation*
- Código modular e organizado

## Como executar o projeto
### Observação:
Certifique-se de estar no local correto
```sh
cd .\database\20252\tarefas\zfelip\T4-SistemaGestaoAtv
```
### 1. Suba o MongoDB via Docker

```sh
docker compose up -d
```

### 2. Instale as dependências

```sh
pip install pymongo
```

### 3. Execute o projeto

```sh
python main.py
```

## Estrutura do Projeto

```
config/
  database.py

models/
  user.py
  activity.py

repositories/
  user.py
  activity.py

services/
  user.py
  activity.py

controllers/
  user.py
  activity.py

main.py
tarefa-mongodb.md
docker-compose.yml
```

## Docker Compose

O projeto inclui um serviço MongoDB para uso.
