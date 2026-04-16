from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, text, insert
from datetime import date, datetime

# Conexão com o banco PostgreSQL
engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes")

metadata = MetaData()

# Definição da tabela "usuarios"
usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False, unique=True),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

from sqlalchemy import Index
Index('ix_cpf', 'cpf')

# Criação da tabela no banco (se não existir)
metadata.create_all(engine)

# Inserção de dois registros
with engine.connect() as conn:
    conn.execute(
        insert(usuarios),
        [
            {
                'nome': 'Ana Silva',
                'cpf': '123.456.789-00',
                'email': 'ana.silva@example.com',
                'telefone': '(11) 99999-1111',
                'data_nascimento': date(1995, 5, 10)
            },
            {
                'nome': 'Carlos Souza',
                'cpf': '987.654.321-00',
                'email': 'carlos.souza@example.com',
                'telefone': '(21) 98888-2222',
                'data_nascimento': date(1990, 8, 25)
            }
        ]
    )
    conn.commit()

# Consulta e exibição dos registros
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios;"))
    for row in result:
        print(row)
