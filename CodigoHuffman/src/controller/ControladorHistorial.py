import sys
import json
sys.path.append( "." )
sys.path.append( "src" )

import psycopg2

from model.Historial import Historial
import SecretConfig

from controller.ControladorUsuarios import ControladorUsuarios

class ControladorHistorial:

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorHistorial.ObtenerCursor()

        cursor.execute("""create table historial (
  usuario text not null,
  code_decode text not null,
  frase text not null,
  diccionario json  not null,
  huffman text not null
);  """)
        cursor.connection.commit()



    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorHistorial.ObtenerCursor()

        cursor.execute("""drop table historial""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarHuffman( historial : Historial ):
        """ Recibe un a instancia de la clase Historial y la inserta en la tabla respectiva"""

        try:
            cursor = ControladorHistorial.ObtenerCursor()

            diccionario_json = json.dumps(historial.diccionario)
            
            # Convertir el diccionario a una cadena JSON válida con ensure_ascii=False
            cadena_json_con_escape = json.dumps(diccionario_json, ensure_ascii=False)

            # Escapar manualmente las comillas dobles dentro de la cadena JSON
            #cadena_json_con_escape = cadena_json_con_escape.replace('"', '\\"')

            cursor.execute( f"""insert into historial (usuario, code_decode, frase, diccionario, huffman) 
                            values ('{historial.user}', '{historial.code_decode}', '{historial.frase}', 
                                '{diccionario_json}',  '{historial.huffman}')""" )
            cursor.connection.commit()

        except:
            cursor.connection.rollback()
            raise Exception ("No fue posible insertar al historial : " + historial.user)

    def BuscarHistorial (usuario) :
        """Recibe un usuario y si este existe, le muestra su historial."""
        cursor = ControladorUsuarios.ObtenerCursor()
        
        cursor.execute(f"""select usuario,code_decode, frase, diccionario, huffman
            from historial where usuario = '{usuario}' """ )  

        resultados = cursor.fetchall()

        return resultados      

    def BorrarHistorial(usuario):
        """Recibe un usuario y borra el historial de este."""

        cursor = ControladorUsuarios.ObtenerCursor()
        
        cursor.execute(f"""DELETE 
            from historial where usuario = '{usuario}' """ )  
        

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor