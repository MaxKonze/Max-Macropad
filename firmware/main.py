# You import all the IOs of your board
import board
import time

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.statusled import statusLED

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

macros = Macros()
rotary_encoder = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules.append(rotary_encoder)

#rgb = RGB(pixel_pin=board.D6, num_pixels=2,val_limit=100,val_default=50,hue_default=0,sat_default=255,rgb_order=(1,0,2))
#eyboard.extensions.append(rgb)


keyboard.col_pins = (board.D7, board.D8)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [
        KC.AUDIO_MUTE, KC.B,
        KC.C, KC.D,
        KC.E, KC.F,
        KC.G, KC.H,
    ]
]

rotary_encoder.pins = ((board.D9, board.D10, None, False),)  # Define pins for one rotary encoder
rotary_encoder.map = [
    ((KC.VOLU, KC.VOLD),),
]

if __name__ == '__main__':
    keyboard.go()
