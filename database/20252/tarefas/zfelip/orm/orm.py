from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Projeto, Atividade

engine = create_engine("postgresql://postgres:12345@localhost:5432/atividade_db")
Session = sessionmaker(bind=engine)
session = Session()

print("Conexão realizada")

nova = Atividade(
    descricao="Atividade via ORM",
    projeto=1,
    data_inicio="2024-01-01",
    data_fim="2024-02-01"
)
session.add(nova)
session.commit()

session.execute(text("UPDATE projeto SET responsavel = 4 WHERE codigo = 1"))
session.commit()

projetos = session.query(Projeto).all()

for p in projetos:
    print(f"Projeto: {p.nome}")
    for a in p.atividades:
        print("  -", a.descricao)
