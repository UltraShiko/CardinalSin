
define bloodflash = Fade(.25, 0.0, .75, color="#ff0000")
define graceflash = Fade(.25, 0.0, .75, color="#92a9f5")
define maliceflash = Fade(.25, 0.0, .75, color="#680a0a")
define sinflash = Fade(.25, 0.0, .75, color="#56066e")
define iceblast = Fade(.1, 0.0, .75, color="#ced6f0")
define fireflash = Fade(.25, 0.0, .75, color="#cb7f1c")
define electricflash = Fade(.25, 0.0, .75, color="#5c7bd5")

define iris_in_out = ImageDissolve("images/transitions/eye_1.png", 0.5)
define iris_in_out_slow = ImageDissolve("images/transitions/eye_1.png", 1.0)

define quickblinds = ImageDissolve(im.Tile("blindstile.png"), 0.5, 8)
define quicksquares = ImageDissolve(im.Tile("squarestile.png"), 0.5, 256)
