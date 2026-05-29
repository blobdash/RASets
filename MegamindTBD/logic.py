
from ast import Constant
from pycheevos.core.constants import *
from pycheevos.core.helpers import *
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

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

def ptr(value):
  return tbyte(value)

def on_first_clear(mem: MemoryValue) :
    return (
        (Memory.ROOT != 0) &
        (delta(bit4(mem.address)) == 0) &
        (bit4(mem.address) == 1)
    )

def generate_single_tt_lb(levelid: int, lb: Leaderboard):
    lb.set_start(
        (Memory.ROOT != 0) &
        (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
        (Memory.INGAME_CURRENT_STATUS == levelid) &
        (Memory.END_SCREEN_REACHED == 0x00)
    )
    lb.set_cancel(
        (Memory.ROOT == 0) &
        (Memory.END_SCREEN_REACHED == 0x00)
    )
    lb.set_submit(
        (delta(Memory.END_SCREEN_REACHED) == 0x00) &
        (Memory.END_SCREEN_REACHED == 0x01)
    )
    lb.set_value(
        measured(Memory.PAUSED_STATE != 0x01)
    )

def generate_section_tt_lb(range: range, lb: Leaderboard):
    lb.set_start(
        (Memory.ROOT != 0) &
        (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
        (Memory.INGAME_CURRENT_STATUS >= range.start) &
        (Memory.INGAME_CURRENT_STATUS <= range.stop) &
        (Memory.END_SCREEN_REACHED == 0x00)
    )
    lb.set_cancel(
        (Memory.INGAME_CURRENT_STATUS < 0xfffffffe) &
            (
                (Memory.INGAME_CURRENT_STATUS > range.stop) |
                (Memory.INGAME_CURRENT_STATUS < range.start)
            )
    )
    sub_conditions = []
    for i in range:
        sub_conditions.append(
            ((delta(Memory.END_SCREEN_REACHED) == 0x00) &
            (Memory.END_SCREEN_REACHED == 0x01) &
            (Memory.INGAME_CURRENT_STATUS == i)).with_hits(1)
        )
    lb.set_submit(
       sub_conditions
    )
    lb.set_value(
        measured((Memory.PAUSED_STATE == 0x00) & (Memory.INGAME_CURRENT_STATUS < 0xfffffffe))
    )

def track_kills(quantity: int):
    return (
        (Memory.END_SCREEN_REACHED == 0x00) &
        (Memory.TOTAL_ENNEMY_KILLS + (ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> ptr(0x48) >> ptr(0x138) >> delta(dword(0x4))) < quantity) &
        (Memory.TOTAL_ENNEMY_KILLS + (ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> ptr(0x48) >> ptr(0x138) >> dword(0x4)) >= quantity)
    )

def track_kills_alt(quantity: int):
    return (
        measured(Memory.TOTAL_ENNEMY_KILLS == quantity)
    )