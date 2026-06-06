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
    
    @achievement(612811)
    def lasso_unlock(self, ach: Achievement):
        ach.add_core(
            weapon_unlock(Weapons_Offsets.LASSO)
        )
    
    @achievement(612812)
    def fusion_unlock(self, ach: Achievement):
        ach.add_core(
            weapon_unlock(Weapons_Offsets.FUSION)
        )
    
    @achievement(612813)
    def eom_unlock(self, ach: Achievement):
        ach.add_core(
            weapon_unlock(Weapons_Offsets.EOM)
        )
    
    @achievement(612814)
    def barrage_unlock(self, ach: Achievement):
        ach.add_core(
            weapon_unlock(Weapons_Offsets.BARRAGE)
        )
    
    @achievement(612844)
    def downtown_megas(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            get_megas_deltas_for_level(Memory.DOWNTOWN_1_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.DOWNTOWN_2_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.DOWNTOWN_3_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.DOWNTOWN_4_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.DOWNTOWN_5_COLLECTIBLES),
            (value(0x0) < 20),
            get_megas_for_level(Memory.DOWNTOWN_1_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_2_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_3_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_4_COLLECTIBLES),
            get_megas_for_level(Memory.DOWNTOWN_5_COLLECTIBLES),
            (measured(value(0x0) == 20))
        ))

    @achievement(612845)
    def underground_megas(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            get_megas_deltas_for_level(Memory.UNDERGROUND_1_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.UNDERGROUND_2_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.UNDERGROUND_3_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.UNDERGROUND_4_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.UNDERGROUND_5_COLLECTIBLES),
            (value(0x0) < 20),
            get_megas_for_level(Memory.UNDERGROUND_1_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_2_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_3_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_4_COLLECTIBLES),
            get_megas_for_level(Memory.UNDERGROUND_5_COLLECTIBLES),
            (measured(value(0x0) == 20))
        ))
    
    @achievement(612846)
    def waterfront_megas(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            get_megas_deltas_for_level(Memory.WATERFRONT_1_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.WATERFRONT_2_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.WATERFRONT_3_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.WATERFRONT_4_COLLECTIBLES),
            get_megas_deltas_for_level(Memory.WATERFRONT_5_COLLECTIBLES),
            (value(0x0) < 20),
            get_megas_for_level(Memory.WATERFRONT_1_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_2_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_3_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_4_COLLECTIBLES),
            get_megas_for_level(Memory.WATERFRONT_5_COLLECTIBLES),
            (measured(value(0x0) == 20))
        ))

    @achievement(612847)
    def museum_megas(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            get_megas_deltas_for_level(Memory.MUSEUM_COLLECTIBLES),
            (value(0x0) < 4),
            get_megas_for_level(Memory.MUSEUM_COLLECTIBLES),
            (measured(value(0x0) == 4))
        ))
    
    @achievement(612848)
    def downtown_films(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            add_source(delta(bit4(Memory.DOWNTOWN_1_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.DOWNTOWN_2_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.DOWNTOWN_3_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.DOWNTOWN_4_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.DOWNTOWN_5_COLLECTIBLES.address))),
            (value(0x0) == 4),
            add_source(bit4(Memory.DOWNTOWN_1_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_2_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_3_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_4_COLLECTIBLES.address)),
            add_source(bit4(Memory.DOWNTOWN_5_COLLECTIBLES.address)),
            (measured(value(0x0) == 5))
        ))
    
    @achievement(612849)
    def underground_films(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            add_source(delta(bit4(Memory.UNDERGROUND_1_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.UNDERGROUND_2_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.UNDERGROUND_3_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.UNDERGROUND_4_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.UNDERGROUND_5_COLLECTIBLES.address))),
            (value(0x0) == 4),
            add_source(bit4(Memory.UNDERGROUND_1_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_2_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_3_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_4_COLLECTIBLES.address)),
            add_source(bit4(Memory.UNDERGROUND_5_COLLECTIBLES.address)),
            (measured(value(0x0) == 5))
        ))

    @achievement(612850)
    def waterfront_films(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            add_source(delta(bit4(Memory.WATERFRONT_1_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.WATERFRONT_2_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.WATERFRONT_3_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.WATERFRONT_4_COLLECTIBLES.address))),
            add_source(delta(bit4(Memory.WATERFRONT_5_COLLECTIBLES.address))),
            (value(0x0) == 4),
            add_source(bit4(Memory.WATERFRONT_1_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_2_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_3_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_4_COLLECTIBLES.address)),
            add_source(bit4(Memory.WATERFRONT_5_COLLECTIBLES.address)),
            (measured(value(0x0) == 5))
        ))
    
    @achievement(612851)
    def museum_film(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            delta(bit4(Memory.MUSEUM_COLLECTIBLES.address)) == 0,
            bit4(Memory.MUSEUM_COLLECTIBLES.address) == 1
        ))

    @achievement(612842)
    def untouchable(self, ach: Achievement):
        ach.add_core([
            (
                # checkpoint hit for entering level
                (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
                (Memory.INGAME_CURRENT_STATUS < 0xfffffffe).with_hits(1)
            ),
            (
                # resetif hp goes down
                and_next((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x0) >> delta(dword(0x10c))) == 0xa000) &
                reset_if((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x0) >> dword(0x10c)) < 0xa000)
            ),
            (
                # resetif exited level
                reset_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe)
            ),
            (
                # trigger if end screen goes from 0 to 1
                trigger(delta(Memory.END_SCREEN_REACHED) == 0x00) &
                trigger(Memory.END_SCREEN_REACHED == 0x01)
            )
        ])
    
    
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
    
    @achievement(612924)
    def all_ingame_achievements(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            add_source(delta(bit0(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit1(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit2(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit3(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit4(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit5(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit6(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit7(Memory.ACHIEVEMENTS.address))),
            add_source(delta(bit0(Memory.ACHIEVEMENTS_1.address))),
            add_source(delta(bit1(Memory.ACHIEVEMENTS_1.address))),
            (value(0x0) < 10),
            add_source(bit0(Memory.ACHIEVEMENTS.address)),
            add_source(bit1(Memory.ACHIEVEMENTS.address)),
            add_source(bit2(Memory.ACHIEVEMENTS.address)),
            add_source(bit3(Memory.ACHIEVEMENTS.address)),
            add_source(bit4(Memory.ACHIEVEMENTS.address)),
            add_source(bit5(Memory.ACHIEVEMENTS.address)),
            add_source(bit6(Memory.ACHIEVEMENTS.address)),
            add_source(bit7(Memory.ACHIEVEMENTS.address)),
            add_source(bit0(Memory.ACHIEVEMENTS_1.address)),
            add_source(bit1(Memory.ACHIEVEMENTS_1.address)),
            (value(0x0) == 10),
        ))

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
        generate_section_tt_lb(range(Levels.DOWNTOWN_1, Levels.DOWNTOWN_5 + 1), lb)

    @leaderboard(163718)
    def underground_section_tt_lb(self, lb: Leaderboard):
        generate_section_tt_lb(range(Levels.UNDERGROUND_1, Levels.UNDERGROUND_5 + 1), lb)

    @leaderboard(163719)
    def waterfront_section_tt_lb(self, lb: Leaderboard):
        generate_section_tt_lb(range(Levels.WATERFRONT_1, Levels.WATERFRONT_5 + 1), lb)
    
    @achievement(614379)
    def destruction_worker_nohit(self, ach: Achievement):
        ach.add_core(
            nohit_boss(Levels.DOWNTOWN_5, BOSS_ARENAS.DESTRUCTION_WORKER)
        )

    @achievement(614380)
    def psycho_delic_nohit(self, ach: Achievement):
        ach.add_core(
            nohit_boss(Levels.UNDERGROUND_5, BOSS_ARENAS.PSYCHO_DELIC)
        )
    
    @achievement(614381)
    def hot_flash_nohit(self, ach: Achievement):
        ach.add_core(
            nohit_boss(Levels.WATERFRONT_5, BOSS_ARENAS.HOT_FLASH)
        )
    
    @achievement(614387)
    def tighthen_nohit(self, ach: Achievement):
        ach.add_core([
            (
                # checkpoint hit for entering level
                (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
                (Memory.INGAME_CURRENT_STATUS == Levels.MUSEUM).with_hits(1)
            ),
            (
                # resetif hp goes down
                and_next((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x0) >> delta(dword(0x10c))) == 0xa000) &
                reset_if((ptr(Memory.ROOT.address) >> ptr(0x64) >> ptr(0x0) >> dword(0x10c)) < 0xa000)
            ),
            (
                # resetif exited level
                reset_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe)
            ),
            (
                # trigger if end screen goes from 0 to 1
                trigger(delta(Memory.END_SCREEN_REACHED) == 0x00) &
                trigger(Memory.END_SCREEN_REACHED == 0x01)
            )
        ])
    
    @achievement(614528)
    def first_upgrade(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            delta(bit2(Memory.ACHIEVEMENTS.address)) == 0,
            bit2(Memory.ACHIEVEMENTS.address) == 1
        ))
    
    @achievement(614523)
    def blaster_mk3(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            Weapons.BLASTER.reachedLevel(3)
        ))
    
    @achievement(614524)
    def lasso_mk3(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            Weapons.LASSO.reachedLevel(3)
        ))
    
    @achievement(614525)
    def fusion_mk3(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            Weapons.FUSION.reachedLevel(3)
        ))
    
    @achievement(614526)
    def eom_mk3(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            Weapons.EOM.reachedLevel(3)
        ))
    
    @achievement(614527)
    def barrage_mk3(self, ach: Achievement):
        ach.add_core(group(
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe),
            Weapons.BARRAGE.reachedLevel(3)
        ))
    
    @achievement(614636)
    def melee_only(self, ach: Achievement):
        ach.add_core(group(
            # checkpoint hit for entering level
            (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
            (Memory.INGAME_CURRENT_STATUS < 0xfffffffe).with_hits(1),
            # resetif any ammo is consumed
            reset_if(Weapons.BLASTER.ammoConsumed()),
            reset_if(Weapons.LASSO.ammoConsumed()),
            reset_if(Weapons.FUSION.ammoConsumed()),
            reset_if(Weapons.EOM.ammoConsumed()),
            reset_if(Weapons.BARRAGE.ammoConsumed()),
            # resetif exited level
            reset_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe),
            # trigger on level exit
            (
                trigger(delta(Memory.END_SCREEN_REACHED) == 0x00) &
                trigger(Memory.END_SCREEN_REACHED == 0x01)
            )
        ))
    
    @achievement(614637)
    def museum_base_loadout(self, ach: Achievement):
        ach.add_core(group(
            # checkpoint hit for entering level
            (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
            (Memory.INGAME_CURRENT_STATUS == Levels.MUSEUM).with_hits(1),
            # resetif lasso used more than once
            reset_if((ptr(Memory.ROOT.address)
                    >> delta(dword(0x64)) != 0) &
                (ptr(Memory.ROOT.address)
                >> ptr(0x64)
                >> ptr(0x00)
                >> ptr(0x2E8)
                >> ptr(0x1C)
                >> ptr(Weapons_Offsets.LASSO)
                >> delta(dword(0x48)) > dword(0x48)).with_hits(2)),
            # resetif weapons other than blaster/melee/lasso used
            reset_if(Weapons.FUSION.ammoConsumed()),
            reset_if(Weapons.EOM.ammoConsumed()),
            reset_if(Weapons.BARRAGE.ammoConsumed()),
            # resetif exited level
            reset_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe),
            # trigger if end screen goes from 0 to 1
            trigger(delta(Memory.END_SCREEN_REACHED) == 0x00) &
            trigger(Memory.END_SCREEN_REACHED == 0x01)
        ))
    
    @achievement(614638)
    def museum_speedrun(self, ach: Achievement):
        ach.add_core(group(
            # checkpoint hit for entering level
            (delta(Memory.INGAME_CURRENT_STATUS) == 0xfffffffe) &
            (Memory.INGAME_CURRENT_STATUS == Levels.MUSEUM).with_hits(1),
            # resetif exited level
            reset_if(Memory.INGAME_CURRENT_STATUS >= 0xfffffffe),
            # resetif timer expired
            reset_if((Memory.PAUSED_STATE == 0x00) & (Memory.INGAME_CURRENT_STATUS < 0xfffffffe).with_hits(speedrun_hits(5, 30))),
            # trigger if end screen goes from 0 to 1
            trigger(delta(Memory.END_SCREEN_REACHED) == 0x00) &
            trigger(Memory.END_SCREEN_REACHED == 0x01)
        ))
    
    @achievement(614639)
    def downtown_section_speedrun(self, ach: Achievement):
        ach.add_core(
            generate_section_tt_ach(range(Levels.DOWNTOWN_1, Levels.DOWNTOWN_5 + 1), 28, 0)
        )

    @achievement(614640)
    def underground_section_speedrun(self, ach: Achievement):
        ach.add_core(
            generate_section_tt_ach(range(Levels.UNDERGROUND_1, Levels.UNDERGROUND_5 + 1), 40, 0)
        )

    @achievement(614641)
    def waterfront_section_speedrun(self, ach: Achievement):
        ach.add_core(
            generate_section_tt_ach(range(Levels.WATERFRONT_1, Levels.WATERFRONT_5 + 1), 42, 0)
        )

if __name__=="__main__":
    MegamindSet().save("output/")
