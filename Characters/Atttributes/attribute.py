from numpy import prod


class Attribute:

    def __init__(
            self,
            base=0,
            per_level=0,
            strength_modifier=0.0,
            dexterity_modifier=0.0,
            intelligence_modifier=0.0
    ):
        self._base = base
        self._per_level = per_level
        self._attribute_modifiers = {
            "strength": strength_modifier,
            "dexterity": dexterity_modifier,
            "intelligence": intelligence_modifier
        }

    def get_total(
            self,
            character_level=1,
            sdi=None,
            additional=None,
            increase=None,
            decrease=None,
            more=None,
            less=None
    ):
        attr_contribution = 0
        add_contribution = 0
        inc_contribution = 0
        dec_contribution = 0
        more_contribution = 1
        less_contribution = 1
        if sdi:
            attr_contribution = sum([self._attribute_modifiers[key] * sdi[key] for key in sdi.keys()])
        if additional:
            add_contribution = sum(additional)
        if increase:
            inc_contribution = sum([val/100 for val in increase])
        if decrease:
            dec_contribution = sum([val/100 for val in decrease])
        if more:
            more_contribution = prod([1 + val/100 for val in more])
        if less:
            less_contribution = prod([1 - val/100 for val in less])
        flat = self._base + (character_level * self._per_level) + attr_contribution + add_contribution
        inc_or_dec = 1 + inc_contribution - dec_contribution
        return int(flat * inc_or_dec * more_contribution * less_contribution)


class Strength(Attribute):

    def __init__(self, base=0):
        super().__init__(base=base)


class Dexterity(Attribute):

    def __init__(self, base=0):
        super().__init__(base=base)


class Intelligence(Attribute):

    def __init__(self, base=0):
        super().__init__(base=base)


class Life(Attribute):

    def __init__(self, base=38, per_level=12, strength_modifier=(1/2)):
        super().__init__(base=base, per_level=per_level, strength_modifier=strength_modifier)

