from pycheevos.core.condition import ConditionList
from types import NoneType
from pycheevos.core.constants import *
from pycheevos.core.helpers import *
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

from memory import Memory

FRAMERATE = 60

class Episode:
  EPISODE_00 = 0x08
  EPISODE_01 = 0x14
  EPISODE_02 = 0x20
  EPISODE_03 = 0x2c
  EPISODE_04 = 0x38
  EPISODE_05 = 0x44
  EPISODE_06 = 0x50
  EPISODE_07 = 0x5c
  EPISODE_08 = 0x68
  EPISODE_09 = 0x74
  EPISODE_10 = 0x80
  EPISODE_11 = 0x8c
  EPISODE_12 = 0x98
  EPISODE_13 = 0xa4
  EPISODE_14 = 0xb0
  EPISODE_15 = 0xbc
  EPISODE_16 = 0xc8
  EPISODE_17 = 0xd4
  VR_1 = 0xe0
  VR_2 = 0xec
  VR_3 = 0xf8
  VR_4 = 0x04
  VR_5 = 0x10
  VR_6 = 0x1c

class SaveData:
  ROOKIESLOT: MemoryValue
  NORMALSLOT: MemoryValue
  VETERANSLOT: MemoryValue
  
  def __init__(self, rookieslot: MemoryValue, normalslot: MemoryValue, veteranslot: MemoryValue):
    self.ROOKIESLOT = rookieslot
    self.NORMALSLOT = normalslot
    self.VETERANSLOT = veteranslot

  def firstClear(self):
    return group(
      (and_next(delta(self.ROOKIESLOT) == 0)), or_next(self.ROOKIESLOT != 0),
      (and_next(delta(self.NORMALSLOT) == 0)), or_next(self.NORMALSLOT != 0),
      (and_next(delta(self.VETERANSLOT) == 0)), self.VETERANSLOT != 0,
    )
  
  def firstClearDifficulty(self, difficulty: int):
    match difficulty:
      case 0:
        return ((delta(self.ROOKIESLOT) == 0) & (self.ROOKIESLOT != 0))
      case 1:
        return ((delta(self.NORMALSLOT) == 0) & (self.NORMALSLOT != 0))
      case 2:
        return ((delta(self.VETERANSLOT) == 0) & (self.VETERANSLOT != 0))

