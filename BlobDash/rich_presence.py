from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_source, measured
from pycheevos.models.rich_presence import *

from memory import Memory
from logic import *

def render(conditions: ConditionList):
    return "_".join([cond.render() for cond in conditions])

class BlobDashRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 37962

    def generate(self):
        self.add_lookup('MenuState', {
            (0x3d, 0x0f, 0x1e, 0x9d, 0xbf, 0xe1, 0x62): 'Blob is in the Main Menu',
            (0x16, 0x65): 'Blob made it to college!',
            (0x06, 0x13, 0x35, 0x3b, 0x70, 0x7f, 0x9c, 0xa1, 0xa5, 0xc9, 0xd1, 0xda, 0xe8, 0xeb, 0xfc): 'Blob is admiring the prints',
            (0x17, 0x63, 0x67, 0xc7): 'Blob is looking at their collection',
            (0xe2, 0xd2, 0x32): 'Blob is checking out the settings',
            (0x14, 0x50, 0x6d): 'Blob is thinking about their goals'
        }, default='Blob is in the backrooms')
        self.add_lookup('Difficulty', {
            0x01: '😁',
            0x02: '🙂',
            0x03: '☹️'
        })
        self.add_display(group(
            or_next(Memory.CURRENT_SCENE_ID == 0x45),
            or_next(Memory.CURRENT_SCENE_ID == 0x55),
            or_next(Memory.CURRENT_SCENE_ID == 0xf2),
            Memory.CURRENT_SCENE_ID == 0x03
        ),
        f'Blob is in the Title Screen')
        self.add_display(Memory.CURRENT_SCENE_ID == 0x38, f'Blob just learned about these shinies thingy')
        self.add_display(
            (Memory.CURRENT_SCENE_ID == 0x85),
            f'Blob is dashing through! • @Number({Memory.CURRENT_RUN_HP})HP {self.getCurrentShinies()}💎 {self.getCurrentDist()}yd🏃 • Total {self.getTotalShinies()}💎 {self.getTotalDist()}yd🏃 • @Difficulty({Memory.CURRENT_DIFFICULTY})'
        )
        self.add_display(
            (Memory.CURRENT_SCENE_ID == 0x3c),
            f'Blob is done for this run... • {self.getCurrentShinies()}💎 {self.getCurrentDist()}yd🏃 • Total {self.getTotalShinies()}💎 {self.getTotalDist()}yd🏃 • @Difficulty({Memory.CURRENT_DIFFICULTY})'
        )
        self.add_display(
            group(Memory.CURRENT_SCENE_ID != 0x00),
            f'@MenuState({Memory.CURRENT_SCENE_ID}) • Total {self.getTotalShinies()}💎 {self.getTotalDist()}yd🏃 • @Difficulty({Memory.CURRENT_DIFFICULTY})'
        )
        self.add_display(None, "Playing Blob Dash")

    def getCurrentShinies(self):
        return f'@Number({group(
            add_source(Memory.CURRENT_RUN_SHINIES),
            add_source(Memory.CURRENT_RUN_SHINIES_1 * 256),
            measured(value(0x0))
        )})'
    
    def getCurrentDist(self):
        return f'@Number({group(
            add_source(Memory.CURRENT_RUN_DISTANCE),
            add_source(Memory.CURRENT_RUN_DISTANCE_1 * 256),
            measured(value(0x0))
        )})'
    
    def getTotalShinies(self):
        return f'@Number({group(
            add_source(Memory.TOTAL_SHINIES),
            add_source(Memory.TOTAL_SHINIES_1 * 256),
            measured(value(0x0))
        )})'
    
    def getTotalDist(self):
        return f'@Number({group(
            add_source(Memory.TOTAL_DISTANCE),
            add_source(Memory.TOTAL_DISTANCE_1 * 256),
            measured(value(0x0))
        )})'

if __name__=="__main__":
    rp = BlobDashRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

