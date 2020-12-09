import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDFillRoundFlatIconButton, MDFloatingRootButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, IconLeftWidget, OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


Builder.load_file("structure.kv")


class MenuScreen(Screen):

    screen = ''

    name_field = ObjectProperty(None)
    age_field = ObjectProperty(None)

    def get_data(self):
        ages = ['8', '9', '10', '11', '12', '13', '14', '15']
        name_field = self.name_field.text
        age_field = self.age_field.text
        text = ""

        if name_field == "" or len(name_field) < 5 or age_field not in ages:
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

    def close_dialog(self, obj):
        self.name_field.text = ""
        self.age_field.text = ""
        self.dailog.dismiss()
        if self.screen == 'change':
            main_app.sm.current = 'profile'


class ProfileScreen(Screen):
    pass


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


main_app().run()
