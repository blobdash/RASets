from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_source, measured
from pycheevos.models.rich_presence import *

from memory import Memory
from logic import *

def render(conditions: ConditionList):
    return "_".join([cond.render() for cond in conditions])

class MoonRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 9969

    def generate(self):
        self.add_lookup('MenuState', {
            0x00: 'Loading...',
            0x04: 'Adjusting some settings',
            0x18: 'Deleting the save data?!',
            0x2e: 'On the title screen',
            0x56: 'Selecting a level in Quick Play'
        })
        self.add_lookup('Episode', {
            0x08: 'the Prologue',
            0x14: 'Episode 01',
            0x20: 'Episode 02',
            0x2c: 'Episode 03',
            0x38: 'Episode 04',
            0x44: 'Episode 05',
            0x50: 'Episode 06',
            0x5c: 'Episode 07',
            0x68: 'Episode 08',
            0x74: 'Episode 09',
            0x80: 'Episode 10',
            0x8c: 'Episode 11',
            0x98: 'Episode 12',
            0xa4: 'Episode 13',
            0xb0: 'Episode 14',
            0xbc: 'Episode 15',
            0xc8: 'Episode 16',
            0xd4: 'Episode 17'
        })
        self.add_lookup('Difficulty', {
            0: 'Rookie',
            1: 'Normal',
            2: 'Veteran'
        })

        # If the Game State pointer is not initialized, we are in the splash screens
        self.add_display(Memory.GAME_STATE == 0, 'Loading...')
        # First byte of the current area is always set to 00 when not ingame
        self.add_display(
            byte(Memory.CURRENT_AREA_ID) == 0x00, 
            f'@MenuState({ptr(Memory.GAME_STATE.address) >> ptr(0x190) >> measured(dword(0x30))})')
        self.add_display(
            byte(Memory.CURRENT_AREA_ID) != 0x00, 
            f'Major Kane is in @Episode({Memory.CURRENT_EPISODE}) • @Difficulty({Memory.CURRENT_DIFFICULTY})')
        self.add_display(None, "Playing Moon")

if __name__=="__main__":
    rp = MoonRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

