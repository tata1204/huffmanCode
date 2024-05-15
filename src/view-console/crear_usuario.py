import sys

sys.path.append("src")

from datetime import date

from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

usuario = Usuario( nombre="", apellido="", id="", 
                    correo = "", user = "", contraseña="" )

def crearUsuario():
    print("Ingrese datos para crear el usuario:")
    usuario.nombre = input ("Nombre:")
    usuario.apellido = input ("Apellido:")
    usuario.id = input ("id:")
    usuario.correo = input ("Correo:")
    usuario.user = input ("Usuario:")
    usuario.contraseña = input ("Contraseña:")

    ControladorUsuarios.InsertarUsuario (usuario)

    print("Usuario insertado correctamente :)")