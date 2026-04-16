from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert
from datetime import datetime
from faker import Faker
import random

fake = Faker('pt_BR')
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

metadata.create_all(engine)

def gerar_usuarios_fake(qtd=10000):
    usuarios_fake = []
    for _ in range(qtd):
        data_nasc = fake.date_between(start_date='-75y', end_date='-15y') 
        usuarios_fake.append({
            'nome': fake.name(),
            'cpf': fake.cpf(),
            'email': fake.unique.email(),
            'telefone': fake.phone_number(),
            'data_nascimento': data_nasc
        })
    return usuarios_fake

usuarios_fake = gerar_usuarios_fake(10000)

with engine.connect() as conn:
    conn.execute(insert(usuarios), usuarios_fake)
    conn.commit()


from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
    for row in result:
        print(row)
