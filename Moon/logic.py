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
      (Memory.CURRENT_GAMEMODE == 0x00),
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

def clearedChapter(episode: int, map: str, subarea: str, gamemode = None, difficulty = None):
  cond = group(
    (Memory.CURRENT_EPISODE == episode),
    (delta(Memory.END_SCREEN) == 0x00),
    (Memory.END_SCREEN == 0x07),
    (string_equals(Memory.CURRENT_AREA_ID, map, 2, endianness='little')),
    (string_equals(Memory.CURRENT_SUBMAP_ID, subarea, 3, endianness='little'))
  )
  if(gamemode is not None):
    cond.append((Memory.CURRENT_GAMEMODE == gamemode))
  if(difficulty is not None):
    cond.append(Memory.CURRENT_DIFFICULTY == difficulty)
  return cond

def chapterTimeTrial(episode: int, minutes: int, seconds: int):
  return group(
    (Memory.CURRENT_EPISODE == episode),
    (Memory.CURRENT_DIFFICULTY >= 0x01),
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
    (Memory.CURRENT_EPISODE != episode) |
    (Memory.CURRENT_DIFFICULTY != difficulty) |
    (ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x10) == 0x00)
  )
  lb.add_submit(
    always_true()
  )
  lb.add_value(
    measured(ptr(Memory.GAME_STATE.address) >> ptr(0x04) >> dword(0x0c))
  )

def sanctus_healchallenge(seconds: int):
  return group(
    (Memory.CURRENT_EPISODE == Episode.EPISODE_05),
    (Memory.CURRENT_DIFFICULTY >= 0x01),
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
    pause_if(delta(Memory.BOSS_HEALTH_STATIC_COPY) < Memory.BOSS_HEALTH_STATIC_COPY).with_hits(seconds*3)
  )

def frames(min: int, seconds: int):
  return ((min * 60) + seconds) * FRAMERATE