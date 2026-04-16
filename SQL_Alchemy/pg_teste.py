from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes")

with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))
    print(result.fetchone())
