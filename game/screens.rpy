
define config.default_text_cps = 40

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


transform posisi_kiri:
    zoom 0.5
    xpos 230
    yalign 1.0


transform posisi_kanan:
    zoom 0.5
    xpos 1690
    xanchor 1.0
    yalign 1.0


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


screen choice(items):

    modal True
    zorder 200

    frame:
        background None
        xalign 0.5
        yalign 0.55
        xsize 1000

        vbox:
            spacing 20
            xalign 0.5

            for i in items:

                textbutton i.caption:
                    action i.action

                    xsize 900
                    xalign 0.5
                    padding (30, 20)

                    background "#FFFFFF25"
                    hover_background "#FFFFFF55"

                    text_color "#FFFFFF"
                    text_hover_color "#FFFFFF"

                    text_size 28
                    text_xalign 0.5
                    text_text_align 0.5


screen character_portrait(image_name, position="left"):

    if position == "left":
        add image_name:
            zoom 0.5
            xalign 0.12
            yalign 1.0

    elif position == "right":
        add image_name:
            zoom 0.5
            xalign 0.88
            yalign 1.0
