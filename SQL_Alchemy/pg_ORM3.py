from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Numeric, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"User(username='{self.username}', email_address='{self.email_address}', phone='{self.phone}', password='{self.password}')"


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self):
        return f"Cookie(cookie_name='{self.cookie_name}', cookie_recipe_url='{self.cookie_recipe_url}', cookie_sku='{self.cookie_sku}', quantity={self.quantity}, unit_cost={self.unit_cost})"


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))

    user = relationship("User", backref=backref('orders', order_by="Order.order_id"))

    def __repr__(self):
        return f"Order(user_id={self.user_id})"


class LineItems(Base):
    __tablename__ = 'line_items'

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    order = relationship("Order", backref=backref('line_items', order_by="LineItems.line_item_id"))
    cookie = relationship("Cookie", uselist=False, order_by="Cookie.cookie_id")

    def __repr__(self):
        return f"LineItems(order_id={self.order_id}, cookie_id={self.cookie_id}, quantity={self.quantity}, extended_cost={self.extended_cost})"


engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

from random import randint, uniform, choice
users = [
    User(username='alice', email_address='alice@example.com', phone='(11) 99999-1111', password='1234'),
    User(username='bob', email_address='bob@example.com', phone='(11) 99999-2222', password='abcd'),
    User(username='carol', email_address='carol@example.com', phone='(11) 99999-3333', password='xyz')
]
session.add_all(users)
session.commit()

cookies = []
for i in range(1, 11):
    cookies.append(
        Cookie(
            cookie_name=f'Cookie {i}',
            cookie_recipe_url=f'https://example.com/cookie{i}',
            cookie_sku=f'SKU{i:03d}',
            quantity=randint(10, 100),
            unit_cost=round(uniform(1.5, 5.0), 2)
        )
    )
session.add_all(cookies)
session.commit()


orders = []
for i in range(1, 11):
    user = choice(users)
    orders.append(Order(user_id=user.user_id))
session.add_all(orders)
session.commit()


line_items = []
for i in range(1, 11):
    order = choice(orders)
    cookie = choice(cookies)
    quantity = randint(1, 5)
    extended_cost = quantity * float(cookie.unit_cost)
    line_items.append(
        LineItems(order_id=order.order_id, cookie_id=cookie.cookie_id, quantity=quantity, extended_cost=extended_cost)
    )
session.add_all(line_items)
session.commit()

'''


for u in session.query(User).all():
    print(u)
for c in session.query(Cookie).limit(5):
    print(c)
for o in session.query(Order).limit(5):
    print(o)
for l in session.query(LineItems).limit(5):
    print(l)

############################################################    
from sqlalchemy import desc
# Ordena por nome (ascendente)
for user in session.query(User).order_by(User.username):
    print(user.username)

# Ordena por data de criação (descendente)
for user in session.query(User).order_by(desc(User.created_on)):
    print(f"{user.username} criado em {user.created_on}")

############################################################
# Retorna apenas 3 cookies
for cookie in session.query(Cookie).limit(3):
    print(cookie.cookie_name, cookie.unit_cost)

############################################################
# Filtra usuários com nome 'alice'
user = session.query(User).filter(User.username == 'alice').first()
print("Usuário encontrado:", user)

# Filtra cookies com custo maior que 3.00
for cookie in session.query(Cookie).filter(Cookie.unit_cost > 3.00):
    print(cookie.cookie_name, cookie.unit_cost)

############################################################
from sqlalchemy import and_, or_, not_

# AND → ambos precisam ser verdadeiros
for cookie in session.query(Cookie).filter(and_(Cookie.unit_cost > 2, Cookie.quantity < 50)):
    print("Cookie caro e em pouca quantidade:", cookie.cookie_name)

# OR → basta uma condição ser verdadeira
for cookie in session.query(Cookie).filter(or_(Cookie.cookie_name.like('%2%'), Cookie.cookie_name.like('%5%'))):
    print("Cookie nome contém 2 ou 5:", cookie.cookie_name)

# NOT → negação
for cookie in session.query(Cookie).filter(not_(Cookie.cookie_name.like('%1%'))):
    print("Cookie que NÃO contém 1:", cookie.cookie_name)

############################################################
# UPDATE

user = session.query(User).filter_by(username='alice').first()

if user:
    user.phone = "99999-0000"  # nova informação
    user.updated_on = datetime.now()

    session.commit()  # confirma a alteração no banco
else:
    print("Usuário 'alice' não encontrado.")

#### 
session.query(Cookie).filter(Cookie.unit_cost < 2.00).update({Cookie.unit_cost: 2.00})
session.commit()
############################################################
# DELETE

cookie_to_delete = session.query(Cookie).first()
session.delete(cookie_to_delete)
session.commit()

session.close()

'''