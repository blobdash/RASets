
from pycheevos.core.constants import *
from pycheevos.core.helpers import *
from pycheevos.core.value import MemoryValue

from memory import Memory

class Levels:
    DOWNTOWN_1 = 3
    DOWNTOWN_2 = 4
    DOWNTOWN_3 = 5
    DOWNTOWN_4 = 6
    DOWNTOWN_5 = 7
    MUSEUM = 8
    UNDERGROUND_1 = 9
    UNDERGROUND_2 = 10
    UNDERGROUND_3 = 11
    UNDERGROUND_4 = 12
    UNDERGROUND_5 = 13
    WATERFRONT_1 = 14
    WATERFRONT_2 = 15
    WATERFRONT_3 = 16
    WATERFRONT_4 = 17
    WATERFRONT_5 = 18

class Weapons:
    SCEPTER = 0x03
    BLASTER = 0x04
    FUSION = 0x05
    LASSO = 0x06
    EOM = 0x07
    BARRAGE = 0x08
    NOTHING = 0x0e

def on_first_clear(mem: MemoryValue) :
    return (
        (Memory.ROOT != 0) &
        (delta(bit4(mem.address)) == 0) &
        (bit4(mem.address) == 1)
    )