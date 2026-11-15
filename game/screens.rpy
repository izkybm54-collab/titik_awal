
screen main_menu():

    tag menu

    # Background
    add "images/background_menu.jpg":
        xysize (config.screen_width, config.screen_height)
    # Logo / Judul
    add "images/logo.png":
        xalign 0.5
        yalign 0.25
        xsize 650

    # Menu navigasi
    vbox:
        xalign 0.5
        yalign 0.68
        spacing 15

        textbutton "NEW GAME":
            action Start()

        textbutton "CONTINUE":
            action ShowMenu("load")

        textbutton "CHAPTER SELECTION":
            action NullAction()

        textbutton "SETTINGS":
            action ShowMenu("preferences")

        textbutton "QUIT":
            action Quit(confirm=True)

screen say(who, what):

    window:
        id "window"

        xalign 0.5
        yalign 0.78

        xsize 1100
        padding (40, 30)

        background Frame(
            Solid("#FFFFFF35"),
            30, 30
        )

        vbox:
            spacing 15
            xalign 0.5

            if who is not None:
                text who id "who":
                    size 30
                    color "#FFFFFF"
                    outlines [(2, "#00000055", 0, 0)]
                    xalign 0.5

            text what id "what":
                size 26
                color "#FFFFFF"
                outlines [(2, "#00000055", 0, 0)]
                xmaximum 1020
                text_align 0.5