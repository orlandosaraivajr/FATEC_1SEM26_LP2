from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Date, func, text
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///usuarios.db", echo=False)
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    data_nascimento = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Pessoa(nome='{self.nome}', data_nascimento='{self.data_nascimento}')>"


Session = sessionmaker(bind=engine)
session = Session()
hoje = date.today()

try:
    pessoas_18 = (
        session.query(Pessoa)
        .filter(
            (
                (func.strftime('%Y', text('CURRENT_DATE')) - func.strftime('%Y', Pessoa.data_nascimento))
                - (
                    (func.strftime('%m-%d', text('CURRENT_DATE')) < func.strftime('%m-%d', Pessoa.data_nascimento))
                )
            ) == 18
        )
        .all()
    )

    print("\n👩 Pessoas com 18 anos:\n")
    if pessoas_18:
        for p in pessoas_18:
            print(f"- {p.nome} (nascida em {p.data_nascimento})")
    else:
        print("Nenhuma pessoa com 18 anos encontrada.")

except Exception as e:
    print("Erro ao consultar o banco:", e)
finally:
    session.close()