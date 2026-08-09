from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    SET_LOGIC_IS_AVAILABLE_ON_HTTPS_GITHUB = byte(0x000000)
    """
    [Notes] [8-bit] Set logic is available on https://github.com/blobdash/RASets/tree/master/Moon
    """

    CURRENT_DIFFICULTY = dword(0x14fec8)
    """
    [32-bit] Current Difficulty
    0x00 = Rookie
    0x01 = Normal
    0x02 = Veteran
    """

    GAME_STATE = tbyte(0x151660)
    """
    [24-bit Pointer] Game State
    +0x04: [24-bit pointer] 
    ++0x01: [8-bit] [Bitfield] Terminals Read
    ++0x04: [32-bit] Total Shots
    ++0x08: [32-bit] Total Hit Shots
    ++0x0C: [32-bit] Current Time
    """

    CURRENT_AREA_ID = (0x2aa758)
    """
    [2 bytes ASCII] Current Area ID
    """

    CURRENT_SUBMAP_ID = (0x2aa75b)
    """
    [3 bytes ASCII] Current Submap ID
    """

    LAST_ENTRANCE_ID = (0x2aa760)
    """
    [11 bytes ASCII] Last Entrance ID
    """

    HEALTH_HOST = word(0x2aa770)
    """
    [16-bit] Health Host
    0x3c = Max
    0x64 = Dead
    """

    HEALTH_RAD = byte(0x2aa772)
    """
    [8-bit] Health RAD
    0x19 = Max
    0x64 = Dead
    0x00 = RAD not deployed
    """

    SELECTED_WEAPON = byte(0x2aa773)
    """
    [8-bit] Selected weapon
    0x00 = SAR
    0x24 = Controlling RAD
    0x48 = Muon
    0x6c = Quanta
    0x90 = Fermion
    0xb4 = Lepton
    0xd8 = Oxid Cannon
    0xfc = Seeker Pods
    """

    SAR_AMMO = byte(0x2aa774)
    """
    [8-bit] SAR Ammo
    0x64 = Max
    0x00 = Min
    // Infinite ammo weapon. There still exists a counter for some reason.
    """

    RAD_AMMO = byte(0x2aa775)
    """
    [8-bit] RAD Ammo
    0x08 = Max
    """

    QUANTA_RIFLE_AMMO = byte(0x2aa776)
    """
    [8-bit] Quanta Rifle Ammo
    """

    QUANTA_RIFLE_RESERVE_AMMO = byte(0x2aa777)
    """
    [8-bit] Quanta Rifle Reserve Ammo
    0xc0 = Max Reserve
    """

    MUON_PISTOL_AMMO = byte(0x2aa778)
    """
    [8-bit] Muon Pistol Ammo
    """

    MUON_PISTOL_RESERVE_AMMO = byte(0x2aa779)
    """
    [8-bit] Muon Pistol Reserve Ammo
    0x50 = Max Reserve
    """

    LEPTON_SPREAD_RESERVE_AMMO = byte(0x2aa77a)
    """
    [8-bit] Lepton Spread Reserve Ammo
    0x20 = Max Reserve
    """

    LEPTON_SPREAD_AMMO = byte(0x2aa77b)
    """
    [8-bit] Lepton Spread Ammo
    """

    FERMION_SNIPER_RESERVE_AMMO = byte(0x2aa77c)
    """
    [8-bit] Fermion Sniper Reserve Ammo
    0x10 = Max Reserve
    """

    FERMION_SNIPER_AMMO = byte(0x2aa77d)
    """
    [8-bit] Fermion Sniper Ammo
    """

    OXID_CANNON_RESERVE_AMMO = byte(0x2aa77e)
    """
    [8-bit] Oxid Cannon Reserve Ammo
    0x18 = Max Reserve
    """

    OXID_CANNON_AMMO = byte(0x2aa77f)
    """
    [8-bit] Oxid Cannon Ammo
    """

    SEEKER_PODS_RESERVE_AMMO = byte(0x2aa780)
    """
    [8-bit] Seeker Pods Reserve Ammo
    0x0c = Max Reserve
    """

    SEEKER_PODS_AMMO = byte(0x2aa781)
    """
    [8-bit] Seeker Pods Ammo
    """

    ROOM_WHERE_RAD_IS = (0x2aa788)
    """
    [6 bytes ASCII] Room where RAD is
    First byte = 0x00 when not deployed
    """

    WEAPON_UNLOCKS = byte(0x2aa7a8)
    """
    [8-bit] [Bitfield] Weapon Unlocks
    Bit0 = SAR
    Bit1 = RAD
    Bit2 = Muon Pistol
    Bit3 = Quanta Rifle
    Bit4 = Fermion Sniper
    Bit5 = Lepton Spread
    Bit6 = Oxid Cannon
    Bit7 = Seeker Pods
    """

    HEALTH_UPGRADES = byte(0x2aa7a9)
    """
    [8-bit] [Bitfield] Health Upgrades
    Bit0 = Upgrade 1
    Bit1 = Upgrade 2
    Bit2 = Upgrade 3
    Bit3 = Upgrade 4
    Bit4 = Upgrade 5
    Bit5 = Upgrade 6
    """

    BIT5 = byte(0x2ab03b)
    """
    [8-bit] [Bitfield]
    Bit5 = Timed Section Active
    """

    TIMED_SECTIONS_SECONDS_REMAINING = dword(0x2ab068)
    """
    [32-bit] Timed Sections - Seconds Remaining
    """

