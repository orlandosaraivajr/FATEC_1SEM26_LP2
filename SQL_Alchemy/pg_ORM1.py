from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Base ORM
Base = declarative_base()

# Modelo User
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# Conexão com PostgreSQL (ajuste conforme necessário)
engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes", echo=False)

# Criação das tabelas
Base.metadata.create_all(engine)

# Criação de sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de um usuário
'''
novo_user = User(
    username="maria",
    email_address="maria@example.com",
    phone="(11) 99999-1111",
    password="123456"
)
session.add(novo_user)
session.commit()
'''
# Consulta o usuário inserido
user = session.query(User).first()
print("Usuário encontrado:", user.username)


