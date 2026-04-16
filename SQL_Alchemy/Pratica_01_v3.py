from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Date, select, func, text
from datetime import datetime


engine = create_engine("sqlite:///usuarios.db", echo=False)
metadata = MetaData()

usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

with engine.connect() as conn:
    hoje = datetime.today()

    stmt = (
        select(usuarios.c.id, usuarios.c.nome, usuarios.c.data_nascimento)
        .where(
            (
                (func.strftime('%Y', text('CURRENT_DATE')) - func.strftime('%Y', usuarios.c.data_nascimento))
                - (
                    (func.strftime('%m-%d', text('CURRENT_DATE')) < func.strftime('%m-%d', usuarios.c.data_nascimento))
                )
            ) == 18
        )
    )

    resultados = conn.execute(stmt).fetchall()

    print("\n👩 Pessoas com 18 anos:\n")
    if resultados:
        for row in resultados:
            print(f"- {row.nome} (nascida em {row.data_nascimento})")
    else:
        print("Nenhuma pessoa com 18 anos encontrada.")