class EpisodeSaveData:
  EPISODE_00 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_PROLOGUE, 
    Memory.SAVE_DATA_FOR_NORMAL_PROLOGUE, 
    Memory.SAVE_DATA_FOR_VETERAN_PROLOGUE
  )
  EPISODE_01 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_PSS_I, 
    Memory.SAVE_DATA_FOR_NORMAL_PSS_I, 
    Memory.SAVE_DATA_FOR_VETERAN_PSS_I
  )
  EPISODE_02 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_GUARDIAN_I, 
    Memory.SAVE_DATA_FOR_NORMAL_GUARDIAN_I, 
    Memory.SAVE_DATA_FOR_VETERAN_GUARDIAN_I
  )
  EPISODE_03 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_PSS_I_ESCAPE, 
    Memory.SAVE_DATA_FOR_NORMAL_PSS_I_ESCAPE, 
    Memory.SAVE_DATA_FOR_VETERAN_PSS_I_ESCAPE
  )
  EPISODE_04 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_PSS_II, 
    Memory.SAVE_DATA_FOR_NORMAL_PSS_II, 
    Memory.SAVE_DATA_FOR_VETERAN_PSS_II
  )
  EPISODE_05 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_SANCTUS_VECTOR, 
    Memory.SAVE_DATA_FOR_NORMAL_SANCTUS_VECTOR, 
    Memory.SAVE_DATA_FOR_VETERAN_SANCTUS_VECTOR
  )
  EPISODE_06 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_EXIT_PSS_II, 
    Memory.SAVE_DATA_FOR_NORMAL_EXIT_PSS_II, 
    Memory.SAVE_DATA_FOR_VETERAN_EXIT_PSS_II
  )
  EPISODE_07 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_NON_ETEO_TRANSPORT_VESSEL, 
    Memory.SAVE_DATA_FOR_NORMAL_NON_ETEO_TRANSPORT_VESSEL, 
    Memory.SAVE_DATA_FOR_VETERAN_NON_ETEO_TRANSPORT_VESSEL
  )
  EPISODE_08 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_WASTE_DISPOSAL, 
    Memory.SAVE_DATA_FOR_NORMAL_WASTE_DISPOSAL, 
    Memory.SAVE_DATA_FOR_VETERAN_WASTE_DISPOSAL
  )
  EPISODE_09 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_GUARDIAN_II, 
    Memory.SAVE_DATA_FOR_NORMAL_GUARDIAN_II, 
    Memory.SAVE_DATA_FOR_VETERAN_GUARDIAN_II
  )
  EPISODE_10 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_POWER_STATION, 
    Memory.SAVE_DATA_FOR_NORMAL_POWER_STATION, 
    Memory.SAVE_DATA_FOR_VETERAN_POWER_STATION
  )
  EPISODE_11 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_PHEXIC_MANIFOLD,
    Memory.SAVE_DATA_FOR_NORMAL_PHEXIC_MANIFOLD, 
    Memory.SAVE_DATA_FOR_VETERAN_PHEXIC_MANIFOLD
  )
  EPISODE_12 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_COLD_PROCESS, 
    Memory.SAVE_DATA_FOR_NORMAL_COLD_PROCESS, 
    Memory.SAVE_DATA_FOR_VETERAN_COLD_PROCESS
  )
  EPISODE_13 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_GUARDIAN_III, 
    Memory.SAVE_DATA_FOR_NORMAL_GUARDIAN_III, 
    Memory.SAVE_DATA_FOR_VETERAN_GUARDIAN_III
  )
  EPISODE_14 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_IRRADIATED_STRATUM, 
    Memory.SAVE_DATA_FOR_NORMAL_IRRADIATED_STRATUM, 
    Memory.SAVE_DATA_FOR_VETERAN_IRRADIATED_STRATUM
  )
  EPISODE_15 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_MATRIX_PROGENITOR, 
    Memory.SAVE_DATA_FOR_NORMAL_MATRIX_PROGENITOR, 
    Memory.SAVE_DATA_FOR_VETERAN_MATRIX_PROGENITOR
  )
  EPISODE_16 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_FERMIAN_HOMEWORLD, 
    Memory.SAVE_DATA_FOR_NORMAL_FERMIAN_HOMEWORLD, 
    Memory.SAVE_DATA_FOR_VETERAN_FERMIAN_HOMEWORLD
  )
  EPISODE_17 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_OVERLORD, 
    Memory.SAVE_DATA_FOR_NORMAL_OVERLORD, 
    Memory.SAVE_DATA_FOR_VETERAN_OVERLORD
  )
  VR_1 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_VR_TRAINING_1, 
    Memory.SAVE_DATA_FOR_NORMAL_VR_TRAINING_1, 
    Memory.SAVE_DATA_FOR_VETERAN_VR_TRAINING_1
  )
  VR_2 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_VR_TRAINING_2, 
    Memory.SAVE_DATA_FOR_NORMAL_VR_TRAINING_2, 
    Memory.SAVE_DATA_FOR_VETERAN_VR_TRAINING_2
  )
  VR_3 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_VR_TRAINING_3, 
    Memory.SAVE_DATA_FOR_NORMAL_VR_TRAINING_3, 
    Memory.SAVE_DATA_FOR_VETERAN_VR_TRAINING_3
  )
  VR_4 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_VR_TRAINING_4, 
    Memory.SAVE_DATA_FOR_NORMAL_VR_TRAINING_4, 
    Memory.SAVE_DATA_FOR_VETERAN_VR_TRAINING_4
  )
  VR_5 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_VR_TRAINING_5, 
    Memory.SAVE_DATA_FOR_NORMAL_VR_TRAINING_5, 
    Memory.SAVE_DATA_FOR_VETERAN_VR_TRAINING_5
  )
  VR_6 = SaveData(
    Memory.SAVE_DATA_FOR_ROOKIE_VR_TRAINING_6, 
    Memory.SAVE_DATA_FOR_NORMAL_VR_TRAINING_6, 
    Memory.SAVE_DATA_FOR_VETERAN_VR_TRAINING_6
  )
  

class Gamemode:
  ADVENTURE = 0x00
  QUICKPLAY = 0x01

class Difficulty:
  ROOKIE = 0x00
  NORMAL = 0x01
  VETERAN = 0x02

