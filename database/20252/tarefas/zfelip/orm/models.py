from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Projeto(Base):
    __tablename__ = "projeto"

    codigo = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)

    atividades = relationship("Atividade", back_populates="projeto_rel")

class Atividade(Base):
    __tablename__ = "atividade"

    codigo = Column(Integer, primary_key=True)
    descricao = Column(String)
    projeto = Column(Integer, ForeignKey("projeto.codigo"))
    data_inicio = Column(Date)
    data_fim = Column(Date)

    projeto_rel = relationship("Projeto", back_populates="atividades")
