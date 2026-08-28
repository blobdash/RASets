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

def clearedChapter(episode: int, map: str, subarea: str, gamemode: int | NoneType = None, difficulty: int | NoneType = None):
  cond = group(
    (Memory.CURRENT_EPISODE == episode),
    (delta(Memory.END_SCREEN) == 0x00),
    (Memory.END_SCREEN == 0x07),
    (string_equals(Memory.CURRENT_AREA_ID, map, 2, endianness='little')),
    (string_equals(Memory.CURRENT_SUBMAP_ID, subarea, 3, endianness='little')),
    adventure_mode()
  )
  if(difficulty is not None):
    cond.append(Memory.CURRENT_DIFFICULTY == difficulty)
  return cond

def chapterTimeTrial(episode: int, minutes: int, seconds: int):
  return group(
    quick_play(),
    (Memory.CURRENT_EPISODE == episode),
    (Memory.CURRENT_DIFFICULTY == 0x01),
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x03),
    (delta(Memory.END_SCREEN) == 0x00),
    (trigger(Memory.END_SCREEN == 0x07)),
    # pauseif timer is above number of frames allowed for tt
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x0c) <= frames(minutes, seconds))
  )

def chapterTimeTrialLeaderboard(episode: int, difficulty: int, lb: Leaderboard):
  lb.format = LeaderboardFormat.FRAMES
  lb.lower_is_better = True
  lb.add_start(
    group(
      (Memory.CURRENT_EPISODE == episode),
      (Memory.CURRENT_DIFFICULTY == difficulty),
      (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x03),
      (delta(Memory.END_SCREEN) == 0x00),
      (Memory.END_SCREEN == 0x07)
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
    quick_play(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_05),
    (Memory.CURRENT_DIFFICULTY == 0x01),
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x03),
    (delta(Memory.END_SCREEN) == 0x00),
    (trigger(Memory.END_SCREEN == 0x07)),
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
    quick_play(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_11),
    (Memory.CURRENT_DIFFICULTY == 0x01),
    (delta(Memory.END_SCREEN) == 0x00),
    (Memory.END_SCREEN == 0x07),
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
    (Memory.CURRENT_EPISODE == Episode.EPISODE_03),
    (bit0(Memory.LEVEL_EVENTS_E03.address) == 0x01),
    (delta(bit1(Memory.LEVEL_EVENTS_E03.address)) == 0x00),
    (trigger(bit1(Memory.LEVEL_EVENTS_E03.address) == 0x01)),
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x30) >= seconds)
  )

def pssiisatellitetrial(seconds: int):
  return group(
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
    adventure_mode(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_15),
    (string_equals(Memory.CURRENT_AREA_ID, 'a5', 2, endianness='little')),
    (string_equals(Memory.CURRENT_SUBMAP_ID, '016', 3, endianness='little')),
    (delta(bitcount(Memory.HEALTH_UPGRADES.address)) == 5),
    (bitcount(Memory.HEALTH_UPGRADES.address) == 6)
  )

def all_ammo():
  return group(
    adventure_mode(),
    (Memory.CURRENT_EPISODE == Episode.EPISODE_15),
    (string_equals(Memory.CURRENT_AREA_ID, 'a1', 2, endianness='little')),
    (string_equals(Memory.CURRENT_SUBMAP_ID, '017', 3, endianness='little')),
    (delta(bitcount(Memory.AMMO_CLIP_UPGRADES.address)) == 3),
    (bitcount(Memory.AMMO_CLIP_UPGRADES.address) == 4)
  )

def frames(min: int, seconds: int):
  return ((min * 60) + seconds) * FRAMERATE