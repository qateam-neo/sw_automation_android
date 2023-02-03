from enum import Enum, IntEnum
import random

# class syntax
class AndroidEnums(IntEnum):
    KEYCODE_APP_SWITCH = 187
    KEYCODE_BACK = 4
    
    KEYCODE_BACKSLASH = 73

    KEYCODE_ESCAPE = 111
    KEYCODE_HOME = 3

    KEYCODE_VOLUME_DOWN = 25
    KEYCODE_VOLUME_MUTE = 164
    KEYCODE_VOLUME_UP = 24
    
    KEYCODE_CLEAR = 28
    KEYCODE_COPY = 278
    KEYCODE_CUT = 277
    KEYCODE_PASTE = 279
    KEYCODE_DEL = 67
    KEYCODE_ENTER = 66

class PredefinedEnums(IntEnum):
     
    CONSERVATIVE = 3
    BALANCED = 5
    GROWTH = 7
    
    def values(self):
         return [self.CONSERVATIVE, self.BALANCED, self.GROWTH]
    
    def Get_random_value(self):
        values=self.values()
        return random.choice(values)

