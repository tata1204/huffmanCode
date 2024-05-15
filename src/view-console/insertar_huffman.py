import sys

sys.path.append("src")

from datetime import date

from model.Historial import Historial
from controller.ControladorHistorial import ControladorHistorial

def insertarHuffman (usuario, code_decode, frase, diccionario, huffman):

    try:
        codificacion_prueba = Historial(user = usuario, code_decode = code_decode, frase = frase,
                                         diccionario = diccionario,
                                         huffman = huffman)
        
        ControladorHistorial.InsertarHuffman(codificacion_prueba)
    except ValueError as e:
        print("Error:", e)

def mostrarHistorial(usuario):
    try:
        resultados = ControladorHistorial.BuscarHistorial(usuario)
        return resultados
    except Exception as e:
        print(f"Ocurrió un error al buscar el historial: {e}")
        return []
    
def borrarHistorial(usuario):
    try:
        resultados = ControladorHistorial.BorrarHistorial(usuario)
    except Exception as e:
        print(f"Ocurrió un error al borrar el historial: {e}")
        return []