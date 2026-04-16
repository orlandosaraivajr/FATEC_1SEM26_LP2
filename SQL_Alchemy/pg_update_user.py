from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, text, update
from datetime import date, datetime

# 1️⃣ Conexão com o banco PostgreSQL
engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes")

metadata = MetaData()

# 2️⃣ Definição da tabela "usuarios"
usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False),
    Column('cpf', String(14), nullable=False, unique=True),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

# 3️⃣ (Opcional) Garante que a tabela exista
metadata.create_all(engine)

# 4️⃣ Solicita CPF e novo e-mail do usuário
cpf_alvo = input("Digite o CPF do usuário a ser atualizado: ")
novo_email = input("Digite o novo e-mail: ")

# 5️⃣ Atualiza o registro
with engine.connect() as conn:
    stmt = (
        update(usuarios)
        .where(usuarios.c.cpf == cpf_alvo)
        .values(email=novo_email, updated_on=datetime.now())
    )
    result = conn.execute(stmt)
    conn.commit()
    if result.rowcount > 0:
        print(f"E-mail atualizado com sucesso para o CPF {cpf_alvo}.")
    else:
        print(f"Nenhum usuário encontrado com o CPF {cpf_alvo}.")

# 6️⃣ Exibe o registro atualizado
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios WHERE cpf = :cpf"), {"cpf": cpf_alvo})
    row = result.fetchone()
    if row:
        print("\nUsuário atualizado:")
        print(row)
