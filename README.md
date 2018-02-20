# B.Ash
A python bot created to play Pokemon Sapphire

THIS IS A WORK IN PROGRESS PROJECT

THERE WILL BE BUGS

THERE WILL BE CRASHES

But we're working towards the goal of a fairly smart bot who can move himself around the game world and eventually battle.


## How to use:

### Controls: 

  Movement - 
  
      up - i
      
    down - k
    
    left - j
    
    right - l
 
  select - z
  
  cancel - x

## Instructions:

1) Go to \Main Build\Scripts\

2) Run Main.py

3) Once the emulator has launched, launch pokemon sapphire and load into the game. (File > Open > Pokemon - Sapphire Version (U) (V1.1).gba > Open )

4) Position the player so that you can see the door of the south building, but not stand directly in front. (Note: The door must be fully visible and NOT in the bottom or top 8 pixels of the emulator).

5) Make sure that the emulator window isn't covered by any other window.

6) Read entire step: Hit enter in the script window (e.g. command prompt) and within 3 seconds click back onto the emulator window. After 3 seconds the bot should start moving around to the three doors of Littleroot town on a continuous loop.

7) To stop the bot and script, click back to the script window and press CTRL+C or just close the window. (Note: Because of the input style of the bot, if you focus on any other window the key presses will be sent to the focused window).



Currently the bot is not able to detect when it strays from the correct path. This means if the bot runs into a person without detecting them, it will throw the bot's positioning off and you will need to close and relaunch the script.

DO NOT USE THE PREVIOUS EMULATOR INSTANCE IF YOU RESTART THE SCRIPT. PLEASE CLOSE THE EMULATOR AND USE THE INSTANCE THAT IS OPENED WHEN THE SCRIPT IS STARTED.