class Weapon:
  AMMO: MemoryValue
  AMMO_RESERVE: MemoryValue | None
  UNLOCKED: MemoryValue

  def __init__(self, ammoaddr: MemoryValue, reserveaddr: MemoryValue | None, unlockbit: MemorySize) -> None:
        self.AMMO = ammoaddr
        self.AMMO_RESERVE = reserveaddr
        self.UNLOCKED = MemoryValue(Memory.WEAPON_UNLOCKS.address, unlockbit)
  
  def unlocked(self, episode: int):
    return group(
      (Memory.CURRENT_EPISODE == episode),
      (Memory.PLAY_STATE == 0x00),
      adventure_mode(),
      delta(self.UNLOCKED) == 0,
      self.UNLOCKED == 1
    )

class Weapons:
  SAR = Weapon(
    Memory.SAR_AMMO, 
    None, 
    MemorySize.BIT0
  )
  MUON = Weapon(
    Memory.MUON_PISTOL_AMMO, 
    Memory.MUON_PISTOL_RESERVE_AMMO, 
    MemorySize.BIT2
  )
  QUANTA = Weapon(
    Memory.QUANTA_RIFLE_AMMO, 
    Memory.QUANTA_RIFLE_RESERVE_AMMO, 
    MemorySize.BIT3
  )
  FERMION = Weapon(
    Memory.FERMION_SNIPER_AMMO, 
    Memory.FERMION_SNIPER_RESERVE_AMMO, 
    MemorySize.BIT4
  )
  LEPTON = Weapon(
    Memory.LEPTON_SPREAD_AMMO, 
    Memory.LEPTON_SPREAD_RESERVE_AMMO, 
    MemorySize.BIT5
  )
  OXID = Weapon(
    Memory.OXID_CANNON_AMMO, 
    Memory.OXID_CANNON_RESERVE_AMMO, 
    MemorySize.BIT6
  )
  SEEKER = Weapon(
    Memory.SEEKER_PODS_AMMO, 
    Memory.SEEKER_PODS_RESERVE_AMMO, 
    MemorySize.BIT7
  )


def ptr(value):
  return tbyte(value)

def adventure_mode():
  return (Memory.QUICK_PLAY_LEVEL_SELECT_INDEX == 0xff)

def quick_play():
  return (Memory.QUICK_PLAY_LEVEL_SELECT_INDEX != 0xff)

def enter_end_screen():
  return group(
    (delta(bit2(Memory.END_SCREEN.address)) == 0x00),
    (bit2(Memory.END_SCREEN.address) == 0x01),
  )

def enter_end_screen_trigger():
  return group(
    (delta(bit2(Memory.END_SCREEN.address)) == 0x00),
    (trigger(bit2(Memory.END_SCREEN.address) == 0x01)),
  )

def is_ingame():
  return group(
    Memory.GAME_STATE != 0x00,
    Memory.POINTER_TO_LAST_ACCESSED_DIALOGUE_SCRIPT != 0
  )

def is_not_ingame():
  return (Memory.POINTER_TO_LAST_ACCESSED_DIALOGUE_SCRIPT == 0)

def clearedChapter(episode: int, difficulty: int | NoneType = None):
  cond = group(
    is_ingame(),
    (Memory.CURRENT_EPISODE == episode),
    enter_end_screen(),
    adventure_mode()
  )
  if(difficulty is not None):
    cond.append(Memory.CURRENT_DIFFICULTY == difficulty)
  return cond

def chapterTimeTrial(episode: int, minutes: int, seconds: int):
  return group(
    is_ingame(),
    quick_play(),
    (Memory.CURRENT_EPISODE == episode),
    (Memory.CURRENT_DIFFICULTY == 0x01),
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x03),
    enter_end_screen_trigger(),
    # timer is above number of frames allowed for tt
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x0c) <= frames(minutes, seconds))
  )

def chapterTimeTrialLeaderboard(episode: int, difficulty: int, lb: Leaderboard):
  lb.format = LeaderboardFormat.FRAMES
  lb.lower_is_better = True
  lb.add_start(
    group(
      is_ingame(),
      (Memory.CURRENT_EPISODE == episode),
      (Memory.CURRENT_DIFFICULTY == difficulty),
      (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x03),
      enter_end_screen()
    )
  )
  lb.add_cancel(
    always_false()
  )
  lb.add_submit(
    always_true()
  )
  lb.add_value(
    measured(ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x0c))
  )

