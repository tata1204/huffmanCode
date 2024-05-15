from datetime import date

class Historial:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa al historial de la aplicación de Codificación con Huffman
    """

    def __init__( self, user, code_decode, frase, diccionario, huffman): 
        self.user = user
        self.code_decode = code_decode
        self.frase = frase
        self.diccionario = diccionario
        self.huffman = huffman


    def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """

        assert( self.user== comparar_con.user )
        assert( self.code_decode == comparar_con.code_decode )
        assert( self.frase== comparar_con.frase )
        assert( self.diccionario== comparar_con.diccionario )
        assert( self.huffman == comparar_con.huffman)

        