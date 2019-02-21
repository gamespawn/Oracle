screen bathroom():
    imagebutton:
        hover im.Scale("images/testpoint.png", 100, 100)
        idle im.Scale("images/testpoint2.png", 100, 100)
        action Jump("sink")
        xpos 700
        ypos 390



    imagebutton:
        hover im.Scale("images/larrow.png", 225, 225)
        idle im.Scale("images/larrow.png", 225, 225)
        action Jump("kitchen")
        xpos 002
        ypos 390

    imagebutton:
        hover im.Scale("images/rarrow.png", 225, 225)
        idle im.Scale("images/rarrow.png", 225, 225)
        action Jump("bedroom")
        xpos 1108
        ypos 390
