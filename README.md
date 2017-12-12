# **ATHENA**

## DESCRIÇÃO);
Athena é uma pequena rest api que pode auxiliar na criação de aplicações para gerenciamento de consultórios.

# REQUIREMENTOS
- [python 3.6](https://www.python.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [Django 2](https://www.djangoproject.com/)
- [Django Rest Framework](http://www.django-rest-framework.org/)

## COMO USAR?
- $ mkdir restapi && cd restapi
- $ virtualenv --no-site-packages -p python3.6 env
- $ source env/bin/activate
- $ git clone https://github.com/maurxeugenio/athena.git
- $ cd athena
- $ pip install -r requirements.txt
- $ ./manage.py runserver
- Acessar localhost:8000/api/agendamentos [METHOD: GET] para acessar a lista de agendamentos

- http://localhost:8000/api/agendamento [METHODS: GET, POST, DELETE]
- [POST] http://localhost:8000/api/agendamento - Para criar um agendamento
- [GET]  http://localhost:8000/api/agendamento/1 - Para ver os detalhes de um agendamento, neste caso o parâmetro 1 é o
<id> do agendamento (objeto).
- [DELETE] http://localhost:8000/api/agendamento/2 - Para deletar um agendamento, 2 é o id do agendamento.

## DETALHES
> O projeto é divido em dois app's django para facilitar a manutenção.
- Core é destinado as regras de negocio, incluido os modelos dos objetos
- Api é destinado a serialização dos dados e da entrega ou recebimento através dos endpoints

## ENDPOINTS
> api/agendamentos/ Seleciona todos os objetos existentes em Agendamentos e sempre retorna 200

> [POST] api/agendameto/ Verifica se os dados inseridos são válidos, caso sejam é criado um novo agendamento retornando
202 neste caso e 409 caso haja conflito

> [GET] api/agendamento/1 Seleciona o objeto através do ID se este existir retorna 200, caso não exista retorna 404

> [DELETE] api/agendamento/1 Seleciona o objeto através do ID se este existir é deletado e retorna 204, caso não exista
 retorna 404 

## TESTES

## 