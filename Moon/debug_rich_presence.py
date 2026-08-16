from pycheevos.core.condition import ConditionList
from pycheevos.core.helpers import add_source, measured
from pycheevos.models.rich_presence import *

from memory import Memory
from logic import *

def render(conditions: ConditionList):
    return "_".join([cond.render() for cond in conditions])

class MoonRichPresence(RichPresence):
    def __init__(self):
        super().__init__()
        self.game_id = 9969

    def generate(self):
        self.add_display(Memory.GAME_STATE == 0, 'Uninitialized Game State')
        self.add_display(None, f'Current Map : {self.print_ascii(7, Memory.CURRENT_AREA_ID)} • Cutscene : {self.print_ascii(12, Memory.LAST_LOADED_MOVIE_CUTSCENE_ID)} • Event flags : {self.print_bits(Memory.GAME_STATE.address)}')

    def print_ascii(self, size: int, addr: int):
        buffer = ''
        for i in range(size):
            buffer += f'@ASCIIChar({byte(addr+i)})'
        return buffer
    
    def print_bits(self, baseAddr: int) :
        buffer = ''
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit7(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit6(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit5(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit4(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit3(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit2(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit1(0x20))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit0(0x20))})'
        buffer += '-'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit7(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit6(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit5(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit4(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit3(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit2(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit1(0x21))})'
        buffer += f'@Number({ptr(baseAddr) >> ptr(0x04) >> measured(bit0(0x21))})'
        return buffer;


if __name__=="__main__":
    rp = MoonRichPresence()
    rp.generate()
    rp.save(rp.game_id, path="output/")

