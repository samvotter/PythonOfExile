from Characters.Atttributes.attribute import (
    # core attributes
    Strength,
    Dexterity,
    Intelligence,

    # derived attributes
    Life
)


class Character:

    def __init__(
            self,
            level           = 1,
            base_str        = 0,
            base_dex        = 0,
            base_int        = 0,
    ):
        self.level = level
        self.strength = Strength(base=base_str)
        self.dexterity = Dexterity(base=base_dex)
        self.intelligence = Intelligence(base=base_int)
        self.life = Life()

    def get_total_life(self):
        return self.life.get_current_total(
            level=self.level,
            strength=self.strength.get_current_total(),
            dexterity=self.dexterity.get_current_total(),
            intelligence=self.intelligence.get_current_total()
        )
