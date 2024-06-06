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
      
  try:
    Base.metadata.create_all(bind=engine)
    print('Tabelas criadas com sucesso')

  except Exception as e:
      print('Erro ao criar tabelas:',e)
      return


  
  controller = UsuarioController()
    # Adicionando um novo usuário
  
  while True:
    print('Escolha uma opção')
    print("1 - Inserir usuário")
    print("2 - Excluir usuário")
    print("3 - Sair")

    opcao = input('Digite uma opção: ')

    if opcao == '1':
      user = input("Digite seu nome")
      email = input("Digite seu email")
      controller.add_usuario(user, email)
    
    elif opcao == '2':
      user = input('Digite o id do usuário que será deletado:')
      controller.delete_usuario(user)
      print('Usuário deletado com sucesso')

    elif opcao == '3':
      print('Saindo do programa')
      break
    else:
      print('Opção inválida. Por favor escolha uma opção válida')

    

  

    # Listando todos os usuários
  usuarios = controller.get_usuarios()
  for usuario in usuarios:
      print(usuario.nome, usuario.email)

if __name__ == '__main__':
    main()
