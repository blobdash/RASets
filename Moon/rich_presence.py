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
            0x04: 'Adjusting some settings',
            0x18: 'Deleting the save data?!',
            0x2e: 'On the title screen',
            0x56: 'Selecting a level in Quick Play'
        }, default='Loading...')
        self.add_lookup('Episode', {
            0x08: 'in the Prologue',
            0x14: 'in the PSS I',
            0x20: 'fighting the first Guardian',
            0x2c: 'escaping the PSS I',
            0x38: 'in the PSS II',
            0x44: 'fighting the Sanctus Vector',
            0x50: 'escaping the PSS II',
            0x5c: 'in the Non-ETEO Transport Vessel',
            0x68: 'in the Waste Disposal',
            0x74: 'fighting the second Guardian',
            0x80: 'in the Power Station',
            0x8c: 'fighting the Phexic Manifold',
            0x98: 'in the Cold Process',
            0xa4: 'fighting the third Guardian',
            0xb0: 'in the Irradiated Stratum',
            0xbc: 'fighting the Matrix Progenitor',
            0xc8: 'in the Fermian Homeworld',
            0xd4: 'fighting the Overlord',
            (0xe0, 0xec, 0xf8, 0x04, 0x1c, 0x10): 'training with Tsuke'
        })
        self.add_lookup('Difficulty', {
            0: 'Rookie',
            1: 'Normal',
            2: 'Veteran'
        })
        self.add_lookup('Gamemode', {
            0xff: 'Adventure Mode',
            (0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07): 'Quick Play'
        })

        # If the Game State pointer is not initialized, we are in the splash screens
        self.add_display(Memory.GAME_STATE == 0, 'Loading...')
        # First byte of the current area is always set to 00 when not ingame
        self.add_display(
            is_not_ingame(), 
            f'@MenuState({ptr(Memory.GAME_STATE.address) >> ptr(0x190) >> measured(dword(0x30))})')
        self.add_display(
            is_ingame(),
            f'Major Kane is @Episode({Memory.CURRENT_EPISODE}) • @Number({Condition(0x64, '-', Memory.HEALTH_HOST)})❤️ @Difficulty({Memory.CURRENT_DIFFICULTY}) • @Gamemode({Memory.QUICK_PLAY_LEVEL_SELECT_INDEX})')
        self.add_display(None, "Playing Moon")

if __name__=="__main__":
    rp = MoonRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

