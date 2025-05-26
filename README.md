# API Reserva de Salas

API desenvolvida com Flask e SQLAlchemy para gerenciamento de salas e suas reservas, seguindo o padrão MVC. Ideal para instituições que desejam controlar o uso de ambientes físicos (salas) por turmas.

## 🛠️ Tecnologias

- Python 3
- Flask
- SQLAlchemy
- MySQL
- Flasgger (Swagger UI)

## 📁 Estrutura

```
app/
├── app.py #Ponto de entrada da aplicação Flask
├── config.py #Configurações de ambiente e banco de dados
├── models/
│ ├── salas.py #Model de Salas
│ ├── reservas.py #Model de Reservas
| └── turmas_dummy.py #Model de Turmas (outra API)
├── controller/
│ ├── sala.py #Controller de Salas
│ └── reserva.py #Controller de Reservas
```

## ⚙️ Configuração

### Banco de Dados

A aplicação utiliza MySQL. O arquivo `config.py` já possui um exemplo de conexão via `pymysql`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:SenhaForte123@host.docker.internal:3306/school-system"
```
⚠️ Altere as credenciais e host conforme seu ambiente.

## 🔌 Endpoints
### SALAS
GET /salas
Lista todas as salas.

GET /salas/<id>
Retorna os dados de uma sala.

POST /salas
Cria uma nova sala.

### RESERVAS
GET /salas/reservas
Lista todas as reservas.

GET /salas/reservas/<id>
Retorna os dados de uma reserva.

POST /salas/reservas
Cria uma nova reserva.

### RESETAR
POST /salas/resetar
Reseta salas e reservas no banco


📌 Observações
Swagger UI está disponível em /apidocs (habilitado por padrão com Flasgger).


# 🛜 Integrações
#### API School-System
repositório: https://github.com/VassaloSama/School-System

#### API Activity-System
repositório: 