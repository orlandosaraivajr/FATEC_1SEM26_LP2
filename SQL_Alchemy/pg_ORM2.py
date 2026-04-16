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


'''
cc_cookie = Cookie(cookie_name='chocolate chip', cookie_recipe_url='http://some.aweso.me/cookie/recipe.html', cookie_sku='CC01', quantity=12, unit_cost=0.50)
session.add(cc_cookie)
session.commit()


dcc = Cookie(cookie_name='dark chocolate chip', cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html', cookie_sku='CC02', quantity=1, unit_cost=0.75)
mol = Cookie(cookie_name='molasses', cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html', cookie_sku='MOL01', quantity=1, unit_cost=0.80)
session.add(dcc)
session.add(mol)
session.flush()
print(dcc.cookie_id)
print(mol.cookie_id)

c1 = Cookie(cookie_name='peanut butter', cookie_recipe_url='http://some.aweso.me/cookie/peanut.html', cookie_sku='PB01', quantity=24, unit_cost=0.25)
c2 = Cookie(cookie_name='oatmeal raisin', cookie_recipe_url='http://some.okay.me/cookie/raisin.html', cookie_sku='EWW01', quantity=100, unit_cost=1.00)
session.bulk_save_objects([c1,c2])
session.commit()

'''