# Max Macropad
I wanted to create a small Keyboard with shortcuts, so I can simplify a lot of tasks on my PC. For example it significantly simplifies Photoshop workflows by binding complex multi-key shortcuts to a single press on my Macropad.
Moreover I have always wanted to dive into electronics and this macropad was the perfect starting point for me. 

My Hackpad has 7 keys. 6 of those keys are macros oriented in a row2col matrix, while the 7th key is to change between two layers. I also used a rotary encoder with a switch to change the volume on my pc.

## Features:
- 7 Keys + a switch in the rotary encoder
- 1 rotary encoder
- 2 LEDs as status lights
- XIAO RP2040

## Challenges:
I had some difficulties routing my PCB, because I did this for the first time. After multiple iterations I was eventually satisfied with the result. Fusion went pretty smooth for me, because I already had a bit of Experience in 3D Modeling.

# The build process:
## PCB:
The PCB was designed in KiCAD. I used a matrix for the keys. For the 8th key I used the switch of the rotary encoder. My routing on the PCB is still a bit messy, but I already improved significantly, considering my first iteration of routing.

_Note: First I used the wrong LEDs (SK6812), but I changed them later on to the SK6812MINI-E_

![](https://github.com/MaxKonze/Max-Macropad/blob/main/pcb/schematic%20image.png)
![](https://github.com/MaxKonze/Max-Macropad/blob/main/pcb/pcb.png)

## Case:
The case was made using Fusion. The top part of the case gets secured using M3 Screws and M3 heatset inserts. I decided to add a window to see the diodes, to give the design a bit more character. In the end I added a few design elements on the top side of my Hackpad, because I think it looks quite cool.

![](https://github.com/MaxKonze/Max-Macropad/blob/main/cad/Hackpad_1.png)
![](https://github.com/MaxKonze/Max-Macropad/blob/main/cad/Hackpad_2.png)

## Firmware:
I wrote the firmware using the KMK library in python. I'm using a 2-layer system to have more hotkeys on my macropad without needing more physical switches. For now I'm not 100% sure which hotkeys I want to have on my Hackpad, so I used letters as placeholders. I'll change that later. The LEDs work as a status light to show which layer is currently active.

[My Firmware](https://github.com/MaxKonze/Max-Macropad/blob/main/firmware/main.py)

# BOM:
|Amount|Part|
|------|---------
| 1x |XIAO RP2040 (with pins, so I can solder it through-hole)|
| 7x |Cherry MX Switches|
| 1x |EC11 Rotary Encoder EC11 + Switch + Vertical H20mm MountingHoles & 1x Knob|
| 7x |DSA Keycaps|
| 8x |1N4148 Diodes|
| 2x |SK6812 MINI-E LEDs|
| 7x |M3 Screws|
| 7x |M3 heat inserts|
| 1x |3D Printed Case|

(I used 3 more screws and heat inserts than allowed the secure my pcb in place. If it is not possible to ship those, I will just order them by myself.)
