import unittest
import pytest

import sys
sys.path.append("src")  # Agrega el directorio "src" al path para importar el módulo personalizado

# Importar las funciones de codificación y decodificación desde el módulo huffman
from model.huffmanCode.huffman import encode_message, decode_message

class TestHuffman(unittest.TestCase):

    # Casos de prueba para la compresión
    def test1(self):
        # Caso normal 1: Mensaje repetitivo
        input_data = "aaaabbbcc"
        expected_data = '00001111111010'
        result = encode_message(input_data)[0]  # Llamar a la función de compresión
        self.assertEqual(expected_data, result)

    def test2(self):
        # Caso normal 2: Mensaje variado
        input_data = "Hola mundo"
        expected_data = '000111001010011100101110111'
        result = encode_message(input_data)[0]  # Llamar a la función de compresión
        self.assertEqual(expected_data, result)

    def test3(self):
        # Caso normal 3: Números como mensaje
        input_data = "123"
        expected_data = '11011'  # Añadir comillas para representar un string
        result = encode_message(input_data)[0]  # Llamar a la función de compresión
        self.assertEqual(expected_data, result)

    def test7(self):
        # Caso extraordinario 1: Solo un carácter
        input_data = "a"
        expected_data = '1'  # Añadir comillas para representar un string
        result = encode_message(input_data)[0]  # Llamar a la función de compresión
        self.assertEqual(expected_data, result)

    def test8(self):
        # Caso extraordinario 2: Carácter especial
        input_data = "/"
        expected_data = ''  # Modificar el valor esperado
        result = encode_message(input_data)[0]  # Llamar a la función de compresión
        self.assertEqual(expected_data, result)

        with self.assertRaises(Exception):  # Forzar excepción
            encode_message(input_data)  

    # Casos de prueba para la descompresión
    def test4(self):
        # Caso normal 4: Mensaje repetitivo
        input_data = '00001111111010'
        expected_data = "aaaabbbcc"
        result = decode_message(input_data)  # Llamar a la función de descompresión
        self.assertEqual(expected_data, result)

    def test5(self):
        # Caso normal 5: Mensaje variado
        input_data = '000111001010011100101110111'
        expected_data = "Hola mundo"
        result = decode_message(input_data)  # Llamar a la función de descompresión
        self.assertEqual(expected_data, result)

    def test6(self):
        # Caso normal 6: Números como mensaje
        input_data = '11011'  # Añadir comillas para representar un string
        expected_data = "123"
        result = decode_message(input_data)  # Llamar a la función de descompresión
        self.assertEqual(expected_data, result)

    def test9(self):
        # Caso extraordinario 3: Solo un carácter
        input_data = '1'  # Añadir comillas para representar un string
        expected_data = "a"
        result = decode_message(input_data)  # Llamar a la función de descompresión
        self.assertEqual(expected_data, result)

    def test10(self):
        # Caso extraordinario 4: Carácter especial
        input_data = ""
        expected_data = "/"  # Modificar el valor esperado
        result = decode_message(input_data)  # Llamar a la función de descompresión
        self.assertEqual(expected_data, result)

        with self.assertRaises(Exception):  # Forzar excepción
            decode_message(input_data)  

    # Otros casos de prueba
    def test17(self):
        # Caso extraordinario 5: Mensaje muy grande para comprimir
        big_data = "a" * (10**9)
        with self.assertRaises(AssertionError):  # Forzar fallo si no se produce una excepción
            encode_message(big_data)

    def test18(self):
        # Caso extraordinario 6: Mensaje muy grande para descomprimir
        big_data = "a" * (10**1000)
        with self.assertRaises(AssertionError):  # Forzar fallo si no se produce una excepción
            decode_message(big_data)

    # Casos de errores esperados
    def test11(self):
        # Caso de error 1: Entrada no válida
        input_data = 12345  
        with self.assertRaises(TypeError):
            encode_message(input_data)

    def test12(self):
        # Caso de error 2: Caracteres no válidos
        input_data = "abcde^&*"
        with self.assertRaises(ValueError):
            encode_message(input_data)

    def test13(self):
        # Caso de error 3: Diccionario no vacío
        dictionary1 = {"a": 1}
        dictionary2 = {}
        self.assertNotEqual(dictionary1, dictionary2)

    def test14(self):
        # Caso de error 4: Dato descomprimido corrupto
        datos_corruptos = "esto no es un dato comprimido válido"
        with pytest.raises(ValueError):
            decode_message(datos_corruptos)

    def test15(self):
        # Caso de error 5: Entrada nula para compresión
        with pytest.raises(TypeError):
            encode_message(None)

    def test16(self):
        # Caso de error 6: Entrada nula para descompresión
        with pytest.raises(TypeError):
            decode_message(None)

    def test19(self):
        # Caso de error 7: Tipo de entrada incorrecta (lista)
        type_data_incorrect = [1, 2, 3]
        with self.assertRaises(TypeError):
            encode_message(type_data_incorrect)

    def test20(self):
        # Caso de error 8: Caracteres no ASCII
        data_no_ascii = "ñáéíóú"
        with self.assertRaises(ValueError):
            encode_message(data_no_ascii)


if __name__ == '__main__':
    unittest.main()


