from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import sys
import json
sys.path.append("src")  # Agrega el directorio "src" al path para importar el módulo personalizado

# Importar las funciones de codificación y decodificación desde el módulo huffman
from model.huffmanCode.huffman import encode_message, decode_message


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.username_input = TextInput(multiline=False)
        self.password_input = TextInput(multiline=False, password=True)

        layout = BoxLayout(orientation='vertical')
        
        # Inputs para usuario y contraseña
        layout.add_widget(Label(text='Usuario:'))
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)
        
        layout.add_widget(Label(text='Contraseña:'))
        self.password_input = TextInput(multiline=False, password=True)
        layout.add_widget(self.password_input)

        # Botones para iniciar sesión y crear nuevo usuario
        login_button = Button(text='Iniciar sesión', size_hint=(None, None), size=(150, 50))
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        new_user_button = Button(text='Crear nuevo usuario', size_hint=(None, None), size=(200, 50))
        new_user_button.bind(on_press=self.create_new_user)
        layout.add_widget(new_user_button)

        self.add_widget(layout)

    def login(self, instance):
        # Verifica las credenciales ingresadas y permite el acceso o muestra un mensaje de error
        # Aquí puedes agregar tu lógica de autenticación
        if self.username_input.text == "" and self.password_input.text == "":
            self.manager.current = 'main'
        else:
            popup = Popup(title='Error', content=Label(text='Credenciales incorrectas'), size_hint=(None, None), size=(200, 200))
            popup.open()

    def create_new_user(self, instance):
        # Aquí puedes agregar la lógica para crear un nuevo usuario
        pass

    def reset_fields(self):
        # Restablece los campos de entrada de texto a su estado inicial (vacío)
        self.username_input.text = ''
        self.password_input.text = ''

class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Aquí puedes cargar y mostrar el historial de decodificación
        # Por ejemplo, puedes leer de un archivo o una base de datos y mostrar los registros

        back_button = Button(text='Regresar', size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def switch_to_main_screen(self, instance):
        # Regresa a la pantalla principal
        self.manager.current = 'main'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Diseño de la pantalla principal
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        # Título
        title_label = Label(text='Seleccionar modo:', font_size=24, size_hint=(1, 0.5), pos_hint={'top': 0.9})
        layout.add_widget(title_label)

        # Botones para seleccionar modo de codificación o decodificación
        self.encode_button = Button(text='Codificar', size_hint=(1, None), size=(200, 100), font_size=20)
        self.encode_button.bind(on_press=self.switch_to_encode_screen)
        layout.add_widget(self.encode_button)

        self.decode_button = Button(text='Decodificar', size_hint=(1, None), size=(200, 100), font_size=20)
        self.decode_button.bind(on_press=self.switch_to_decode_screen)
        layout.add_widget(self.decode_button)

        # Botón para ir al historial
        history_button = Button(text='Ver Historial', size_hint=(1, None), size=(200, 100), font_size=20)
        history_button.bind(on_press=self.switch_to_history_screen)
        layout.add_widget(history_button)

        # Botón para volver a la pantalla de inicio de sesión
        logout_button = Button(text='Cerrar Sesión', size_hint=(1, None), size=(200, 100), font_size=20)
        logout_button.bind(on_press=self.switch_to_login_screen)
        layout.add_widget(logout_button)

        self.add_widget(layout)

    def switch_to_encode_screen(self, instance):
        # Cambia a la pantalla de codificación
        self.manager.current = 'encode'

    def switch_to_decode_screen(self, instance):
        # Cambia a la pantalla de decodificación
        self.manager.current = 'decode'

    def switch_to_history_screen(self, instance):
        # Cambia a la pantalla de historial
        self.manager.current = 'history'

    def switch_to_login_screen(self, instance):
        # Llama al método para restablecer los campos de entrada de texto en la pantalla de inicio de sesión
        self.manager.get_screen('login').reset_fields()
        # Cambia a la pantalla de inicio de sesión
        self.manager.current = 'login'

class EncodeScreen(Screen):
    def __init__(self, **kwargs):
        super(EncodeScreen, self).__init__(**kwargs)

        # Diseño de la pantalla de codificación
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Ingrese el mensaje:'))
        self.message_input = TextInput(multiline=False)
        layout.add_widget(self.message_input)
        encode_button = Button(text='Codificar Mensaje', size_hint=(None, None), size=(150, 50))
        encode_button.bind(on_press=self.encode_message)
        layout.add_widget(encode_button)
        layout.add_widget(Label(text='Secuencia Huffman del mensaje ingresado:'))
        self.encoded_output = TextInput(readonly=True)
        layout.add_widget(self.encoded_output)
        layout.add_widget(Label(text='Diccionario:'))
        self.dictionary_output = TextInput(readonly=True, multiline=True)
        layout.add_widget(self.dictionary_output)
        back_button = Button(text='Regresar', size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def encode_message(self, instance):
        # Codifica el mensaje ingresado
        message = self.message_input.text.strip()  
        encoded, dictionary = encode_message(message)
        self.encoded_output.text = encoded
        self.dictionary_output.text = dictionary

    def switch_to_main_screen(self, instance):
        # Regresa a la pantalla principal
        self.manager.current = 'main'


class DecodeScreen(Screen):
    def __init__(self, **kwargs):
        super(DecodeScreen, self).__init__(**kwargs)

        # Diseño de la pantalla de decodificación
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Ingrese el código:'))
        self.encoded_input = TextInput(multiline=False)
        layout.add_widget(self.encoded_input)
        layout.add_widget(Label(text='Ingrese el diccionario de codificación como un JSON:'))
        self.dictionary_input = TextInput(multiline=False)
        layout.add_widget(self.dictionary_input)
        decode_button = Button(text='Decodificar Mensaje', size_hint=(None, None), size=(150, 50))
        decode_button.bind(on_press=self.decode_message)
        layout.add_widget(decode_button)
        layout.add_widget(Label(text='Mensaje decodificado:'))
        self.decoded_output = TextInput(readonly=True)
        layout.add_widget(self.decoded_output)
        back_button = Button(text='Regresar', size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.switch_to_main_screen)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def decode_message(self, instance):
        # Decodifica el código ingresado
        encoded = self.encoded_input.text.strip()
        dictionary = self.dictionary_input.text.strip()
        try:
            tree_dict = json.loads(dictionary.replace("'", "\""))
        except json.JSONDecodeError:
            self.decoded_output.text = "El formato del diccionario de codificación es inválido."
            return
        decoded = decode_message(encoded, tree_dict)
        self.decoded_output.text = decoded

    def switch_to_main_screen(self, instance):
        # Regresa a la pantalla principal
        self.manager.current = 'main'




class HuffmanApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(EncodeScreen(name='encode'))
        sm.add_widget(DecodeScreen(name='decode'))
        sm.add_widget(HistoryScreen(name='history'))
        return sm

    def encode_message(self, message):
        # Codifica el mensaje y guarda la información de codificación
        encoded, dictionary = encode_message(message)
        self.root.get_screen('encode').encoded_output.text = encoded
        self.root.get_screen('encode').dictionary_output.text = dictionary

    def decode_message(self, encoded):
        # Decodifica el mensaje y muestra la información de decodificación
        decoded = decode_message(encoded)
        self.root.get_screen('decode').decoded_output.text = decoded

# Ejecuta la aplicación
if __name__ == '__main__':
    HuffmanApp().run()
