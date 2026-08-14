from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    SET_LOGIC_IS_AVAILABLE_ON_HTTPS_GITHUB = byte(0x000000)
    """
    [Notes] [8-bit] Set logic is available on https://github.com/blobdash/RASets/tree/master/Moon
    """

    CURRENT_EPISODE = byte(0x1495bc)
    """
    [8-bit] Current Episode
    // When on main menu and not on level select, gets set to current adventure mode progress
    0x08 = E00
    0x14 = E01
    0x20 = E02
    0x2c = E03
    0x38 = E04
    0x44 = E05
    0x50 = E06
    0x5c = E07
    0x68 = E08
    0x74 = E09
    0x80 = E10
    0x8c = E11
    0x98 = E12
    0xa4 = E13
    0xb0 = E14
    0xbc = E15
    0xc8 = E16
    0xd4 = E17
    """

    CURRENT_DIFFICULTY = dword(0x14fec8)
    """
    [32-bit] Current Difficulty
    0x00 = Rookie
    0x01 = Normal
    0x02 = Veteran
    """

    INPUTS = byte(0x151616)
    """
    [8-bit] [Bitfield] Inputs
    // gets shifted back by 32-bit when in options, otherwise static
    Bit0 = A
    Bit1 = B
    Bit2 = Select
    Bit5 = Dpad Left
    Bit4 = Dpad Right
    Bit6 = Dpad Up
    Bit7 = Dpad Down
    """

    INPUTS_1 = byte(0x151617)
    """
    [8-bit] [Bitfield] Inputs
    // gets shifted back by 32-bit when in options, otherwise static
    Bit0 = R
    Bit1 = L
    Bit2 = X
    Bit3 = Y
    Bit4 = Touch
    """

    GAME_STATE = tbyte(0x151660)
    """
    [24-bit Pointer] Game State
    +0x04: [24-bit Pointer] 
    ++0x01: [8-bit] [Bitfield] Terminals Read
    ++0x04: [32-bit] Total Shots
    ++0x08: [32-bit] Total Hit Shots
    ++0x0C: [32-bit] Current Time
    ++0x30: [32-bit] Timed Events Seconds Remaining
    ++0x34: [32-bit] Timed Events Seconds Framecounter
    +0x190: [24-bit Pointer]
    ++0x30: [32-bit] Current Menu State 
    // Only usable when not ingame
    ... 0x04 = Options
    ... 0x18 = Delete All Data Prompt
    ... 0x2e = Title Screen
    ... 0x56 = Quick Play Level Select
    """

    PLAYER_X = dword(0x16a534)
    """
    [32-bit] Player X
    // likely value from map display, lacking Z axis
    """

    PLAYER_Y = dword(0x16a538)
    """
    [32-bit] Player Y
    // likely value from map display, lacking Z axis
    """

    CURRENT_GAMEMODE = byte(0x207287)
    """
    [8-bit] Current Gamemode
    0x00 = Adventure Mode
    0x01 = Quick Play
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

    HEALTH_HOST = byte(0x2aa770)
    """
    [8-bit] Health Host
    0x3c = Max (no upgrades)
    0x32 = Max (1st upgrade)
    0x28 = Max (2nd)
    0x1e = Max (3rd)
    0x14 = Max (4th)
    0x0a = Max (5th)
    0x00 = Max (6th)
    0x64 = Dead
    """

    HEALTH_LOLA_RR10 = byte(0x2aa771)
    """
    [8-bit] Health LOLA-RR10
    0x19 = Max
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

    LEVEL_EVENTS_E00_PROLOGUE = byte(0x2ab058)
    """
    [8-bit] [Bitfield] Level Events E00 Prologue
    Bit0 = Tried to leave without picking up SAR
    Bit1 = After Health Pack Pickup Event
    Bit2 = Captain Blake Examined
    Bit4 = Tried to go to the wrong door
    """

    LEVEL_EVENTS_E01_PSSI = byte(0x2ab0f0)
    """
    [8-bit] [Bitfield] Level Events E01 PSSI
    Bit0 = Picked Up Canister
    Bit1 = Examined Pvt. Elias Warner
    Bit2 = Got 1st Map Half
    Bit3 = Dialogue after 1st Map Half Discovery
    Bit4 = Muon Pistol Unlock Event
    Bit5 = Picked Up Red Key
    Bit6 = Dialogue after Red Key Pickup
    Bit7 = Got 2nd Map Half
    """

    LEVEL_EVENTS_E01_PSSI_2 = byte(0x2ab0f1)
    """
    [8-bit] [Bitfield] Level Events E01 PSSI #2
    Bit0 = Dialogue after 2nd Map Half Discovery
    Bit4 = 
    Bit5 =
    """

    LAST_LOADED_MOVIE_CUTSCENE_ID = (0x2f05e0)
    """
    [11 bytes ASCII] Last Loaded Movie Cutscene ID
    // all possible values
    ambush
    breveal
    breveal01
    breveal02
    breveal03
    breveal04
    briefing = Before taking SAR (E00)
    briefing2
    buggy
    buggyele01
    buggyele02
    buggyele03
    buggyexit
    chaser
    comdish
    depart = Outro Cutscene after defeating Matrix Progenitor (E15)
    dooropen1
    edeath1
    edeath2
    edeath3
    elevator01 = Going inside PSS I (E00/E01)
    elevator02 = PSS I Level Intro (E01)
    elevator03 = Going outwards from PSS I (E01/E03)
    elevator04
    elevator05
    ereveal1
    explosives
    fin = Outro Cutscene after beating Overlord (E17)
    gdeath01 = Guardian 1 Death Cutscene (E02)
    gdeath02 = Guardian 2 Death Cutscene (E09)
    gdeath03 = Guardian 3 Death Cutscene (E13)
    greveal01 = Guardian 1 Intro Cutscene (E02)
    greveal02 = Guardian 2 Intro Cutscene (E09)
    greveal03 = Guardian 3 Intro Cutscene (E13)
    health = First health pickup (E00)
    idoor
    intro = Game intro (E00)
    ldeath = Matrix Progenitor Death Cutscene (E15)
    lreveal = Matrix Progenitor Intro Cutscene (E15)
    mdeath
    mreveal
    oreveal = Overlord Intro Cutscene (E17)
    rdeath
    redkeyopen
    rreveal
    sdeath = Sanctus Vector Death Cutscene (E05)
    spidertank
    sreveal = Sanctus Vector Intro Cutscene (E05)
    """

    QUICK_PLAY_LEVEL_SELECT_INDEX = byte(0x2f0b76)
    """
    [8-bit] Quick Play Level Select Index
    0x00 = 1st entry
    0x01 = 2nd entry
    0xff = Not in Quick Play
    // paginated : see 0x002f0b7a for page index
    // stays allocated during quick play, gets set to 0xff if out of level select/exited to main menu
    """

    QUICK_PLAY_LEVEL_SELECT_PAGE_INDEX = byte(0x2f0b7a)
    """
    [8-bit] Quick Play Level Select Page Index
    0x01 = Page 1
    0x02 = Page 2
    0x03 = Page 3
    // gets reset to 0x01 if out of quick play, check if selected index = 0xff first
    """

