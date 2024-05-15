# main.py

import sys
import json

sys.path.append("src")  # Agrega el directorio "src" al path para importar el módulo personalizado

# Importar las funciones de codificación y decodificación desde el módulo huffman
from model.huffmanCode.huffman import encode_message, decode_message

import usuario_contraseña
import crear_usuario
import buscar_contraseña
import cambiar_contraseña
import insertar_huffman
import cambiar_correo
import borrar_usuario

def main_menu():
    while True:
        print("Bienvenido al compresor y descompresor de mensajes!")
        print("Elija la opción:")
        print("1. Ingresar")
        print("2. Crear usuario")
        print("3. Olvide mi contraseña")
        print("4. Cambiar contraseña")
        print("5. Apagar compresor")

        opcion = input("Ingrese el número de su opción: ")

        if opcion == "1":
            if not user_menu():
                continue  # Si no se encontró el usuario, vuelve al menú principal
        elif opcion == "2":
            crear_usuario.crearUsuario()
        elif opcion == "3":
            buscar_contraseña.buscarContraseña()
        elif opcion == "4":
            cambiar_contraseña.cambiarContraseña()
        elif opcion == "5":
            print("Apagando el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

def user_menu():
    user = input("Ingrese el usuario: ")
    if not usuario_contraseña.ingresarUsuario(user):
        return False  # Indica que no se encontró el usuario y se debe volver al menú principal

    encoding_dict = None  # Inicializa el diccionario de codificación

    while True:
        print("Seleccione una opción:")
        print("1. Comprimir un mensaje")
        print("2. Descomprimir un mensaje comprimido")
        print("3. Ver historial")
        print("4. Modificar usuario")
        print("5. Salir")

        opcion = input("Ingrese el número de su opción: ")

        if opcion == '1':
            message = input("Ingrese el mensaje: ")
            encoded_message, encoding_dict = encode_message(message)
            print("Mensaje codificado:", encoded_message)
            print("Diccionario de codificación:", encoding_dict)
            insertar_huffman.insertarHuffman(user, "Codificar", message, encoding_dict, encoded_message)

        elif opcion == '2':
            mensaje_comprimido = input("Ingrese el mensaje comprimido a descomprimir: ")
            tree_dict_input = input("Ingrese el diccionario de codificación como un JSON: ")
            try:
                tree_dict = json.loads(tree_dict_input.replace("'", "\""))
            except json.JSONDecodeError:
                print("El formato del diccionario de codificación es inválido.")
                continue
            mensaje_descomprimido = decode_message(mensaje_comprimido, tree_dict)
            print(f"Mensaje descomprimido: {mensaje_descomprimido}")

            insertar_huffman.insertarHuffman(user, "Decodificar", mensaje_descomprimido, tree_dict, mensaje_comprimido)

        elif opcion == '3':
            resultados = insertar_huffman.mostrarHistorial(user)

            print("Historial: \n")

            if resultados:
                for resultado in resultados:
                    print(f"Usuario: {resultado[0]}")
                    print(f"Code/Decode: {resultado[1]}")
                    print(f"Frase: {resultado[2]}")
                    print(f"Diccionario: {resultado[3]}")
                    print(f"Huffman: {resultado[4]}\n")
            else:
                print("No se encontraron coincidencias para el usuario.")

        elif opcion == '4':
            while True:
                print("1. Cambiar correo")
                print("2. Borrar usuario")
                print("3. Salir")
                sub_opcion = input("Ingrese el número de su opción: ")

                if sub_opcion == '1':
                    cambiar_correo.cambiarCorreo()
                elif sub_opcion == '2':
                    borrar_usuario.borrarUsuario()
                    insertar_huffman.borrarHistorial(user)
                    print("Usuario borrado. Regresando al menú principal.")
                    return True  # Sale de user_menu y regresa al menú principal
                elif sub_opcion == '3':
                    break
                else:
                    print("Opción inválida. Por favor, intente nuevamente.")

        elif opcion == '5':
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
    return True  # Indica que el usuario fue encontrado y se queda en user_menu

# Inicia el programa desde el menú principal
main_menu()

