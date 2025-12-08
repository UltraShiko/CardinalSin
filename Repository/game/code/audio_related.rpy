
init python: 
    
    # Allows me to attach sound fx to transform commands
    
    def play_sound_c(trans, st, at, file=None):
        renpy.sound.play(file, loop=False)
        return None

    play_sound = renpy.curry(play_sound_c)
