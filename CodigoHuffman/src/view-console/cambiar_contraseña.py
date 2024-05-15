import sys

sys.path.append("src")

from datetime import date

from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios


def cambiarContraseña():
    try:
        usuario = input("Ingrese el usuario:")
        id = input("Ingrese el Id del usuario:")
        contraseñaVieja = input("Ingrese la contraseña del usuario:")
        contraseñaNueva = input("Ingrese la contraseña nueva que desea poner:")

        ControladorUsuarios.CambiarContraseña(id,usuario,contraseñaVieja, contraseñaNueva)
        print("Contraseña modificada correctamente")

    except ValueError as e:
        print("Error:", e)
