import pytest

from Characters.character import Character
from Characters.duelist import Duelist
from Characters.marauder import Marauder
from Characters.ranger import Ranger
from Characters.scion import Scion
from Characters.shadow import Shadow
from Characters.templar import Templar
from Characters.witch import Witch

from Characters.Atttributes.attribute import Life


@pytest.mark.parametrize(
    "level,strength,add,inc,dec,more,less,result", [
        (1, 0, 0, 0, 0, 0, 0,                   50),
        (1, 100, 0, 0, 0, 0, 0,                 100),
        (1, 100, {"ten":10, ""}, [], [], [], [], 120),
        (1, {"strength": 100}, [], [10, 10], [], [], [], 120),
        (1, {"strength": 100}, [10, 10], [10, 10], [], [], [], 144),
        (1, {"strength": 100}, [10, 10], [], [10, 10], [], [], 96),
        (1, {"strength": 100}, [10, 10], [10, 10], [], [10, 10], [], 174),
        (1, {"strength": 100}, [10, 10], [10, 10], [], [], [10, 10], 116),
        (1, {"strength": 100}, [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], 93),

    ]
)
def test_X_life(level, strength, add, inc, dec, more, less, result):
    life = Life()
    life._add

    calculated = life.get_current_total(
        level=level,
        strength=strength
    )
    assert calculated == result


@pytest.mark.parametrize(
    "character,level,result", [
        (Character, 1, 50),
        (Character, 50, 638),
        (Character, 100, 1238),
        (Duelist, 1, 50+11),
        (Duelist, 50, 638+11),
        (Duelist, 100, 1238+11),
        (Marauder, 1, 50+16),
        (Marauder, 50, 638+16),
        (Marauder, 100, 1238+16),
        (Ranger, 1, 50+7),
        (Ranger, 50, 638+7),
        (Ranger, 100, 1238+7),
        (Scion, 1, 50+10),
        (Scion, 50, 638+10),
        (Scion, 100, 1238+10),
        (Shadow, 1, 50+7),
        (Shadow, 50, 638+7),
        (Shadow, 100, 1238+7),
        (Templar, 1, 50+11),
        (Templar, 50, 638+11),
        (Templar, 100, 1238+11),
        (Witch, 1, 50+7),
        (Witch, 50, 638+7),
        (Witch, 100, 1238+7)
    ]
)
def test_character_has_X_life_at_level(character, level, result):
    test_chr = character(level=level)
    calculated_life = test_chr.get_total_life()
    assert calculated_life == result

