# Especificação do projeto

Esta é uma aplicação web desenvolvida com o framework Django e DRF.

O controle de dependencias do projeto foi realizado com o [Poetry](https://python-poetry.org/) é sugerido a instalação das dependencias através da ferramenta.


# Como executar

Primeiramente, clone este repositório através do seguinte comando:
```
git clone https://github.com/rvmoura96/django-human-resources-api.git
```

Após a conclusão do download entre no diretório:
```
cd django-human-resources-api
```

Na raíz do repositório onde encontram-se os arquivos pyproject.toml, README.MD execute o seguinte comando para a instalação das dependencias do projeto em um ambiente virtual controlado pelo poetry:
```
poetry install
```

Após a instalação execute o seguinte comando para ativar o ambiente virtual:
```
poetry shell
```

Com o ambiente virtual ativo entre no diretório itmss_api a raiz do nosso projeto Django

```
cd itmss_api
```

seguindo o passo anterior encontra-se no mesmo nivel do arquivo manage.py vamos inicializar começando a aplicando as nossas migrações do banco de dados, utilize o seguinte comando:

```
python manage.py migrate
```

Após isso vamos fazer a criação de um usuário admin necessário para acessar aos recursos da api, utilize o seguinte comando:
```
python manage.py createsuperuser --email admin@example.com --username admin
```
será solicitada a inserção de uma senha no shell onde o comando foi executado está será a senha de acesso do usuário criado acima.

Feito isso podemos iniciar nossa aplicação com o seguinte comando:
```
python manage.py runserver
```

Por padrão a aplicação será inicializada na porta 8000 do localhost.


Ao acessar a página http://localhost:8000/ em seu navegador será apresentada a interface padrão do Django Rest Framework, para acessar a cada uma das APIs basta clicar no link apresentado para cada uma das collections lembrando a necessidade de autenticação para o acesso as collections.


## Endpoint para o controle de sedes
http://localhost:8000/headquarters/
Parâmetros com exemplo para requisição do tipo **POST** utilizada para a criação de uma nova sede.
```
{
    "cnpj": "28.608.978/0001-50",
    "address": "Rua das Palmeiras",
    "city": "São Paulo",
    "country": "Brasil"
}
```
O retorno da requisição acima será algo parecido com:
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://localhost:8000/headquarters/1/
Vary: Accept

{
    "url": "http://localhost:8000/headquarters/1/",
    "cnpj": "28.608.978/0001-50",
    "address": "Rua das Palmeiras",
    "city": "São Paulo",
    "country": "Brasil"
}
```

Para acessar os detalhes de uma sede ja criada faça uma requisição do tipo **GET** ao endereço: http://localhost:8000/headquarters/{id_da_sede_desejada}

Para a atualização de dados de uma sede faça uma requisição do tipo **PUT** para o endereço: http://localhost:8000/headquarters/{id_da_sede_desejada}/ com o seguginte body:
```
{
    "cnpj": "28.608.978/0001-50",
    "address": "Rua das Palmeiras",
    "city": "São Paulo",
    "country": "Brasil"
}
```

Para a exclusão de uma sede faça uma reqquisição do tipo **DELETE** para o endereço: http://localhost:8000/headquarters/{id_da_sede_desejada}/

## Endpoint para o controle de departamentos
http://localhost:8000/departments/
Parâmetros com exemplo para requisição do tipo **POST** utilizada para a criação de um novo departamento.
```
{
    "cost_center": "FIN",
    "name": "Financeiro"
}
```
O retorno da requisição acima será algo parecido com:
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://localhost:8000/departments/1/
Vary: Accept

{
    "url": "http://localhost:8000/departments/1/",
    "cost_center": "FIN",
    "name": "Financeiro"
}

```
Para acessar os detalhes de um departamento ja criado faça uma requisição do tipo **GET** ao endereço: http://localhost:8000/departments/{id_do_departamento_desejado}

Para a atualização de dados de um departamento já criado faça uma requisição do tipo **PUT** para o endereço: http://localhost:8000/departments/{id_do_departamento_desejado}/ com o seguginte body:
```
{
    "cost_center": "FIN",
    "name": "Financeiro"
}
```

Para a exclusão de um departamento faça uma requisição do tipo **DELETE** para o endereço: http://localhost:8000/departments/{id_do_departamento_desejado}/


## Endpoints para o controle de usuários
http://localhost:8000/employees/
Parâmetros com exemplo para requisição do tipo **POST** utilizada para a criação de um novo funcionário:
```
{
    "name": "Jonas",
    "email": "jonas@email.com",
    "phone": "5511999994321",
    "birth": "2023-02-07",
    "admission": "2023-02-07",
    "shutdown": "2023-02-07",
    "city": "Indaiatuba",
    "department": "http://localhost:8000/departments/{id_department_desejado}/", # Este campo precisa ser previamente criado na api de departamentos(departments)
    "headquarter": "http://localhost:8000/headquarters/{id_headquarter_desejado}/" # Este campo precisa ser previamente criado na api de sedes utilizando o id da sede desejada (headquarters)
}
```

O retorno da requisição anterior será parecido com:

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: http://localhost:8000/employees/6/
Vary: Accept

{
    "url": "http://localhost:8000/employees/6/",
    "name": "Jonas",
    "email": "jonas@email.com",
    "phone": "5511999994321",
    "birth": "2023-02-07",
    "admission": "2023-02-07",
    "shutdown": "2023-02-07",
    "active": true,
    "city": "Indaiatuba",
    "department": "http://localhost:8000/departments/1/",
    "headquarter": "http://localhost:8000/headquarters/1/"
}
```

Para acessar os detalhes de um funcionário já criado faça uma requisição do tipo **GET** ao endereço: http://localhost:8000/employees/{id_do_funcionario_desejado}

Para a atualização de dados de um departamento já criado faça uma requisição do tipo **PUT** para o endereço: http://localhost:8000/employees/{id_do_departamento_desejado}/ com o seguginte body:
```
{
    "name": "Jonas",
    "email": "jonas@email.com",
    "phone": "5511999994321",
    "birth": "2023-02-07",
    "admission": "2023-02-07",
    "shutdown": "2023-02-07",
    "city": "Indaiatuba",
    "department": "http://localhost:8000/departments/{id_department_desejado}/", # Este campo precisa ser previamente criado na api de departamentos(departments)
    "headquarter": "http://localhost:8000/headquarters/{id_headquarter_desejado}/" # Este campo precisa ser previamente criado na api de sedes utilizando o id da sede desejada (headquarters)
}
```

Para a exclusão de um departamento faça uma requisição do tipo **DELETE** para o endereço: http://localhost:8000/employees/{id_do_funcionario_desejado}/