from backend.controller.usuario_controller import UsuarioController
from backend.model.usuario import Base
from backend import *
from backend.model.usuario import Usuario



def main():

  try:

    engine = sa.create_engine(f'mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}')
    
    conn = engine.connect()
    print("Conexão bem-sucedida!")
    conn.close()
  except Exception as e:
      print("Erro ao conectar:", e)
      
  try:
    Base.metadata.create_all(bind=engine)
    print('Tabelas criadas com sucesso')

  except Exception as e:
      print('Erro ao criar tabelas:',e)
      return


  
  controller = UsuarioController()
    # Adicionando um novo usuário
  controller.add_usuario('João Silva', 'joao.silva@example.com')

    # Listando todos os usuários
  usuarios = controller.get_usuarios()
  for usuario in usuarios:
      print(usuario.nome, usuario.email)

if __name__ == '__main__':
    main()
