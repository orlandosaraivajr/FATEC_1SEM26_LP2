from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, Numeric, String, Boolean, DateTime,
    ForeignKey, insert, select
)
from datetime import datetime

# 1️⃣ Conexão com o banco PostgreSQL
engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes")

# 2️⃣ Criação do objeto de metadados
metadata = MetaData()

# 3️⃣ Definição das tabelas
users = Table(
    'users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

cookies = Table(
    'cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)

orders = Table(
    'orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),
    Column('shipped', Boolean(), default=False)
)

line_items = Table(
    'line_items', metadata,
    Column('line_item_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)

# 4️⃣ Criação das tabelas no banco (se não existirem)
metadata.create_all(engine)
# engine = create_engine('sqlite:///:memory:')
# metadata.create_all(engine)

# 5️⃣ Inserção de dados
with engine.connect() as conn:
    # Usuários
    conn.execute(
        insert(users),
        [
            {
                'username': 'ana',
                'email_address': 'ana@example.com',
                'phone': '(11)99999-1111',
                'password': '123456'
            },
            {
                'username': 'carlos',
                'email_address': 'carlos@example.com',
                'phone': '(21)98888-2222',
                'password': '654321'
            }
        ]
    )

    # Cookies
    conn.execute(
        insert(cookies),
        [
            {
                'cookie_name': 'Chocolate Chip',
                'cookie_recipe_url': 'http://example.com/chocochip',
                'cookie_sku': 'CC01',
                'quantity': 100,
                'unit_cost': 1.50
            },
            {
                'cookie_name': 'Oatmeal Raisin',
                'cookie_recipe_url': 'http://example.com/oatmeal',
                'cookie_sku': 'OR02',
                'quantity': 200,
                'unit_cost': 1.00
            }
        ]
    )

    # Pedidos
    conn.execute(
        insert(orders),
        [
            {'user_id': 1, 'shipped': False},
            {'user_id': 2, 'shipped': True}
        ]
    )

    # Itens do pedido
    conn.execute(
        insert(line_items),
        [
            {'order_id': 1, 'cookie_id': 1, 'quantity': 5, 'extended_cost': 7.50},
            {'order_id': 1, 'cookie_id': 2, 'quantity': 3, 'extended_cost': 3.00},
            {'order_id': 2, 'cookie_id': 1, 'quantity': 10, 'extended_cost': 15.00}
        ]
    )

    conn.commit()

# 6️⃣ Consulta e exibição dos dados
with engine.connect() as conn:
    print("\n=== USERS ===")
    for row in conn.execute(select(users)):
        print(row)

    print("\n=== COOKIES ===")
    for row in conn.execute(select(cookies)):
        print(row)

    print("\n=== ORDERS ===")
    for row in conn.execute(select(orders)):
        print(row)

    print("\n=== LINE ITEMS ===")
    for row in conn.execute(select(line_items)):
        print(row)
