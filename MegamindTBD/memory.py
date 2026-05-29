from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    INGAME_CURRENT_STATUS = dword(0x083154)
    """
    [32-bit] Ingame + Current Status
    0xffffffff = Not Ingame
    0xfffffffe = Loading (in/out of level)
    Anything else is level ID :
    3-7 = Downtown 1 to 5
    8 = Museum
    9-13 = Underground 1 to 5
    14-18 = Waterfront 1 to 5
    """

    ROOT = dword(0x08a000)
    """
    [32-bit Pointer] Root (null when not ingame)
    +0x64: [32-bit Pointer]
    ++0x00: [32-bit Pointer] Player Struct
    +++0x48 [32-bit Pointer] ???
    ++++0x138 [32-bit Pointer] ???
    +++++0x4 [32-bit] Kills during level
    +++0xa8: [32-bit] Position X
    +++0xac: [32-bit] Position Z
    +++0xb0: [32-bit] Position Y
    +++0x10C: [32-bit] Health
    +++0x110: [32-bit] Health Max
    +++0x2E8: [32-bit Pointer] Inv
    ++++0x1C: [32-bit Pointer] Weapons
    +++++0x00: [32-bit Pointer] Blaster
    ++++++0x48: [32-bit] Blaster Ammo
    ++++++0x4c: [32-bit] Blaster Max Ammo
    ++++++0x50: [32-bit] Blaster Level
    ++++++0x54: [16-bit] Blaster EXP
    +++++0x20: [32-bit Pointer] Lasso
    ++++++0x48: [32-bit] Lasso Ammo
    ++++++0x4c: [32-bit] Lasso Max Ammo
    ++++++0x50: [32-bit] Lasso Level
    ++++++0x54: [16-bit] Lasso EXP
    +++++0x08: [32-bit Pointer] Fusion Bouncer
    ++++++0x48: [32-bit] FB Ammo
    ++++++0x4c: [32-bit] FB Max Ammo
    ++++++0x50: [32-bit] FB Level
    ++++++0x54: [16-bit] FB EXP
    +++++0x10: [32-bit Pointer] Expand-O-Matic
    ++++++0x48: [32-bit] EOM Ammo
    ++++++0x4c: [32-bit] EOM Max Ammo
    ++++++0x50: [32-bit] EOM Level
    ++++++0x54: [16-bit] EOM EXP
    +++++0x18: [32-bit Pointer] Doom Barrage
    ++++++0x48: [32-bit] DB Ammo
    ++++++0x4c: [32-bit] DB Max Ammo
    ++++++0x50: [32-bit] DB Level
    ++++++0x54: [16-bit] DB EXP
    """

    LAST_USED_WEAPON = dword(0x386310)
    """
    [32-bit] Last Used Weapon
    0x03 = Atomic Scepter
    0x04 = Mega Blaster
    0x05 = Fusion Bouncer
    0x06 = Electric Lasso
    0x07 = Expand-O-Matic
    0x08 = Doom Barrage
    0x0e = Nothing (happens after loading a level)
    """

    END_SCREEN_REACHED = byte(0x398443)
    """
    [8-bit] End Screen Reached
    0x00 = Not reached, reset on new level load
    0x01 = Inside end screen
    """

    DOWNTOWN_1_COLLECTIBLES = byte(0x398558)
    """
    [8-bit BitCount] Downtown 1 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    DOWNTOWN_1_STATE = byte(0x39855a)
    """
    [8-bit BitCount] Downtown 1 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    DOWNTOWN_2_COLLECTIBLES = byte(0x39855b)
    """
    [8-bit BitCount] Downtown 2 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    DOWNTOWN_2_STATE = byte(0x39855d)
    """
    [8-bit BitCount] Downtown 2 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    DOWNTOWN_3_COLLECTIBLES = byte(0x39855e)
    """
    [8-bit BitCount] Downtown 3 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    DOWNTOWN_3_STATE = byte(0x398560)
    """
    [8-bit BitCount] Downtown 3 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    DOWNTOWN_4_COLLECTIBLES = byte(0x398561)
    """
    [8-bit BitCount] Downtown 4 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    DOWNTOWN_4_STATE = byte(0x398563)
    """
    [8-bit BitCount] Downtown 4 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    DOWNTOWN_5_COLLECTIBLES = byte(0x398564)
    """
    [8-bit BitCount] Downtown 5 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    DOWNTOWN_5_STATE = byte(0x398566)
    """
    [8-bit BitCount] Downtown 5 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    UNDERGROUND_1_COLLECTIBLES = byte(0x398567)
    """
    [8-bit BitCount] Underground 1 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    UNDERGROUND_1_STATE = byte(0x398569)
    """
    [8-bit BitCount] Underground 1 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    UNDERGROUND_2_COLLECTIBLES = byte(0x39856a)
    """
    [8-bit BitCount] Underground 2 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    UNDERGROUND_2_STATE = byte(0x39856c)
    """
    [8-bit BitCount] Underground 2 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    UNDERGROUND_3_COLLECTIBLES = byte(0x39856d)
    """
    [8-bit BitCount] Underground 3 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    UNDERGROUND_3_STATE = byte(0x39856f)
    """
    [8-bit BitCount] Underground 3 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    UNDERGROUND_4_COLLECTIBLES = byte(0x398570)
    """
    [8-bit BitCount] Underground 4 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    UNDERGROUND_4_STATE = byte(0x398572)
    """
    [8-bit BitCount] Underground 4 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    UNDERGROUND_5_COLLECTIBLES = byte(0x398573)
    """
    [8-bit BitCount] Underground 5 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    UNDERGROUND_5_STATE = byte(0x398575)
    """
    [8-bit BitCount] Underground 5 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    WATERFRONT_1_COLLECTIBLES = byte(0x398576)
    """
    [8-bit BitCount] Waterfront 1 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    WATERFRONT_1_STATE = byte(0x398578)
    """
    [8-bit BitCount] Waterfront 1 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    WATERFRONT_2_COLLECTIBLES = byte(0x398579)
    """
    [8-bit BitCount] Waterfront 2 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    WATERFRONT_2_STATE = byte(0x39857b)
    """
    [8-bit BitCount] Waterfront 2 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    WATERFRONT_3_COLLECTIBLES = byte(0x39857c)
    """
    [8-bit BitCount] Waterfront 3 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    WATERFRONT_3_STATE = byte(0x39857e)
    """
    [8-bit BitCount] Waterfront 3 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    WATERFRONT_4_COLLECTIBLES = byte(0x39857f)
    """
    [8-bit BitCount] Waterfront 4 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    WATERFRONT_4_STATE = byte(0x398581)
    """
    [8-bit BitCount] Waterfront 4 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    WATERFRONT_5_COLLECTIBLES = byte(0x398582)
    """
    [8-bit BitCount] Waterfront 5 Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    WATERFRONT_5_STATE = byte(0x398584)
    """
    [8-bit BitCount] Waterfront 5 State
    bit0 = Unlocked
    bit4 = Cleared
    """

    MUSEUM_COLLECTIBLES = byte(0x398585)
    """
    [8-bit BitCount] Museum Collectibles
    bit0 = M
    bit1 = E
    bit2 = G
    bit3 = A
    bit4 = Photo
    """

    MUSEUM_STATE = byte(0x398587)
    """
    [8-bit BitCount] Museum State
    bit0 = Unlocked
    bit4 = Cleared
    """

    TOTAL_ENNEMY_KILLS = word(0x3985a8)
    """
    [16-bit] Total Ennemy Kills (written on level finish)
    """

    PAUSED_STATE = byte(0x39a2f4)
    """
    [8-bit] Paused State
    0x00 = Unpaused
    0x01 = Paused
    Affected by pause menu, dialog boxes (anything that will say Paused on top screen)
    """

    FRAMES_SINCE_GAME_START = dword(0x3ffc3c)
    """
    [32-bit] Frames since game start
    """

