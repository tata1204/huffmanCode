import sys

sys.path.append("src")

from datetime import date

from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

def cambiarCorreo():
    try:
        usuario = input("Ingrese el usuario:")
        id = input("Ingrese el Id del usuario:")
        contraseña = input("Ingrese la contraseña del usuario:")
        correoNuevo = input("Ingrese el correo nuevo que desea poner:")

        ControladorUsuarios.CambiarCorreo(id,usuario,contraseña, correoNuevo)
        print("Correo modificado correctamente")

    except ValueError as e:
        print("Error:", e)