# Tarefa - ODBC e ORM

## Links para os Scripts SQL
- [01-create-tables.sql](./scripts/01-create-tables.sql)
- [02-insert-data.sql](./scripts/02-insert-data.sql)

## Links para os programas criados

#### Programa usando ODBC (PyODBC)
- [odbc.py](./odbc/odbc.py)

#### Programa usando ORM (SQLAlchemy)
- [models.py](./orm/models.py)
- [orm.py](./orm/orm.py)

## ODBC em Python
ODBC é um padrão que permite que aplicações se comuniquem com diferentes sistemas de banco de dados através de drivers específicos, garantindo independência da linguagem e do banco utilizado. No Python, o principal pacote para trabalhar com ODBC é o PyODBC, que funciona como uma ponte entre o código Python e o driver ODBC instalado no sistema operacional. Com ele, a aplicação estabelece uma conexão com o banco a partir de uma string de conexão que inclui informações como servidor, banco de dados, usuário, senha e driver. Depois disso, é possível executar comandos SQL diretamente, como inserções, atualizações e consultas, e recuperar os resultados em formato de linhas. O ODBC é útil quando se deseja um controle direto do SQL e quando a camada de comunicação precisa ser padronizada entre vários bancos. Nesta tarefa, utilizei o PyODBC para conectar ao PostgreSQL e executar comandos SQL como inserir uma atividade, atualizar o líder de um projeto e listar projetos e atividades.

## ORM em Python - SQLAlchemy
ORM é uma técnica que permite trabalhar com bancos de dados relacionais usando objetos da linguagem de programação, em vez de escrever comandos SQL diretamente. Através do ORM, tabelas viram classes, colunas viram atributos e registros são representados como instâncias dessas classes. Isso torna o código mais organizado, seguro e fácil de manter. Em Python, o framework ORM escolhido foi o SQLAlchemy, amplamente utilizado no mercado e conhecido por sua flexibilidade. Com ele, é possível mapear tabelas para classes, definir relações entre entidades, criar consultas de forma declarativa e manipular dados como objetos. O SQLAlchemy também permite trabalhar tanto em modo ORM quanto escrevendo SQL manual, quando necessário. Nesta atividade, utilizei o SQLAlchemy para conectar ao banco AtividadesBD, criar modelos representando as tabelas, inserir uma nova atividade, atualizar o líder de um projeto e listar todos os projetos e suas atividades.