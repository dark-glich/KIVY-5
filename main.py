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


main = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    name : 'login'
    name_field : name_field
    age_field : age_field

    MDTextField:
        id : name_field
        pos_hint:{"center_x":0.5 , "center_y":0.9}
        hint_text:"Enter Username"
        size_hint_x: None
        width: 250
        helper_text:"Minimum 5 Characters"
        helper_text_mode: "on_focus"
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        id : age_field
        pos_hint:{"center_x":0.5 , "center_y":0.7}
        hint_text:"Enter Age"
        size_hint_x: None
        width: 250
        helper_text:"Only 8-15 Years"
        helper_text_mode: "on_focus"
        icon_right: "calendar"
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        pos_hint:{"center_x":0.5 , "center_y":0.5}
        hint_text:"Enter Email ID"
        size_hint_x: None
        width: 250
        icon_right: "email"
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        pos_hint:{"center_x":0.5 , "center_y":0.3}
        hint_text:"Enter Password"
        size_hint_x: None
        width: 250
        icon_right: "fingerprint"
        icon_right_color: app.theme_cls.primary_color

    MDFillRoundFlatIconButton:
        text:"Create Account" 
        icon:"plus" 
        pos_hint:{'center_x': 0.5, 'center_y': 0.1} 
        on_press : root.get_data()

<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:"Hello"

"""
#root.manager.current = 'profile'



class MenuScreen(Screen):

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

        else:
            text = f"Account Created With Username : {name_field}"
            title = "Account Created Sucessfully"

        close_btn = MDRectangleFlatButton(
            text="Ok", on_release=self.close_dialog)

        self.dailog = MDDialog(title=title, text=text,
                               size_hint_x=0.9, buttons=[close_btn])

        self.dailog.open()

    def close_dialog(self, obj):
        self.name_field.text = ""
        self.age_field.text = ""
        self.dailog.dismiss()
        sm.current = 'profile'


class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='login'))
sm.add_widget(ProfileScreen(name='profile'))


class main_app(MDApp):
    def build(self):

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A200"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.font_styles["JetBrainsMono"] = ["mono"]

        screen = Builder.load_string(main)

        return screen



main_app().run()
