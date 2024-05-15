import sys

sys.path.append("src")

from datetime import date

from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios


def borrarUsuario():
    print("Ingrese datos para eliminar el usuario :")

    try:
        id = input ("Ingrese el Id del usuario a eliminar:")
        usuario = input ("Ingrese el usuario a eliminar:")
        contraseña = input ("Ingrese la contraseña del usuario a eliminar:")

        ControladorUsuarios.EliminarUsuario( id, usuario, contraseña )

        print("Usuario eliminado correctamente")
        
    except ValueError as e:
        print("Error:", e)

