from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///clientes.db")

with engine.connect() as conn:
    result = conn.execute(text("SELECT sqlite_version();"))
    print(result.fetchone())
