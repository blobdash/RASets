from pycheevos.core.constants import *
from pycheevos.core.helpers import *
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

from memory import Memory

FRAMERATE = 60

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

class Weapons_Offsets:
    BLASTER = 0x00
    LASSO = 0x20
    FUSION = 0x08
    EOM = 0x10
    BARRAGE = 0x18

class Weapon:
    OFFSET: int
    
    def __init__(self, offset) -> None:
        self.OFFSET = offset
    
    def hasUpgraded(self):
        return (
            ptr(Memory.ROOT.address)
            >> ptr(0x64)
            >> ptr(0x00)
            >> ptr(0x2E8)
            >> ptr(0x1C)
            >> ptr(self.OFFSET)
            >> delta(dword(0x50)) < dword(0x50)
        )
    
    def reachedLevel(self, level):
        return (
            ptr(Memory.ROOT.address)
            >> ptr(0x64)
            >> ptr(0x00)
            >> ptr(0x2E8)
            >> ptr(0x1C)
            >> ptr(self.OFFSET)
            >> delta(dword(0x50)) == level-2
        ) & (
            ptr(Memory.ROOT.address)
            >> ptr(0x64)
            >> ptr(0x00)
            >> ptr(0x2E8)
            >> ptr(0x1C)
            >> ptr(self.OFFSET)
            >> dword(0x50) == level-1
        )
    
    def ammoConsumed(self):
        return group(
            (ptr(Memory.ROOT.address)
            >> delta(dword(0x64)) != 0) &
            (ptr(Memory.ROOT.address)
            >> ptr(0x64)
            >> ptr(0x00)
            >> ptr(0x2E8)
            >> ptr(0x1C)
            >> ptr(self.OFFSET)
            >> delta(dword(0x48)) > dword(0x48)),
        )

class Weapons:
    BLASTER = Weapon(0x00)
    LASSO = Weapon(0x20)
    FUSION = Weapon(0x08)
    EOM = Weapon(0x10)
    BARRAGE = Weapon(0x18)

class BOUNDING_BOX:
    MAX_X: int
    MIN_X: int
    MAX_Y: int
    MIN_Y: int
    MARGIN:int = 10000

    def __init__(self, MAX_X: int, MIN_X: int, MAX_Y: int, MIN_Y: int) -> None:
        self.MAX_X = MAX_X
        self.MIN_X = MIN_X
        self.MAX_Y = MAX_Y
        self.MIN_Y = MIN_Y

    def getConditionsInBox(self):
        return (
            (ptr(Memory.ROOT.address) >> ptr(0x64)>> ptr(0x00) >> dword(0xa8) >= (self.MIN_X - self.MARGIN)) &
            (ptr(Memory.ROOT.address) >> ptr(0x64)>> ptr(0x00) >> dword(0xa8) <= (self.MAX_X + self.MARGIN)) &
            (ptr(Memory.ROOT.address) >> ptr(0x64)>> ptr(0x00) >> dword(0xb0) >= (self.MIN_Y - self.MARGIN)) &
            (ptr(Memory.ROOT.address) >> ptr(0x64)>> ptr(0x00) >> dword(0xb0) <= (self.MAX_Y + self.MARGIN))
        )

class BOSS_ARENAS:
    DESTRUCTION_WORKER = BOUNDING_BOX(882096, 783990, 1179411, 1067632)
    PSYCHO_DELIC = BOUNDING_BOX(476299, 375155, 2989493, 2891571)
    HOT_FLASH= BOUNDING_BOX(649610, 457808, 1579085, 1408314)

def ptr(value):
  return tbyte(value)

def on_first_clear(mem: MemoryValue) :
    return (
        (Memory.ROOT != 0) &
        (delta(bit4(mem.address)) == 0) &
        (bit4(mem.address) == 1)
    )

def weapon_unlock(weapon_offset: int):
    return (
        (Memory.ROOT != 0) &
        ((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> ptr(0x2E8) >> ptr(0x1C) >> ptr(weapon_offset) >> delta(byte(0x70))) == 0) &
        ((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> ptr(0x2E8) >> ptr(0x1C) >> ptr(weapon_offset) >> byte(0x70) == 1))
    )

