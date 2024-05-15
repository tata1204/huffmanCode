# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

import sys
sys.path.append("src")

from datetime import date

#Importar los módulos de la tabla Usuarios.
from model.Usuarios import Usuario
from controller.ControladorUsuarios import ControladorUsuarios

#Importar los módulos de la tabla Historial.
from model.Historial import Historial
from controller.ControladorHistorial import ControladorHistorial

class ControllerTest(unittest.TestCase):

    def setUpClass():
        # Llamar a la clase Controlador para que cree las tablas

        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()

        ControladorHistorial.EliminarTabla()
        ControladorHistorial.CrearTabla()


    #Test de la tabla de usuarios.

    def testInsertaryBuscar1( self ):
        """ Prueba que se inserto y se busco un registro correctamente en la tabla. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Prueba", apellido="Unitaria", id="1112", correo='no@tiene.com',
                                 user = "usuario", contraseña="contraseña" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario_buscado = ControladorUsuarios.BuscarUsuario( "usuario", "1112", "contraseña" )

        # Verificar Si lo trajo correctamente
        self.assertEqual(  usuario_prueba.apellido, usuario_buscado.apellido )



    def testInsertaryBuscar2( self ):
        """ Prueba que se inserto y se busco un registro correctamente en la tabla. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Otra", apellido="Prueba", id="114141", correo='nuna@tiene.com',
                                 user = "usuario2", contraseña="asfhkaj" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario_buscado = ControladorUsuarios.BuscarUsuario( "usuario2", "114141" , "asfhkaj" )

        # Verificar Si lo trajo correctamente
        self.assertEqual(  usuario_prueba.apellido, usuario_buscado.apellido )


    def testBuscarUserContraseña( self ):
        """ Prueba que se  busco un registro correctamente en la tabla usando unicamente el usuario y la contraseña. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Usur", apellido="Nuevo", id="7410", correo='usuario@contras.com',
                                 user = "prueba", contraseña="bucar" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario_buscado = ControladorUsuarios.UsuarioContraseña( "prueba" , "bucar" )

        # Verificar Si lo trajo correctamente
        self.assertEqual(  usuario_prueba.apellido, usuario_buscado.apellido )


    def testErrorBuscarUserContraseña( self ):
        """ Prueba que se dispara un error al buscar un registro  con el usuario incorrecto en la tabla. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Usur", apellido="Nuevo", id="7415", correo='usuario@contras.com',
                                 user = "prueba2", contraseña="bucar" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario = "Usur"
        contraseña = "bucar"

        # Verificar Si lo trajo correctamente
        self.assertRaises( Exception, ControladorUsuarios.UsuarioContraseña, usuario, contraseña)


    def testErrorBuscarUserContraseña2( self ):
        """ Prueba que se dispara un error al buscar un registro  con la contraseña incorrecta en la tabla. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Usur", apellido="Nuevo", id="741225", correo='usuario@contras.com',
                                 user = "prueba3", contraseña="bucar" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario = "prueba"
        contraseña = "Nuevo"

        # Verificar Si disparo el error correctamente
        self.assertRaises( Exception, ControladorUsuarios.UsuarioContraseña, usuario, contraseña)


    def testBuscarContraseña( self ):
        """ Prueba que se dispara un errar al buscar un registro  con la contraseña incorrecta en la tabla. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Hola", apellido="Mundo", id="01225", correo='hola@mundo.com',
                                 user = "contraseña", contraseña="buscar" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        #Buscar usuario
        usuario_buscado = ControladorUsuarios.BuscarContraseñaUsuario( "contraseña" , "01225" )

        # Verificar Si lo trajo correctamente
        self.assertEqual(  usuario_prueba.contraseña, usuario_buscado.contraseña )


    def testErrorBuscarContraseña( self ):
        """ Prueba que se dispara un error al buscar un registro  con la id incorrecta en la tabla. """

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Usuario4", apellido="Prueba4", id="00000", correo='usuario4@prueba.com',
                                 user = "prueba4", contraseña="contra4" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Buscar al usuario
        usuario = "prueba"
        id = "00000"

        # Verificar Si disparo el error correctamente
        self.assertRaises( Exception, ControladorUsuarios.BuscarContraseñaUsuario, usuario, id)


    def testClavePrimaria( self ):
        """Prueba que no se puede insertar dos veces una personas con el mismo usuario, ya que este es la clave primaria"""

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Clave", apellido="Primaria", id="11110", correo='testclave@prim.com',
                                 user = "primary", contraseña="key" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        # Insertar un Usuario en la tabla
        usuario_otro = Usuario( nombre="Francisco", apellido="Perez", id="111100000", correo='nuna@tiene.com',
                                 user = "primary", contraseña="asfhkaj" )
        
        #Verificar que salta la excepción
        self.assertRaises( Exception, ControladorUsuarios.InsertarUsuario, usuario_otro)


    def testBorrarUsuario( self ):
        """Prueba para verificar que se elimino correctamente un usuario"""
        
        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Borrar", apellido="Usuario", id="9999", correo='no@hay.com',
                                 user = "usuarioBorrar", contraseña="contra" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        #ELiminar Usuario de la tabla
        ControladorUsuarios.EliminarUsuario( '9999', 'usuarioBorrar', 'contra' )

        #Verificar que si salta la excepción al buscar un usuario eliminado
        self.assertRaises( Exception, ControladorUsuarios.EliminarUsuario, usuario_prueba)


    def testBorrarUsuario2( self ):
        """Prueba para verificar que se elimino correctamente un usuario"""
        
        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Borrar2", apellido="Usuario2", id="99922", correo='no@hay.user',
                                 user = "usuario2Borrar", contraseña="contra" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        #ELiminar Usuario de la tabla
        ControladorUsuarios.EliminarUsuario( '99922', 'usuario2Borrar', 'contra' )

        #Verificar que si salta la excepción al buscar un usuario eliminado
        self.assertRaises( Exception, ControladorUsuarios.EliminarUsuario, usuario_prueba)


    #Tests para verificar la correcta ejecución del cambio de correo.

    def testCambioCorreo( self ):
        #Test para verificar el correcto cambio de correo.

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Cambiar", apellido="Correo", id="44", correo='prueba@cambio.correo',
                                 user = "cambio", contraseña="correo" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )
        correoNuevo = 'correo.cambiado@correctamente'
        #Cambiar la contraseña
        ControladorUsuarios.CambiarCorreo( '44', 'cambio', 'correo', correoNuevo )

        #Buscar usuario
        usuario_buscado = ControladorUsuarios.BuscarUsuario( "cambio", "44", "correo" )

        #Verifica el cambio de correo
        self.assertEqual(usuario_buscado.correo, correoNuevo)


    def testCambioCorreo2( self ) :
        # Test para verificar las excepciones en el cambio de correo.

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario(nombre="Cambiar2", apellido="Correo2", id="456", correo='prueba2@cambio.correo',
                                user="cambio2", contraseña="contraseña2")
        ControladorUsuarios.InsertarUsuario(usuario_prueba)
        
        correoNuevo = 'nuevo.correo@prueba.com'
        
        # Verificar que se lance una excepción ValueError al intentar cambiar la contraseña con credenciales incorrectas
        with self.assertRaises(ValueError):
            ControladorUsuarios.CambiarCorreo('98765', 'cambio2', 'contraseña2', correoNuevo)



    def testCambioContraseña( self ):
        #Test para verificar el correcto cambio de contraseña.

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario( nombre="Cambiar", apellido="Contraseña", id="98765", correo='prueba@cambio.com',
                                 user = "cambio3", contraseña="contraseña" )
        ControladorUsuarios.InsertarUsuario( usuario_prueba )

        contraseñaNueva = 'nuevaContraseña'

        #Cambiar la contraseña
        ControladorUsuarios.CambiarContraseña( '98765', 'cambio3', 'contraseña', contraseñaNueva )

        #Busca el usuario
        usuario_buscado = ControladorUsuarios.BuscarContraseñaUsuario( "cambio3", "98765" )

        #Verifica el cambio de contraseña
        self.assertEqual(usuario_buscado.contraseña, contraseñaNueva)


    def testCambioContraseña2( self ) :
        # Test para verificar las excepciones en el cambio de contraseña.

        # Insertar un Usuario en la tabla
        usuario_prueba = Usuario(nombre="Cambiar2", apellido="Contraseña2", id="6363", correo='prueba2@cambio.com',
                                user="cambio4", contraseña="contraseña")
        ControladorUsuarios.InsertarUsuario(usuario_prueba)
        
        contraseñaNueva = 'nuevaContraseña'
        
        # Verificar que se lance una excepción ValueError al intentar cambiar la contraseña con credenciales incorrectas
        with self.assertRaises(ValueError):
            ControladorUsuarios.CambiarContraseña('98765', 'cambio2', 'contraseña_incorrecta', contraseñaNueva)


    #Test de la tabla de Historial

    def testInsertarHistorial ( self ):
        """Prueba que se inserta correctamente un proceso Huffman en el historial"""
        codificacion_prueba = Historial(user = "usuario2", code_decode = 'codificación', frase = 'Hola Mundo',
                                         diccionario = {'l': '000', 'H': '001', ' ': '010', 'a': '011', 'o': '10', 'u': '1100', 'm': '1101', 'd': '1110', 'n': '1111'},
                                         huffman = '00110000011010110111001111111010')
        
        ControladorHistorial.InsertarHuffman(codificacion_prueba)


    def testInsertarHistorial2 ( self ):
        """Prueba que se inserta correctamente un proceso Huffman en el historial"""
        codificacion_prueba = Historial(user = "usuario2", code_decode = 'codificación', frase = 'probando el insertar datos en el historial',
                                         diccionario = {'a': '000', 'o': '001', 'r': '010', 'd': '0110', 'p': '01110', 'h': '011110', 'b': '011111', 'i': '1000', 'l': '1001', 't': '1010', 's': '1011', ' ': '110', 'n': '1110', 'e': '1111'},
                                         huffman = '01110010001011111000111001100011101111100111010001110101111110101010000010110011000010100011011110111111101101111100111001111010001011101000101010000001001')
        
        ControladorHistorial.InsertarHuffman(codificacion_prueba)


    def testErrorInsertarHistorial (self):
        """Prueba que se lance una excepción al ingresar un diccionario incorrecto"""
        codificacion_prueba = Historial(user = "usuario2", code_decode = 'codificación', frase = 'probando error al insertar datos en el historial',
                                         diccionario = "{'d': '0000', 'p': '00010', 'h': '000110', 'b': '000111', 'a': '001', 'o': '010', 'i': '0110', 'l': '0111', 't': '1000', 's': '1001', 'n': '1010', 'e': '1011', ' ': '110', 'r': '111'}",
                                         huffman = '00010111010000111001101000000101101011111111010111110001011111001101010100110111111000001111110000000110000101001110101110101101011011111000011001101001100001011101100010111')
        
        with self.assertRaises(Exception) as context:
            ControladorHistorial.InsertarHuffman(codificacion_prueba)
        # Verificar el mensaje de la excepción
        self.assertIn("No fue posible insertar al historial", str(context.exception))


    def testBuscarHistorial ( self ):
        """Prueba para la correcta busqueda del historial"""
        codificacion_prueba = Historial(user = "usuario2", code_decode = 'codificación', frase = 'esta es una prueba',
                                         diccionario = {'e': '00', 'b': '0100', 'r': '0101', 'u': '011', 's': '100', 't': '1010', 'p': '10110', 'n': '10111', ' ': '110', 'a': '111'},
                                         huffman = '0010010101111100010011001110111111110101100101011000100111')
        ControladorHistorial.InsertarHuffman(codificacion_prueba)

        ControladorHistorial.BuscarHistorial('usuario2')


if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()