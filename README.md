# APLICACIÓN DE CODIFICACIÓN Y DECODIFICACIÓN HUFFMAN 

Esta es una aplicación desarrollada en Python utilizando el framework Kivy, que permite codificar y decodificar mensajes utilizando el algoritmo de compresión Huffman. Además cuenta con una base de datos en NeonDB. 


## ¿Quién hizo esto?

Mayezly Tatiana Gafaro Boada

## ¿Qué es y para qué es?

Este proyecto es una aplicación de codificación y decodificación utilizando el algoritmo de compresión Huffman. Permite comprimir mensajes de texto utilizando el algoritmo de Huffman para generar una secuencia de bits más corta y eficiente. Además, puede decodificar mensajes codificados previamente utilizando el mismo algoritmo.


## ¿Cómo funciona el algoritmo de compresion Huffman?

El algoritmo de compresión Huffman es un método que asigna códigos de longitud variable a cada carácter en un mensaje, basándose en su frecuencia de aparición. Los caracteres más comunes reciben códigos más cortos, mientras que los menos comunes reciben códigos más largos. Esto resulta en una representación más eficiente del mensaje, ya que se utilizan menos bits para los caracteres más frecuentes.


## Prerrequisitos

- Python 3.x instalado en tu sistema. 
- La biblioteca Kivy, esta se puede instalar ejecutando pip install kivy.

## ¿Cómo está hecho?

Este proyecto está implementado en Python y utiliza el framework Kivy para la interfaz de usuario. La arquitectura del proyecto está organizada de la siguiente manera:

- Carpeta 'huffmanCode': Contiene un archivo .py en donde se encuentra el código fuente de la lógica de la aplicación.
    - huffman.py: Contiene la lógica para codificar y decodificar mensajes utilizando el algoritmo de Huffman.

- Carpeta 'interfazHuffman': Contiene un archivo .py en donde se encuentra la interfaz de usuario.
    - interfaz.py: Contiene el código implementado con la biblioteca Kivy para la elaboración de la interfaz gráfica de la aplicación.
 
- Carpeta 'consoleHuffman': Contiene un archivo .py en donde se encuentra la interfaz por consola.
    - console.py: Contiene el código implementado con la lógica Huffmans en la interfaz por consola.

- Carpeta 'tests': Contiene pruebas unitarias para la lógica de la aplicación.
    - test_huffman.py: Pruebas unitarias para las funciones de codificación y decodificación de Huffman.


## Uso

Para poder hacer uso debe conectar a su base de datos en NeonDB, incluyendo los datos de conexión en SecretConfig-sample.py y renombrando el archivo como SecretConfig.py

- Uso del código fuente Huffman por consola: Para hacer uso de la aplicación por consola se debe correr el archivo console.py que se encuentra en la carpeta 'consoleHuffman'.
    - Para ejecutarlo por la terminal se debe especificar la ruta de busqueda donde se encuentran los módulos, además de:
      python huffmanCode\src\view-console\console.py 

- Uso del Kivy: Para hacer uso de la aplicación con interfaz gráfica se debe correr el archivo interfaz.py que se encuentra en la carpeta 'interfazHuffman'.
    - Para ejecutarlo por la terminal se debe especificar la ruta de busqueda donde se encuentran los módulos, además de:
      python huffmanCode\src\view-gui\huffman_gui.py 
  
