import sys

sys.path.append("src")

from datetime import date

from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios


try:
    usuario = input ("Ingrese el usuario a consultar:")
    id = input ("Ingrese el Id del usuario a consultar:")
    contraseña = input ("Ingrese la contraseña del usuario a buscar:")

    usuario_buscado = ControladorUsuarios.BuscarUsuario(id, usuario, contraseña)
    
    print ( usuario_buscado.nombre + " " + usuario_buscado.apellido)
    print ( "Correo: " + usuario_buscado.correo)

except ValueError as e:
    print("Error:", e)