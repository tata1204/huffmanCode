# usuario_contraseña.py

import sys
sys.path.append("src")

from datetime import date
from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

def ingresarUsuario(user):
    try:
        usuario = user
        contraseña = input("Ingrese la contraseña: ")

        usuario_buscado = ControladorUsuarios.UsuarioContraseña(usuario, contraseña)
        
        print("Bienvenido " + usuario_buscado.nombre + ' ' + usuario_buscado.apellido)
        return True

    except ValueError as e:
        print("Error:", e)
        return False
