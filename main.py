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


Builder.load_file("structure.kv")
kivy.core.window.Window.size = (350,600)

class MenuScreen(Screen):

    screen = ''
    name_field = kivy.properties.ObjectProperty(None)
    age_field = kivy.properties.ObjectProperty(None)
    email_field = kivy.properties.ObjectProperty(None)

    def get_data(self):
        ages = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27','28']
        name_field = self.name_field.text
        age_field = self.age_field.text
        email_field = self.email_field.text
        text = ""

        if name_field == "" or len(name_field) < 5 or age_field not in ages or check(email_field) == False:
            name_field = "NA"
            text = "Invalid Invalid"
            title = "Account Not Created"
            self.screen = 'no'

        else:
            text = f"Account Created With Username : {name_field}"
            title = "Account Created Sucessfully"
            self.screen = 'change'

        close_btn = MDRectangleFlatButton(
            text="Ok", on_release=self.close_dialog)

        self.dailog = MDDialog(title=title, text=text,
                               size_hint_x=0.9, buttons=[close_btn])

        self.dailog.open()

    def guest(self):
        main_app.sm.current = 'profile'

    def close_dialog(self, obj):
        self.name_field.text = ""
        self.age_field.text = ""
        self.dailog.dismiss()
        if self.screen == 'change':
            main_app.sm.current = 'profile'
                 
    
class ProfileScreen(Screen):

    play_audio = kivy.properties.ObjectProperty(None)

    def play_sound(self):
        play_audio = self.play_audio.text
        play(play_audio)

class main_app(MDApp):
    sm = ScreenManager()
    def build(self):

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A200"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.font_styles["JetBrainsMono"] = ["mono"]
        self.sm.add_widget(MenuScreen(name='login'))
        self.sm.add_widget(ProfileScreen(name='profile'))
        return self.sm
    def make(self):
        pass
main_app().run()
