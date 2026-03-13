## Sprite Transforms

transform t_alpha(x): #alters a sprite's visibility
    mesh True #prevents mesh from conflicting on layered sprites
    alpha x #determines level of visiblity

transform hop:
    linear 0.1 yoffset -150
    linear 0.1 yoffset 0
    linear 0.1 yoffset -150
    linear 0.1 yoffset 0

transform sway:
    ease 2 xalign 0.75 #this block has him sway from side to side
    ease 2 xalign 0.25 #ease is used due to it's speed being sudden
    repeat