def timer_display(lb: Leaderboard):
  lb.format = LeaderboardFormat.FRAMES
  lb.add_start(
    group(
      reset_if(bit2(Memory.INPUTS.address) == 0x00),
      reset_if(bit0(Memory.INPUTS_1.address) == 0x00),
      reset_if(bit1(Memory.INPUTS_1.address) == 0x00),
      (bit2(Memory.INPUTS.address) == 0x01) &
      (bit0(Memory.INPUTS_1.address) == 0x01) &
      (bit1(Memory.INPUTS_1.address) == 0x01).with_hits(260)
    )
  )
  lb.add_cancel(
    group(
      reset_if(bit2(Memory.INPUTS.address) == 0x00),
      reset_if(bit0(Memory.INPUTS_1.address) == 0x00),
      reset_if(bit1(Memory.INPUTS_1.address) == 0x00),
      (bit2(Memory.INPUTS.address) == 0x01) &
      (bit0(Memory.INPUTS_1.address) == 0x01) &
      (bit1(Memory.INPUTS_1.address) == 0x01).with_hits(360)
    )
  )
  lb.add_submit(
    always_false()
  )
  lb.add_value(
    measured(ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x0c))
  )

def sanctus_healchallenge(seconds: int):
  return group(
    is_ingame(),
    quick_play(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_05),
    (Memory.CURRENT_DIFFICULTY == 0x01),
    enter_end_screen(),
    reset_next_if(group(
      (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> delta(dword(0x10)) == 0x03) &
      (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x00)
    )),
    # only count hits when on the boss map, avoids hits during loads/room transitions
    and_next(string_equals(Memory.CURRENT_AREA_ID, 'a1', 2, endianness='little')),
    and_next(string_equals(Memory.CURRENT_SUBMAP_ID, '016', 3, endianness='little')),
    # only count hits after boss health is initialized
    and_next(Memory.BOSS_HEALTH_STATIC_COPY != 0xffff),
    # boss regains 1hp every 20 frames, meaning 3 hp per second.
    (delta(Memory.BOSS_HEALTH_STATIC_COPY) < Memory.BOSS_HEALTH_STATIC_COPY).with_hits(seconds*3)
  )

def phexic_accchallenge(accuracy: int):
  return group(
    is_ingame(),
    quick_play(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_11),
    (Memory.CURRENT_DIFFICULTY == 0x01),
    enter_end_screen_trigger(),
    # hit shots * 100
    remember((ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x08)) * 100),
    add_address(ptr(Memory.GAME_STATE.address) >> ptr(0x04)),
    # (hit shots * 100) / total shots (toolkit rounds down, just like the game)
    remember(recall() /  dword(0x04)),
    # (calculated accuracy >= req. accuracy)
    (recall() >= accuracy)
  )

def pssitrial(seconds: int):
  return group(
    is_ingame(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_03),
    (bit0(Memory.LEVEL_EVENTS_E03.address) == 0x01),
    (delta(bit1(Memory.LEVEL_EVENTS_E03.address)) == 0x00),
    (trigger(bit1(Memory.LEVEL_EVENTS_E03.address) == 0x01)),
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x30) >= seconds)
  )

def pssiisatellitetrial(seconds: int):
  return group(
    is_ingame(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_06),
    (bit3(Memory.LEVEL_EVENTS_E06_E08.address) == 0x01),
    (delta(bit1(Memory.LEVEL_EVENTS_E06_E08.address)) == 0x00),
    (trigger(bit1(Memory.LEVEL_EVENTS_E06_E08.address) == 0x01)),
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x30) >= seconds)
  )

def pssiescape_lb(lb: Leaderboard):
  lb.format = LeaderboardFormat.SECS
  lb.add_start(
    group(
      is_ingame(),
      (Memory.CURRENT_EPISODE == Episode.EPISODE_03),
      (bit0(Memory.LEVEL_EVENTS_E03.address) == 0x01),
      (delta(bit1(Memory.LEVEL_EVENTS_E03.address)) == 0x00),
      (bit1(Memory.LEVEL_EVENTS_E03.address) == 0x01)
    )
  )
  lb.add_cancel(
    always_false()
  )
  lb.add_submit(
    always_true()
  )
  lb.add_value(
    measured(ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x30))
  )

