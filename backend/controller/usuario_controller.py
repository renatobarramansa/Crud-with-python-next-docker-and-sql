
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
