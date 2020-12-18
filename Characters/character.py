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
            strength        = Strength,
            base_str        = 0,
            dexterity       = Dexterity,
            base_dex        = 0,
            intelligence    = Intelligence,
            base_int        = 0,
            life            = Life,
    ):
        self.level = level
        self.strength = strength(base=base_str)
        self.dexterity = dexterity(base=base_dex)
        self.intelligence = intelligence(base=base_int)
        self.life = life()

    def get_total_life(self):
        return self.life.get_total(
            character_level=self.level,
            sdi={
                "strength": self.strength.get_total(),
                "dexterity": self.dexterity.get_total(),
                "intelligence": self.intelligence.get_total()
            },
            # TODO fill in the effects
        )