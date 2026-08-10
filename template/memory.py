from pycheevos.core.helpers import *
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    TEMPLATE: MemoryValue = byte(0x0)