import ctypes
import time

SendInput = ctypes.windll.user32.SendInput
secs = 0.1

Esc = 0x01
# --- Numbers 0 to 9 ---
Num1 = 0x02
Num2 = 0x03
Num3 = 0x04
Num4 = 0x05
Num5 = 0x06
Num6 = 0x07
Num7 = 0x08
Num8 = 0x09
Num9 = 0x0A
Num0 = 0x0B

Minus = 0x0C
Equals = 0x0D

Backspace = 0x0E
Tab = 0x0F

# --- Letters ---
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32

# --- Shifts ---
LShift = 0x2A

# --- Arrow Keys ---
LArrow = 0xCB
RArrow = 0xCD
UArrow = 0xC8
DArrow = 0xD0

# --- Numpad Keys ---

# --- Windows Keys ---
LWindows = 0xDB
RWindows = 0xDC

# --- Function Keys ---
F1 = 0x3B
F2 = 0x3C
F3 = 0x3D
F4 = 0x3E
F5 = 0x3F
F6 = 0x40
F7 = 0x41
F8 = 0x42
F9 = 0x43
F10 = 0x44

Enter = 0x1C


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
def Button_A():
    PressKey(Z)
    time.sleep(secs)
    ReleaseKey(Z)

def Button_B():
    PressKey(X)
    time.sleep(secs)
    ReleaseKey(X)

def Button_UP():
    PressKey(UArrow)
    time.sleep(secs)
    ReleaseKey(UArrow)

def Button_DOWN():
    PressKey(DArrow)
    time.sleep(secs)
    ReleaseKey(DArrow)

def Button_LEFT():
    PressKey(LArrow)
    time.sleep(secs)
    ReleaseKey(LArrow)

def Button_RIGHT():
    PressKey(RArrow)
    time.sleep(secs)
    ReleaseKey(RArrow)

def Button_START():
    PressKey(Enter)
    time.sleep(secs)
    ReleaseKey(Enter)

def Button_SELECT():
    PressKey(Backspace)
    time.sleep(secs)
    ReleaseKey(Backspaces)

def Bumper_LEFT():
    PressKey(A)
    time.sleep(secs)
    ReleaseKey(A)

def Bumper_RIGHT():
    PressKey(S)
    time.sleep(secs)
    ReleaseKey(S)

def Cap():
    PressKey(F12)
    time.sleep(secs)
    ReleaseKey(F12)
