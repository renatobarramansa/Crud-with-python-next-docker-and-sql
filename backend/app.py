from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

# Configuração do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definição de um modelo de exemplo
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)

# Criação da tabela
Base.metadata.create_all(engine)

# Adicionando um novo usuário
novo_usuario = Usuario(nome='João Silva', email='joao.silva@example.com')
session.add(novo_usuario)
session.commit()

# Consultando usuários
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nome, usuario.email)
