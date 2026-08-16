from turtle import speed
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
class MoonSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=9969,
            title="Moon"
        )
    
    @achievement(631253)
    def prologue_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_00, 'a0', '000', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631254)
    def pss1_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_02, 'a0', '025', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631255)
    def pss2_enter(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_03, 'a1', '000', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631256)
    def pss2_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_05, 'a1', '016', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631257)
    def eteo_clear(self, ach: Achievement):
        # for some reason this boss tps you to map 'dummy2' on clear instead of the next map for the LOLA section
        # it doesn't follow the standard map naming convention (xx_yyy) they use, so it looks weird but it works 
        ach.add_core(clearedChapter(Episode.EPISODE_07, 'du', 'my2', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631258)
    def waste_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_09, 'a2', '022', gamemode=Gamemode.ADVENTURE))

    @achievement(631259)
    def powerstation_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_11, 'a3', '032', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631260)
    def coldprocess_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_13, 'a4', '016', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631261)
    def irradiated_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_15, 'a1', '017', gamemode=Gamemode.ADVENTURE))
    
    @achievement(631262)
    def overlord_clear(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_17, 'a6', '014', gamemode=Gamemode.ADVENTURE))

    @achievement(631263)
    def muon_unlock(self, ach: Achievement):
        ach.add_core(Weapons.MUON.unlocked(Episode.EPISODE_01))
    
    @achievement(631264)
    def quanta_unlock(self, ach: Achievement):
        ach.add_core(Weapons.QUANTA.unlocked(Episode.EPISODE_04))
    
    @achievement(631265)
    def fermion_unlock(self, ach: Achievement):
        ach.add_core(Weapons.FERMION.unlocked(Episode.EPISODE_10))
    
    @achievement(631266)
    def lepton_unlock(self, ach: Achievement):
        ach.add_core(Weapons.LEPTON.unlocked(Episode.EPISODE_12))
    
    @achievement(631267)
    def oxid_unlock(self, ach: Achievement):
        ach.add_core(Weapons.OXID.unlocked(Episode.EPISODE_14))

    @achievement(631268)
    def seeker_unlock(self, ach: Achievement):
        ach.add_core(Weapons.SEEKER.unlocked(Episode.EPISODE_14))

if __name__=="__main__":
    MoonSet().save("output/")
