import sys

sys.path.append("src")

from datetime import date

from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

def buscarContraseña():
    try:
        usuario = input ("Ingrese el usuario a consultar:")
        id = input ("Ingrese el Id del usuario a consultar:")

        usuario_buscado = ControladorUsuarios.BuscarContraseñaUsuario(usuario, id)
        
        print ( usuario_buscado.nombre + " " + usuario_buscado.apellido + ", su contraseña es: " + usuario_buscado.contraseña)

    except ValueError as e:
        print("Error:", e)