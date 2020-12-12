import kivy
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDFillRoundFlatIconButton, MDFloatingRootButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, IconLeftWidget, OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from texttospeech import play
from emailcheck import check
from kivymd.uix.snackbar import Snackbar

Builder.load_file("structure.kv")
kivy.core.window.Window.size = (350,600)

class settingScreen(Screen):
    name = kivy.properties.ObjectProperty(None)
    email = kivy.properties.ObjectProperty(None)


class MenuScreen(Screen):

    screen = ''
    user = kivy.properties.ObjectProperty(None)
    age_field = kivy.properties.ObjectProperty(None)
    email_field = kivy.properties.ObjectProperty(None)
    pass_field = kivy.properties.ObjectProperty(None)

    def get_data(self):
        ages = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27','28']
        name = self.user.text
        age_field = self.age_field.text
        email_field = self.email_field.text
        pass_field = self.pass_field.text
        text = ""

        if name == "" or len(name) < 5 or age_field not in ages or check(email_field) == False or len(pass_field) < 8:
            
            text = "Invalid Invalid"
            title = "Account Not Created"
            self.screen = 'no'

        else:
            text = f"Account Created With Username : {name}"
            title = "Account Created Sucessfully"
            self.screen = 'change'

        close_btn = MDRectangleFlatButton(
            text="Ok", on_release=lambda x : self.close_dialog(name , email_field))

        self.dailog = MDDialog(title=title, text=text,
                               size_hint_x=0.9, buttons=[close_btn])

        self.dailog.open()

    def guest(self):
        main_app.sm.current = 'profile'

    def close_dialog(self, x, y):
        settingScreen.name = x
        settingScreen.email = y
        print(settingScreen.name)
        self.text = ""
        self.user.text = ""
        self.age_field.text = ""
        self.email_field.text = ""
        self.password_field = ""
        self.dailog.dismiss()
        if self.screen == 'change':
            settingScreen.name = "GuestName" 
            main_app.sm.current = 'profile'
    
class ProfileScreen(Screen):

    play_audio = kivy.properties.ObjectProperty(None)

    audio = ''

    def play_sound(self):
        play_audio = self.play_audio.text
        play(play_audio)
        self.audio = 'recorded'

    def open_dialog(self):

        text = ''
        title = '' 

        if self.audio == 'recorded':
            text = "With filename recording.mp3"
            title='File Saved'
        else:
            title = "File Not Saved"
            text = "Please Record The File First"

        close_btn = MDRectangleFlatButton(text="Ok", on_release=self.close_dialog)

        self.dailog = MDDialog(title=title, text=text,size_hint_x=0.9, buttons=[close_btn])

        self.dailog.open()

    def close_dialog(self, obj):
        self.dailog.dismiss()


class main_app(MDApp):
    sm = ScreenManager()
    def build(self):

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A200"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.font_styles["JetBrainsMono"] = ["mono"]
        self.sm.add_widget(MenuScreen(name='login'))
        self.sm.add_widget(ProfileScreen(name='profile'))
        self.sm.add_widget(settingScreen(name='setting'))

        return self.sm
    def change_dark(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "A200"

    def change_light(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "A200"

main_app().run()
