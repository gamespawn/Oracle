screen mainphonescreen:
    hotspot (127, 492, 86, 42) clicked Jump("hide_all_phone_screens") # Home button (Exits)
    frame at popup:
        xalign 0.5
        add "Phone/150Phone.png"
        grid 4 4:
            imagebutton auto "phone/photo_%s.png" action ui.jumps("take_a_photo")
            

label travel_map_a:
    call hide_all_phone_screens
    show screen blank_phone_screen
    show screen travel_map_a
    "" #Need this, or bad things will happen...
    jump travel_map_a # To prevent more bad things happening.
    
    
transform popup:
    yalign 10.0 rotate 50
    linear 0.3 yalign 0.5 rotate 0


#-----------------------------------

# This creates the button to show the phone menus
screen button:
    imagebutton idle "Phone/phone smallest.png" hover "Phone/phone smaller.png" action Show('mainphonescreen') xalign 0.0 yalign 0.0
 
#*******************************************************************************#
#                                                PHONE STARTING SCREEN                                                        #
#*******************************************************************************#

# This part shows the main phone screen, and controls what happens when icons are clicked.   

transform popup:
    yalign 10.0 rotate 50 xalign 0.4
    linear 0.3 yalign 0.5 rotate 0 xalign 0.5
    
screen mainphonescreen:
    modal True
    frame at popup:
        xpadding 0 ypadding 0
        xmaximum 334 ymaximum 555
        background "Phone/300x400 phone no icons.png"
        use phoneselect
        hbox xalign 0.5 yalign 1.0:
            spacing 100
            imagebutton auto "phone/icons/1_%s.png" action Hide('phoneui', transition=dissolve) # Back button
            imagebutton auto "phone/icons/1_%s.png" action [Hide('mainphonescreen', transition=dissolve), Hide('phoneui', transition=dissolve)] # Home button (Exits)
        
screen phoneselect:
    grid 3 4 spacing 30 xalign 0.5 yalign 0.5:
        imagebutton auto "phone/icons/1_%s.png" action Show('start_map_app', transition=dissolve) # 1st icon (Map)
        
        
        
#----------------------------------------------


screen start_map_app:
    tag phoneui
    side "c b r":
        xmaximum 296 ymaximum 353
        xalign 0.5 yalign 0.5
        viewport id "vp":
             draggable True
             vbox:
                 
                 imagebutton:
                     idle "Maps/mega tokyo map 3.jpg"
                     hover "Maps/mega tokyo map 3.jpg"
                     #action ui.callsinnewcontext("start_word_list") # FOR TESTING OTHER PHONE ICONS