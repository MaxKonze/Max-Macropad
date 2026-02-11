# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB

active_layer = 0

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

macros = Macros()
rotary_encoder = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules.append(rotary_encoder)

rgb = RGB(pixel_pin=board.D6, num_pixels=2)

def change_layer_on_macro_press(keyboard, coordinate, is_pressed):
    global active_layer
    if is_pressed:
        if active_layer == 0:
            active_layer = 1
            rgb.set_rgb_fill((255, 0, 0))  # Change to red when on layer 1    
        else:
            active_layer = 0
            rgb.set_rgb_fill((0, 0, 255))  # Change to blue when on layer 0
        keyboard.active_layers = [active_layer]

LAYER_KEY = KC.NO.clone()
LAYER_KEY.on_press_fn = (change_layer_on_macro_press)

keyboard.col_pins = (board.D7, board.D8)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [
        KC.A, KC.B, 
        KC.C, KC.D,
        KC.E, KC.F, 
        KC.G, KC.LAYER_KEY,
    ]
    ,
    [
        KC.N1, KC.N2, 
        KC.N3, KC.N4,
        KC.N5, KC.N6, 
        KC.N7, KC.LAYER_KEY,
    ],
]

rotary_encoder.pins = ((board.D9, board.D10, None, False),)  # Define pins for one rotary encoder
rotary_encoder.map = [
    ((KC.VOLU, KC.VOLD),), 
]

if __name__ == '__main__':
    keyboard.go()