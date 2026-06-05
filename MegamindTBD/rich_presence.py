from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_source, measured
from pycheevos.models.rich_presence import *

from memory import Memory
from logic import *

def render(conditions: ConditionList):
    return "_".join([cond.render() for cond in conditions])

class MegamindRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 22146

    def generate(self):
        self.add_lookup('Level', {
            3: 'Downtown 1',
            4: 'Downtown 2',
            5: 'Downtown 3',
            6: 'Downtown 4',
            7: 'Downtown 5',
            8: 'The Museum',
            9: 'Underground 1',
            10: 'Underground 2',
            11: 'Underground 3',
            12: 'Underground 4',
            13: 'Underground 5',
            14: 'Waterfront 1',
            15: 'Waterfront 2',
            16: 'Waterfront 3',
            17: 'Waterfront 4',
            18: 'Waterfront 5'
        })
        self.add_lookup('MenuScene', {
            0x04: 'Staring at the title screen',
            (0x0a, 0x0c, 0x06, 0x07, 0x08): 'Selecting a save file',
            (0x1c, 0x1d, 0x1a): 'In the Main Menu',
            (0x26, 0x22): 'Choosing a level',
            0x16: 'Looking at goals',
            (0x12, 0x18): 'Admiring the film images',
            0x20: 'Reading the credits',
            (0x10, 0x0e, 0x1e): 'Tweaking some settings',
        }, default='In the backrooms')
        self.add_display((Memory.INGAME_CURRENT_STATUS == 0xffffffff) & (ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> dword(0xf0) <= 0x0c), f'{self.getMenuScene()}')
        self.add_display((Memory.INGAME_CURRENT_STATUS == 0xffffffff), f'{self.getMenuScene()} • {self.getMEGAs()} • {self.getFilms()}')
        self.add_display((Memory.INGAME_CURRENT_STATUS == 0xfffffffe), 'Loading...')
        self.add_display((Memory.INGAME_CURRENT_STATUS < 0xfffffffe), 
            f'Megamind is fighting crime in @Level({Memory.INGAME_CURRENT_STATUS}) • {self.getHealth()} • {self.getMEGAs()} • {self.getFilms()}'
        )
        self.add_display(None, "Playing Megamind: The Blue Defender")

    def getMenuScene(self):
        return f'@MenuScene({(ptr(Memory.MENU_STATE.address) >> ptr(0xac) >> ptr(0x140) >> measured(dword(0xf0)))})'

    def getHealth(self):
        return f"❤️@Number({group(
            remember((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x00) >> dword(0x10c))),
            measured_if(recall() <= 0xa000),
            measured(recall() / 406)
        )})%"
    
    def getMEGAs(self):
        return f"MEGA @Number({group(
            get_megas_for_level(Memory.DOWNTOWN_1_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_2_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_3_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_4_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_5_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_1_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_2_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_3_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_4_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_5_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_1_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_2_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_3_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_4_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_5_COLLECTIBLES),
            get_megas_for_level(Memory.MUSEUM_COLLECTIBLES),
            (measured(value(0x0)))
        )})/64"
    
    def getFilms(self):
        return f"🎞️ @Number({group(
            add_source(bit4(Memory.DOWNTOWN_1_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_2_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_3_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_4_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_5_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_1_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_2_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_3_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_4_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_5_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_1_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_2_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_3_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_4_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_5_COLLECTIBLES.address)),
            add_source(bit4(Memory.MUSEUM_COLLECTIBLES.address)),
            measured(value(0x0))
        )})/16"

if __name__=="__main__":
    rp = MegamindRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

