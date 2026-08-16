from pycheevos.core.constants import *
from pycheevos.core.helpers import *
from pycheevos.core.value import MemoryValue
from pycheevos.models.leaderboard import Leaderboard

from memory import Memory

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