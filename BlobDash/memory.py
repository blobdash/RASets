from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    CURRENT_SCENE_ID = byte(0x00c414)
    """
    [8-bit] Current Scene ID
    0x03 = Title Screen
    0x14 = Shiny Goals from Distance Goals
    0x16 = End Cutscene
    0x17 = Collection
    0x32 = Settings from Data Clear cancel
    0x38 = Intro Cutscene
    0x3c = Results
    0x3d = Main Menu
    0x45 = Game by Screen from Data Clear
    0x50 = Shiny Goals from Title Screen
    0x55 = Game by Screen
    0x65 = Made it to college!
    0x67 = Collection from Hats/Print
    0x6d = Distance Goals
    0x85 = In game
    0x9c = Prints from first print back
    0xc7 = Collection > Hats
    0xcb = Results from Quit
    0xd2 = Data Clear confirmation screen
    0xe2 = Settings
    0xf2 = Title Screen
    0xfc = Collection > Prints

    // Prints
    0x06 = Logo from right
    0x35 = blobs from left
    0x70 = blobs from right
    0x7f = Intro print from left
    0xa1 = Shiny from left
    0xa5 = Intro print from right
    0xc9 = Title monochrome from left
    0xd1 = Shiny from right
    0xeb = Logo from left

    // Transition flickers for Main Menu
    0x0f = Main Menu from Collection
    0x1e = Main Menu from Goal
    0x9d = Main Menu from Settings
    0xbf = Main Menu from Game End
    0xe1 = Main Menu from Run End
    0x62 = Main Menu from first boot
    """

    CURRENT_MENU_SELECTION_OFFSET = byte(0x00c419)
    """
    [8-bit] Current menu selection offset
    """

    CURRENT_RUN_HP = byte(0x00c41b)
    """
    [8-bit] Current run HP
    0x00 = Dead
    0x04 = Max HP
    """

    TOTAL_SHINIES = byte(0x00c41d)
    """
    [8-bit] Total Shinies (low byte)
    """

    TOTAL_SHINIES_1 = byte(0x00c41e)
    """
    [8-bit] Total Shinies (high byte)
    """

    CURRENT_RUN_DISTANCE = byte(0x00c41f)
    """
    [8-bit] Current run distance (low byte)
    """

    CURRENT_RUN_DISTANCE_1 = byte(0x00c420)
    """
    [8-bit] Current run distance (high byte)
    """

    TOTAL_DISTANCE = byte(0x00c421)
    """
    [8-bit] Total distance (low byte)
    """

    TOTAL_DISTANCE_1 = byte(0x00c422)
    """
    [8-bit] Total distance (high byte)
    """

    CURRENT_RUN_SHINIES = byte(0x00c425)
    """
    [8-bit] Current run shinies (low byte)
    """

    CURRENT_RUN_SHINIES_1 = byte(0x00c426)
    """
    [8-bit] Current run shinies (high byte)
    """

    CURRENT_DIFFICULTY = byte(0x00c427)
    """
    [8-bit] Current difficulty
    0x01 = Easy
    0x02 = Normal
    0x03 = Hard
    """

    CURRENTLY_INTANGIBLE = byte(0x00c42d)
    """
    [8-bit] Currently intangible
    // Being intangible prevents you from taking damage
    // and also from collecting shinies
    // freezing doesn't prevent intangibility
    0x00 = Not intangible
    0x01 = Intangible
    """

