import sys
sys.path.append( "." )
sys.path.append( "src" )


import psycopg2

from model.Usuarios import Usuario
import SecretConfig

class ControladorUsuarios :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""create table usuarios (
  nombre text not null,
  apellido text not null,
  id text NOT NULL,
  correo text not null,
  usuario text PRIMARY KEY not null,
  contraseña text not null
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarUsuario( usuario : Usuario ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""

        try:
            cursor = ControladorUsuarios.ObtenerCursor()
            cursor.execute( f"""insert into usuarios (nombre, apellido, id, correo, usuario, contraseña) 
                            values ('{usuario.nombre}', '{usuario.apellido}', '{usuario.id}', 
                                '{usuario.correo}',  '{usuario.user}', '{usuario.contraseña}')""" )
            cursor.connection.commit()

        except:
            cursor.connection.rollback()
            raise Exception ("No fue posible insertar el usuario : " + usuario.id)

    def BuscarContraseñaUsuario( usuario, id):
        """ Trae un usuario de la tabla de usuarios por el usuario y la ID """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""select nombre, apellido, id, correo, usuario, contraseña
        from usuarios where usuario = '{usuario}' and id = '{id}'""" )

        try:
            fila = cursor.fetchone()
            resultado = Usuario(nombre=fila[0], apellido=fila[1], id=fila[2], correo=fila[3],
                            user=fila[4], contraseña=fila[5])
            return resultado
        except TypeError:
            raise ValueError("No se encontró ningún usuario con el ID y usuario especificados.")


    def BuscarUsuario(usuario, id, contraseña):
        """ Trae un usuario de la tabla de usuarios por el usuario, el ID y la contraseña """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""select nombre, apellido, id, correo, usuario, contraseña
        from usuarios where usuario = '{usuario}' and id = '{id}' and contraseña = '{contraseña}'""" )

        try:
            fila = cursor.fetchone()
            resultado = Usuario(nombre=fila[0], apellido=fila[1], id=fila[2], correo=fila[3],
                            user=fila[4], contraseña=fila[5])
            return resultado
        except TypeError:
            raise ValueError("Usuario, ID o contraseña incorrecta.")


    def BuscarPorUsuario(usuario):
        """Busca si el usuario existe."""
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""select nombre, apellido, id, correo, usuario, contraseña
        from usuarios where usuario = '{usuario}' """ )

        try:
            fila = cursor.fetchone()
            resultado = Usuario(nombre=fila[0], apellido=fila[1], id=fila[2], correo=fila[3],
                            user=fila[4], contraseña=fila[5])
            return resultado
        except TypeError:
            raise ValueError("Usuario no encontrado.")

    def UsuarioContraseña(usuario,contraseña):
        """Verifica el usuario y contraseña"""
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""select nombre, apellido, id, correo, usuario, contraseña
        from usuarios where usuario = '{usuario}'  and contraseña = '{contraseña}'""" )

        try:
            fila = cursor.fetchone()
            resultado = Usuario(nombre=fila[0], apellido=fila[1], id=fila[2], correo=fila[3],
                            user=fila[4], contraseña=fila[5])
            return resultado
        except TypeError:
            raise ValueError("Usuario o contraseña incorrecta.")
    

    def CambiarContraseña(id, usuario, contraseñaVieja, contraseñaNueva):
        """Cambia la contraseña de un usuario creado anteriormente."""

        cursor = ControladorUsuarios.ObtenerCursor()
        
        
        usuario_buscado = ControladorUsuarios.BuscarUsuario(usuario, id, contraseñaVieja)
        cursor.execute(f"""UPDATE usuarios
                    SET contraseña = '{contraseñaNueva}'
                    WHERE usuario = '{usuario}' AND id = '{id}' AND contraseña = '{contraseñaVieja}'""")
            
        cursor.connection.commit()


    def CambiarCorreo ( id, usuario, contraseña, correoNuevo):
        """Cambia el correo del usuario."""
        cursor = ControladorUsuarios.ObtenerCursor()

        usuario_buscado = ControladorUsuarios.BuscarUsuario(usuario, id, contraseña)

        cursor.execute(f"""UPDATE usuarios
                    SET correo = '{correoNuevo}'
                    WHERE usuario = '{usuario}' AND id = '{id}' AND contraseña = '{contraseña}'""")
        
        cursor.connection.commit()

    def EliminarUsuario( id, usuario, contraseña ):
        """Elimina un usuario creado anteriormente."""

        cursor = ControladorUsuarios.ObtenerCursor()

        usuario_buscado = ControladorUsuarios.BuscarUsuario(usuario, id, contraseña)

        cursor.execute(f"""DELETE 
                        FROM usuarios 
                        WHERE usuario = '{usuario}' AND id = '{id}' AND contraseña = '{contraseña}'""")
        
        cursor.connection.commit()

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor