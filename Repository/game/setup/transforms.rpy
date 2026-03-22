## Sprite Transforms

transform t_alpha(x): #alters a sprite's visibility
    mesh True #prevents mesh from conflicting on layered sprites
    alpha x #determines level of visiblity

transform flip:
    xzoom -1.0

transform flip_r: #reverts sprite's original xzoom
    xzoom 1.0

transform hop:
    linear 0.1 yoffset -150
    linear 0.1 yoffset 0
    linear 0.1 yoffset -150
    linear 0.1 yoffset 0

transform sway:
    ease 2 xalign 0.75 #this block has him sway from side to side
    ease 2 xalign 0.25 #ease is used due to it's speed being sudden
    repeat

transform invert_camera: #inverts camera
    matrixcolor InvertMatrix(1.0) #inverts the screen colors

transform revert_camera: #resets camera
    subpixel True 
    additive 0.0 
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

transform red_camera: #turns screen dark red
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.25)*HueMatrix(135.0) 

init python:
    def vfxdissolve(img: str): #img: str calls the image typed in parenthesis
        return MultipleTransition([
            False, Dissolve(0.2), #this line hides the old scene
            img,   Pause(0.2),
            img,   dissolve, #dissolve is the transition the calls in the VFX
            True, #this line displays the vfx
        ])

transform in_and_out():
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        linear 0.2 alpha 0.0

screen image_display(img: str):
    timer 0.2 action Return(None)
    hbox:
        align (0.5, 0.5) 
        add img
        at in_and_out