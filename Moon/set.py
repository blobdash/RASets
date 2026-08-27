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

    @achievement(631407)
    def guardian1_tt(self, ach: Achievement):
        ach.add_core(chapterTimeTrial(Episode.EPISODE_02, 1, 0))
    
    @achievement(631469)
    def sanctus_healchallenge(self, ach: Achievement):
        ach.add_core(sanctus_healchallenge(10))
    
    @achievement(631408)
    def eteo_tt(self, ach: Achievement):
        ach.add_core(chapterTimeTrial(Episode.EPISODE_07, 2, 30))
    
    @achievement(631409)
    def guardian2_tt(self, ach: Achievement):
        ach.add_core(chapterTimeTrial(Episode.EPISODE_09, 1, 15))
    
    @achievement(633036)
    def phexic_accchallenge(self, ach: Achievement):
        ach.add_core(phexic_accchallenge(95))
    
    @achievement(631410)
    def guardian3_tt(self, ach: Achievement):
        ach.add_core(conditions=chapterTimeTrial(Episode.EPISODE_13, 2, 0))
    
    @achievement(633027)
    def overlord_tt(self, ach: Achievement):
        ach.add_core(chapterTimeTrial(Episode.EPISODE_17, 3, 0))
    
    @achievement(633028)
    def pss1_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_02, 'a0', '025', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))

    @achievement(633029)
    def pss2_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_05, 'a1', '016', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))
    
    @achievement(633030)
    def eteo_veteran(self, ach: Achievement):
        # for some reason this boss tps you to map 'dummy2' on clear instead of the next map for the LOLA section
        # it doesn't follow the standard map naming convention (xx_yyy) they use, so it looks weird but it works 
        ach.add_core(clearedChapter(Episode.EPISODE_07, 'du', 'my2', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))
    
    @achievement(633031)
    def waste_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_09, 'a2', '022', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))

    @achievement(633032)
    def powerstation_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_11, 'a3', '032', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))
    
    @achievement(633033)
    def coldprocess_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_13, 'a4', '016', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))
    
    @achievement(633034)
    def irradiated_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_15, 'a1', '017', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))
    
    @achievement(633035)
    def overlord_veteran(self, ach: Achievement):
        ach.add_core(clearedChapter(Episode.EPISODE_17, 'a6', '014', gamemode=Gamemode.ADVENTURE, difficulty=Difficulty.VETERAN))
    
    @achievement()
    def pssiexit_trial(self, ach: Achievement):
        ach.add_core(pssitrial(35))
    
    @achievement()
    def pssiisatellite_trial(self, ach: Achievement):
        ach.add_core(pssiisatellitetrial(60))
    
    # Leaderboards

    @leaderboard(170216)
    def display(self, lb: Leaderboard):
        timer_display(lb)

    @leaderboard(169465)
    def guardian1_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_02, Difficulty.NORMAL, lb)
    
    @leaderboard(169466)
    def guardian1_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_02, Difficulty.VETERAN, lb)
    
    @leaderboard(169467)
    def sanctusvector_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_05, Difficulty.NORMAL, lb)
    
    @leaderboard(169468)
    def sanctusvector_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_05, Difficulty.VETERAN, lb)

    @leaderboard(169469)
    def eteocore_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_07, Difficulty.NORMAL, lb)
    
    @leaderboard(169470)
    def eteocore_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_07, Difficulty.VETERAN, lb)

    @leaderboard(169471)
    def guardian2_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_09, Difficulty.NORMAL, lb)
    
    @leaderboard(169472)
    def guardian2_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_09, Difficulty.VETERAN, lb)

    @leaderboard(169473)
    def phexic_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_11, Difficulty.NORMAL, lb)
    
    @leaderboard(169474)
    def phexic_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_11, Difficulty.VETERAN, lb)

    @leaderboard(169475)
    def guardian3_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_13, Difficulty.NORMAL, lb)
    
    @leaderboard(169476)
    def guardian3_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_13, Difficulty.VETERAN, lb)

    @leaderboard(169477)
    def matrix_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_15, Difficulty.NORMAL, lb)
    
    @leaderboard(169478)
    def matrix_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_15, Difficulty.VETERAN, lb)

    @leaderboard(169479)
    def overlord_normal_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_17, Difficulty.NORMAL, lb)
    
    @leaderboard(169480)
    def overlord_veteran_lb(self, lb: Leaderboard):
        chapterTimeTrialLeaderboard(Episode.EPISODE_17, Difficulty.VETERAN, lb)
    
    @leaderboard()
    def pssi_lb(self, lb: Leaderboard):
        pssiescape_lb(lb)

    @leaderboard()
    def pssii_lb(self, lb: Leaderboard):
        pssiisatellite_lb(lb)

if __name__=="__main__":
    MoonSet().save("output/")
