import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatButton, MDFillRoundFlatIconButton, MDFloatingRootButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, IconLeftWidget, OneLineIconListItem
from kivy.uix.scrollview import ScrollView
from structure import name_feild, about_list, age_feild, email_feild, password_feild


class main_app(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A200"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.font_styles["JetBrainsMono"] = ["mono"]

        self.builder_1 = Builder.load_string(name_feild)
        self.builder_2 = Builder.load_string(age_feild)
        self.builder_3 = Builder.load_string(email_feild)
        self.builder_4 = Builder.load_string(password_feild)

        button = MDFillRoundFlatIconButton(text="Create Account", icon="plus", pos_hint={'center_x': 0.5, 'center_y': 0.1}, on_release=self.get_data)
        screen.add_widget(button)

        screen.add_widget(self.builder_1)
        screen.add_widget(self.builder_2)
        screen.add_widget(self.builder_3)
        screen.add_widget(self.builder_4)

        """
        info_list = Builder.load_string(about_list)
        screen.add_widget(info_list)
        icon = IconLeftWidget(icon="calendar", theme_text_color="Custom", text_color=(75/255, 250/255, 197/255, 1))
        icon2 = IconLeftWidget(icon="calendar", theme_text_color="Custom", text_color=(75/255, 250/255, 197/255, 1))
        info_list.ids.container_1.add_widget(icon)
        info_list.ids.container_2.add_widget(icon2)"""

        return screen

    def get_data(self, obj):
        text = ""

        if self.builder_1.text == "" or len(self.builder_1.text) < 5:
            self.builder_1.text = "NA"
            text = "Invalid Username"
            title = "Account Not Created"
        else:
            text = f"Account Created With Username : {self.builder.text}"
            title = "Account Created Sucessfully"

        close_btn = MDRectangleFlatButton(
            text="Ok", on_release=self.close_dialog)

        self.dailog = MDDialog(title=title, text=text, size_hint_x=0.9, buttons=[close_btn])
        self.builder_1.text = ""
        self.dailog.open()

    def close_dialog(self, obj):
        self.dailog.dismiss()


main_app().run()
