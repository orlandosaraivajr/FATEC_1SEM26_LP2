from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime

import time
from functools import wraps
def medir_tempo(func):
    """Decorator que mede o tempo de execução de uma função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()     # tempo final
        duracao = fim - inicio
        print(f"⏱ Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        return resultado
    return wrapper

engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2", echo=False)
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

@medir_tempo
def LGPD(row):
    # Transformar row em lista para permitir modificação
    row = list(row)

    # Campo[1] — Anonimizar nome
    nomes = row[1].split(" ")
    anon_nome = []
    for nome in nomes:
        if len(nome) > 1:
            anon_nome.append(nome[0] + "*" * (len(nome) - 1))
        else:
            anon_nome.append(nome)
    row[1] = " ".join(anon_nome)

    # Campo[2] — Anonimizar CPF
    cpf = row[2]
    cpf_parts = cpf.split(".")
    if len(cpf_parts) == 3 and "-" in cpf_parts[2]:
        cpf_parts[1] = "***"
        cpf_parts[2] = "***-**"
        row[2] = ".".join(cpf_parts)
    else:
        row[2] = "***.***.***-**"  # fallback

    # Campo[3] — Anonimizar E-mail
    email = row[3]
    if "@" in email:
        user, domain = email.split("@", 1)
        if len(user) > 1:
            user = user[0] + "*" * (len(user) - 1)
        else:
            user = "*"
        row[3] = f"{user}@{domain}"
    else:
        row[3] = "*" * len(email)  # fallback

    # Campo[4] — Anonimizar telefone
    telefone = row[4]
    digits = "".join(filter(str.isdigit, telefone))
    if len(digits) >= 4:
        row[4] = digits[-4:]
    else:
        row[4] = "****"

    return tuple(row)

'''
users = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
    for row in result:
        row = LGPD(row)
        users.append(row)

for user in users:
    print(user)
'''