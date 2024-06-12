from backend.controller.usuario_controller import UsuarioController
from backend.model.usuario import Base
from backend import *
from backend.model.usuario import Usuario



def main():

  try:

    conn = engine.connect()
    print("Conexão bem-sucedida!")
    conn.close()
  except Exception as e:
      print("Erro ao conectar:", e)
      
  # try:
  #   Base.metadata.create_all(bind=engine)
  #   print('Tabelas criadas com sucesso')

  # except Exception as e:
  #     print('Erro ao criar tabelas:',e)
  #     return



if __name__ == '__main__':
    main()