def pssiisatellite_lb(lb: Leaderboard):
  lb.format = LeaderboardFormat.SECS
  lb.add_start(
    group(
      is_ingame(),
      (Memory.CURRENT_EPISODE == Episode.EPISODE_06),
      (bit3(Memory.LEVEL_EVENTS_E06_E08.address) == 0x01),
      (delta(bit1(Memory.LEVEL_EVENTS_E06_E08.address)) == 0x00),
      (bit1(Memory.LEVEL_EVENTS_E06_E08.address) == 0x01)
    )
  )
  lb.add_cancel(
    always_false()
  )
  lb.add_submit(
    always_true()
  )
  lb.add_value(
    measured(ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x30))
  )

def all_hp():
  return group(
    measured_if(Memory.GAME_STATE != 0x00),
    measured_if(Memory.POINTER_TO_LAST_ACCESSED_DIALOGUE_SCRIPT != 0),
    measured_if(adventure_mode()),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_15),
    (string_equals(Memory.CURRENT_AREA_ID, 'a5', 2, endianness='little')),
    (string_equals(Memory.CURRENT_SUBMAP_ID, '016', 3, endianness='little')),
    (delta(bitcount(Memory.HEALTH_UPGRADES.address)) == 5),
    measured(bitcount(Memory.HEALTH_UPGRADES.address) == 6)
  )

def all_ammo():
  return group(
    measured_if(Memory.GAME_STATE != 0x00),
    measured_if(Memory.POINTER_TO_LAST_ACCESSED_DIALOGUE_SCRIPT != 0),
    measured_if(adventure_mode()),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_15),
    (string_equals(Memory.CURRENT_AREA_ID, 'a1', 2, endianness='little')),
    (string_equals(Memory.CURRENT_SUBMAP_ID, '017', 3, endianness='little')),
    (delta(bitcount(Memory.AMMO_CLIP_UPGRADES.address)) == 3),
    measured(bitcount(Memory.AMMO_CLIP_UPGRADES.address) == 4)
  )

def vr_training():
  return group(
    is_ingame(),
    enter_end_screen(),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_1),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_2),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_3),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_4),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_5),
    (Memory.CURRENT_EPISODE == Episode.VR_6),
    or_next(EpisodeSaveData.VR_1.ROOKIESLOT != 0),
    or_next(EpisodeSaveData.VR_1.NORMALSLOT != 0),
    and_next(EpisodeSaveData.VR_1.VETERANSLOT != 0),
    or_next(EpisodeSaveData.VR_2.ROOKIESLOT != 0),
    or_next(EpisodeSaveData.VR_2.NORMALSLOT != 0),
    and_next(EpisodeSaveData.VR_2.VETERANSLOT != 0),
    or_next(EpisodeSaveData.VR_3.ROOKIESLOT != 0),
    or_next(EpisodeSaveData.VR_3.NORMALSLOT != 0),
    and_next(EpisodeSaveData.VR_3.VETERANSLOT != 0),
    or_next(EpisodeSaveData.VR_4.ROOKIESLOT != 0),
    or_next(EpisodeSaveData.VR_4.NORMALSLOT != 0),
    and_next(EpisodeSaveData.VR_4.VETERANSLOT != 0),
    or_next(EpisodeSaveData.VR_5.ROOKIESLOT != 0),
    or_next(EpisodeSaveData.VR_5.NORMALSLOT != 0),
    and_next(EpisodeSaveData.VR_5.VETERANSLOT != 0),
    or_next(EpisodeSaveData.VR_6.ROOKIESLOT != 0),
    or_next(EpisodeSaveData.VR_6.NORMALSLOT != 0),
    EpisodeSaveData.VR_6.VETERANSLOT != 0,
  )

def vr_training_veteran():
  return group(
    is_ingame(),
    enter_end_screen(),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_1),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_2),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_3),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_4),
    or_next(Memory.CURRENT_EPISODE == Episode.VR_5),
    (Memory.CURRENT_EPISODE == Episode.VR_6),
    and_next(EpisodeSaveData.VR_1.VETERANSLOT != 0),
    and_next(EpisodeSaveData.VR_2.VETERANSLOT != 0),
    and_next(EpisodeSaveData.VR_3.VETERANSLOT != 0),
    and_next(EpisodeSaveData.VR_4.VETERANSLOT != 0),
    and_next(EpisodeSaveData.VR_5.VETERANSLOT != 0),
    EpisodeSaveData.VR_6.VETERANSLOT != 0,
  )

def frames(min: int, seconds: int):
  return ((min * 60) + seconds) * FRAMERATE