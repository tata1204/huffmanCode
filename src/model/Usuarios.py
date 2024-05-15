from datetime import date

class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la aplicación de Codificación con Huffman
    """
    def __init__( self,  nombre, apellido, id, correo, user, contraseña): 
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.correo = correo
        self.user = user
        self.contraseña = contraseña
        


    def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert( self.nombre == comparar_con.nombre )
        assert( self.apellido== comparar_con.apellido )
        assert( self.id== comparar_con.id )
        assert( self.correo == comparar_con.correo)
        assert( self.user== comparar_con.user )
        assert( self.contraseña== comparar_con.contraseña )