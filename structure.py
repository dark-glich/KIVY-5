name_feild = """
MDTextField:
    pos_hint:{"center_x":0.5 , "center_y":0.4}
    hint_text:"Enter Username"
    size_hint_x: None
    width: 250
    helper_text:"Minimum 5 Characters"
    helper_text_mode: "on_focus"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    
"""

about_list = """
ScrollView:
    MDList:
        OneLineIconListItem:
            text: "Created On"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            id : container_1

        OneLineIconListItem:
            text: "5 Dec 2020"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            id : container_2
"""