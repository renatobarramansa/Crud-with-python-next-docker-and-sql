
from backend.model.usuario import Usuario
from backend import *



class UsuarioController:
    def __init__(self):
        self.session = Session()

    def add_usuario(self, nome, email):
        novo_usuario = Usuario(nome=nome, email=email)
        print(novo_usuario)
        self.session.add(novo_usuario)
        self.session.commit()

    def get_usuarios(self):
        return self.session.query(Usuario).all()

    def delete_usuario(self, usuario_id):
        usuario = self.session.query(Usuario).filter_by(id=usuario_id).first()
        if usuario:
          self.session.delete(usuario)
          self.session.commit()
          print(f"Usuário com ID {usuario_id} foi deletado com sucesso.")
        else:
          print(f"Usuario {usuario_id} não encontrado.")
