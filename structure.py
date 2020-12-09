name_feild = """
MDTextField:
    pos_hint:{"center_x":0.5 , "center_y":0.9}
    hint_text:"Enter Username"
    size_hint_x: None
    width: 250
    helper_text:"Minimum 5 Characters"
    helper_text_mode: "on_focus"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    
"""

age_feild = """
MDTextField:
    pos_hint:{"center_x":0.5 , "center_y":0.7}
    hint_text:"Enter Age"
    size_hint_x: None
    width: 250
    helper_text:"Minimum 8 Years"
    helper_text_mode: "on_focus"
    icon_right: "calendar"
    icon_right_color: app.theme_cls.primary_color
    
"""

email_feild = """
MDTextField:
    pos_hint:{"center_x":0.5 , "center_y":0.5}
    hint_text:"Enter Email ID"
    size_hint_x: None
    width: 250
    icon_right: "email"
    icon_right_color: app.theme_cls.primary_color
    
"""

password_feild = """
MDTextField:
    pos_hint:{"center_x":0.5 , "center_y":0.3}
    hint_text:"Enter Password"
    size_hint_x: None
    width: 250
    icon_right: "fingerprint"
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