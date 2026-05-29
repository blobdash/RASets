from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import *
from memory import Memory
from framework import achievement, achievement_set, leaderboard

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
    
    @achievement(612686)
    def massive_goon_extinction(self, ach: Achievement):
        ach.add_core(
            track_kills(1500)
        )
        ach.add_alt(
            track_kills_alt(1500)
        )
        ach.add_alt(
            (always_true())
        )
    
    @leaderboard(163681)
    def dt1_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.DOWNTOWN_1, lb)
    
    @leaderboard(163685)
    def dt2_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.DOWNTOWN_2, lb)
    
    @leaderboard(163686)
    def dt3_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.DOWNTOWN_3, lb)
    
    @leaderboard(163687)
    def dt4_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.DOWNTOWN_4, lb)
    
    @leaderboard(163688)
    def dt5_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.DOWNTOWN_5, lb)

    @leaderboard(163689)
    def ug1_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.UNDERGROUND_1, lb)
    
    @leaderboard(163690)
    def ug2_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.UNDERGROUND_2, lb)
    
    @leaderboard(163691)
    def ug3_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.UNDERGROUND_3, lb)
    
    @leaderboard(163692)
    def ug4_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.UNDERGROUND_4, lb)
    
    @leaderboard(163693)
    def ug5_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.UNDERGROUND_5, lb)

    @leaderboard(163694)
    def wf1_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.WATERFRONT_1, lb)
    
    @leaderboard(163695)
    def wf2_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.WATERFRONT_2, lb)
    
    @leaderboard(163696)
    def wf3_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.WATERFRONT_3, lb)
    
    @leaderboard(163697)
    def wf4_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.WATERFRONT_4, lb)
    
    @leaderboard(163698)
    def wf5_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.WATERFRONT_5, lb)
    
    @leaderboard(163699)
    def museum_tt_lb(self, lb: Leaderboard):
        generate_single_tt_lb(Levels.MUSEUM, lb)

    @leaderboard(163717)
    def downtown_section_tt_lb(self, lb: Leaderboard):
        generate_section_tt_lb(range(Levels.DOWNTOWN_1, Levels.DOWNTOWN_5+1), lb)

    @leaderboard(163718)
    def underground_section_tt_lb(self, lb: Leaderboard):
        generate_section_tt_lb(range(Levels.UNDERGROUND_1, Levels.UNDERGROUND_5+1), lb)

    @leaderboard(163719)
    def waterfront_section_tt_lb(self, lb: Leaderboard):
        generate_section_tt_lb(range(Levels.WATERFRONT_1, Levels.WATERFRONT_5+1), lb)
        

if __name__=="__main__":
    MegamindSet().save("output/")
