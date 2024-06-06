from sqlalchemy import Column, Integer, String, create_engine
from backend import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)

# Opcional: se você quiser criar as tabelas ao importar este módulo
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Base.metadata.create_all(engine)