def generate_single_tt_lb(levelid: int, lb: Leaderboard):
    lb.set_start(
        (Memory.ROOT != 0) &
        (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
        (Memory.INGAME_CURRENT_STATUS == levelid)
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
        (Memory.INGAME_CURRENT_STATUS <= range.stop - 1)
    )
    lb.set_cancel(
        # force core to always true
        always_true(),
        # alt1 : cancel if player loads a level before this section
        (Memory.INGAME_CURRENT_STATUS < range.start),
        # alt2 : cancel if player loads a level after this section
        (Memory.INGAME_CURRENT_STATUS < 0xfffffffe) & (Memory.INGAME_CURRENT_STATUS > range.stop - 1),
        # alt3 : cancel if player is on title screen
        (ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> delta(dword(0xf4)) == 0x0a) &
        (ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> dword(0xf4) == 0x04)
    )
    sub_conditions = []
    for i in range:
        sub_conditions.append(
            ((delta(Memory.END_SCREEN_REACHED) == 0x00) &
            (Memory.END_SCREEN_REACHED == 0x01) &
            (Memory.INGAME_CURRENT_STATUS == i)).with_hits(1)
        )
    resetif_sub_conditions = []
    for i in range:
        resetif_sub_conditions.append(
            (Memory.END_SCREEN_REACHED == 0x01) &
            (delta(Memory.INGAME_CURRENT_STATUS) == i) &
            add_hits(Memory.INGAME_CURRENT_STATUS == 0xfffffffe).with_hits(1)
        )
        
    lb.set_submit(group(
        sub_conditions,
        # reset if player loads a level not in this section
        reset_if(Memory.INGAME_CURRENT_STATUS < range.start),
        reset_if((Memory.INGAME_CURRENT_STATUS < 0xfffffffe) & (Memory.INGAME_CURRENT_STATUS > range.stop - 1)),
        # reset if player is on title screen
        reset_if((ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> delta(dword(0xf4)) == 0x0a) &
            (ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> dword(0xf4) == 0x04)
        ),
        # add hit for each completed level, the toolkit just doesn't reset hits after a successful submit.
        # resets when player comes back to main menu and has cleared all levels since leaderboard start
        resetif_sub_conditions,
        reset_if(
            always_false().with_hits(5)
        )
    ))
    lb.set_value(
        measured((Memory.PAUSED_STATE == 0x00) & (Memory.INGAME_CURRENT_STATUS < 0xfffffffe))
    )

def generate_section_tt_ach(range: range, minutes: int, seconds: int):
    sub_conditions = []
    for i in range:
        sub_conditions.append(
            trigger(((delta(Memory.END_SCREEN_REACHED) == 0x00) &
            (Memory.END_SCREEN_REACHED == 0x01) &
            (Memory.INGAME_CURRENT_STATUS == i)).with_hits(1))
        )
    return group(
        ((delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
        (Memory.INGAME_CURRENT_STATUS >= range.start) &
        (Memory.INGAME_CURRENT_STATUS <= range.stop - 1)).with_hits(1),
        # reset if player loads a level before this section
        reset_if(Memory.INGAME_CURRENT_STATUS < range.start),
        # reset if player loads a level after this section
        reset_if((Memory.INGAME_CURRENT_STATUS < 0xfffffffe) & (Memory.INGAME_CURRENT_STATUS > range.stop - 1)),
        # reset if player is on title screen
        reset_if((ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> delta(dword(0xf4)) == 0x0a) &
        (ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> dword(0xf4) == 0x04)),
        # resetif timer expired
        reset_if((Memory.PAUSED_STATE == 0x00) & (Memory.INGAME_CURRENT_STATUS < 0xfffffffe).with_hits(speedrun_hits(minutes, seconds))),
        sub_conditions
    )

def track_kills(quantity: int):
    return (
        (Memory.INGAME_CURRENT_STATUS < 0xfffffffe) &
        (Memory.END_SCREEN_REACHED == 0x00) &
        (Memory.TOTAL_ENEMY_KILLS + (ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> ptr(0x48) >> ptr(0x138) >> delta(dword(0x4))) < quantity) &
        (Memory.TOTAL_ENEMY_KILLS + (ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> ptr(0x48) >> ptr(0x138) >> dword(0x4)) >= quantity)
    )

def track_kills_alt(quantity: int):
    return (
        measured(Memory.TOTAL_ENEMY_KILLS == quantity)
    )

def get_megas_for_level(level: MemoryValue):
    return group(
        ((add_source(bitcount(level.address)))),
        ((sub_source(bit4(level.address))))
    )

def get_megas_deltas_for_level(level: MemoryValue):
    return group(
        add_source(delta(bitcount(level.address))),
        sub_source(delta(bit4(level.address)))
    )

def nohit_boss(level: int, box: BOUNDING_BOX):
    return group(
        (
            (Memory.INGAME_CURRENT_STATUS == level) &
            box.getConditionsInBox()
        ),
        (
            # pauseif hp goes down and in box
            reset_next_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe)
        ),
        (
            pause_if((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x0) >> dword(0x10c) < delta(dword(0x10c))) & box.getConditionsInBox()).with_hits(1)
        ),
        (
            # pauseif invincibility triggers (for voidouts)
            reset_next_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe)
        ),
        (
            pause_if((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x0) >> dword(0x1b8) == 1) & box.getConditionsInBox()).with_hits(1)
        ),
        (
            delta(Memory.END_SCREEN_REACHED) == 0x00
        ),
        (
            # trigger if end screen goes from 0 to 1
            trigger(Memory.END_SCREEN_REACHED == 0x01)
        )
    )

def speedrun_hits(min: int, seconds: int):
    return ((min * 60) + seconds) * FRAMERATE