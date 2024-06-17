from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import firebase_admin
import requests
from firebase import firebase
from firebase_admin import credentials, auth
import pyrebase 

fc = {
    'apiKey': "AIzaSyCYqvGvItSXGi9evCBWZ1BP8jfnACBT1D8",
    'authDomain': "jonathan-professor-trabalho-jo.firebaseapp.com",
    'databaseURL': "https://jonathan-professor-trabalho-jo-default-rtdb.firebaseio.com",
    'projectId': "jonathan-professor-trabalho-jo",
    'storageBucket': "jonathan-professor-trabalho-jo.appspot.com",
    'messagingSenderId': "954624217025",
    'appId': "1:954624217025:web:e2962bfaca7bd7bec86940",
    'measurementId': "G-N832EB1EEV"
}

f=pyrebase.initialize_app(fc)
auth=f.auth()

Window.clearcolor = (1,1,1,1)

class Gerador (ScreenManager):
    pass

class Login (Screen):
    pass

class Cadastro (Screen):
    pass

class Login(App):
    
    def build (self):
        return Builder.load_file('main.kv')
    
    def Cadastrar(self):
        email = self.root.get_screen('Cadastro').ids.email.text
        senha = self.root.get_screen('Cadastro').ids.senha.text

        try:
            user = auth.create_user_with_email_and_password(email, senha)
        except:
            self.root.get_screen('Cadastro').ids.sts.color = (1,0,0,1)
        else:
            self.root.current = 'login'

    def Logar(self):
        email = self.root.get_screen('login').ids.email.text
        senha = self.root.get_screen('login').ids.senha.text

        try:        
            auth.sign_in_with_email_and_password(email, senha)

        except:
            self.root.get_screen('login').ids.sts.text = 'Erro no login.'
            self.root.get_screen('login').ids.sts.color = (1,0,0,1)

        else:
            self.root.get_screen('login').ids.sts.text = "Sucesso no login!"
            self.root.get_screen('login').ids.sts.color = (0.2,0.2,1,1)

if __name__ == "__main__":
    Login().run()    