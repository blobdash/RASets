from pycheevos.models.set import AchievementSet
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import *
from memory import Memory
from framework import achievement, achievement_set

import assets

@achievement_set(
    assets=assets,
    author="blobdash"
)
class MegamindSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=22146,
            title="Megamind: The Blue Defender"
        )

    @achievement(611949)
    def dt1_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.DOWNTOWN_1_STATE)
        )

    @achievement(611954)
    def dt2_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.DOWNTOWN_2_STATE)
        )
    
    @achievement(611955)
    def dt3_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.DOWNTOWN_3_STATE)
        )
    
    @achievement(611956)
    def dt4_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.DOWNTOWN_4_STATE)
        )
    
    @achievement(611957)
    def dt5_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.DOWNTOWN_5_STATE)
        )

    @achievement(611958)
    def ug1_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.UNDERGROUND_1_STATE)
        )

    @achievement(611959)
    def ug2_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.UNDERGROUND_2_STATE)
        )
    
    @achievement(611960)
    def ug3_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.UNDERGROUND_3_STATE)
        )
    
    @achievement(611961)
    def ug4_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.UNDERGROUND_4_STATE)
        )
    
    @achievement(611962)
    def ug5_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.UNDERGROUND_5_STATE)
        )
    
    @achievement(611963)
    def wf1_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.WATERFRONT_1_STATE)
        )

    @achievement(611964)
    def wf2_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.WATERFRONT_2_STATE)
        )
    
    @achievement(611965)
    def wf3_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.WATERFRONT_3_STATE)
        )
    
    @achievement(611966)
    def wf4_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.WATERFRONT_4_STATE)
        )
    
    @achievement(611967)
    def wf5_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.WATERFRONT_5_STATE)
        )
    
    @achievement(611968)
    def museum_clear(self, ach: Achievement):
        ach.add_core(
            on_first_clear(Memory.MUSEUM_STATE)
        )
    
    

if __name__=="__main__":
    MegamindSet().save("output/")
