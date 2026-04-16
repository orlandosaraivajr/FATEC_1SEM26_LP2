from sqlalchemy import create_engine, MetaData

# Conexão com o PostgreSQL
engine = create_engine("postgresql+psycopg2://orlando:123mudar@localhost:5432/clientes")

# Cria um objeto MetaData para refletir as tabelas existentes
metadata = MetaData()

# Reflete todas as tabelas existentes no banco
metadata.reflect(bind=engine)

# Mostra as tabelas que foram encontradas
print("Tabelas encontradas no banco:", metadata.tables.keys())

# Ordem de exclusão: primeiro as tabelas que dependem de outras
tabelas_para_remover = ['line_items', 'orders', 'cookies', 'users']

with engine.connect() as conn:
    for tabela in tabelas_para_remover:
        if tabela in metadata.tables:
            print(f"Removendo tabela '{tabela}'...")
            metadata.tables[tabela].drop(engine)
            print(f"✅ Tabela '{tabela}' removida com sucesso.")
        else:
            print(f"⚠️ Tabela '{tabela}' não encontrada, pulando.")

print("🎯 Todas as tabelas foram removidas com sucesso (se existiam).")
