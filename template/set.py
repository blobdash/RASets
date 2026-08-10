from turtle import speed
from pycheevos.models.leaderboard import Leaderboard
from pycheevos.models.set import AchievementSet
from pycheevos.models.achievement import Achievement
from pycheevos.core.helpers import *
from pycheevos.core.constants import *

from logic import *
from memory import Memory
from framework import achievement, achievement_set, leaderboard

import assets

@achievement_set(
    assets=assets,
    author="blobdash"
)
class TemplateSet(AchievementSet):
    def __init__(self):
        super().__init__(
            game_id=0,
            title="TEMPLATE"
        )

if __name__=="__main__":
    TemplateSet().save("output/")
