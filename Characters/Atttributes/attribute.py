from numpy import prod


class AttributeKeyword:
    """
    Description:
        Assists tracking and calculating values associated with Attributes

    Example:
        Strength
        Dexterity
        Intelligence

        Additional
        Increase
        Decrease
        More
        Less
    """
    def __init__(self, base=0.0, sources=None):
        self._sources = {"base": base}
        if sources:
            self._sources.update(sources)
        self._current = 0

    def add_source(self, new_source):
        self._sources.update(new_source)
        self.update()

    def update(self):
        return self._current

    def get_current(self):
        return self._current




class LevelModifier(AttributeKeyword):
    """
    Description:
        How much either Strength, Dexterity, or Intelligence contributes to an attribute

    Example:
        Strength                = 50
        Contribution to life    = (5/10)
        Total                   = 25
    """
    def __init__(self, base=0.0, sources=None):
        super().__init__(base=base, sources=sources)
        self._current = sum(self._sources.values())

    def update(self):
        self._current = sum(self._sources.values())
        return self._current


class SDIModifier(AttributeKeyword):
    """
    Description:
        How much either Strength, Dexterity, or Intelligence contributes to an attribute

    Example:
        Strength                = 50
        Contribution to life    = (5/10)
        Total                   = 25
    """
    def __init__(self, base=0.0, sources=None):
        super().__init__(base=base, sources=sources)
        self._current = sum(self._sources.values())

    def update(self):
        self._current = sum(self._sources.values())
        return self._current


class Additional(AttributeKeyword):
    """
    Description:
        Additional refers to a flat bonus to the underlying base value.

    Example:
        Base Damage         = 50
        Additional Damage   = 30
        Total Damage        = 80
    """
    def __init__(self, base=0.0, sources=None):
        super().__init__(base=base, sources=sources)
        self._current = sum(self._sources.values())

    def update(self):
        self._current = sum(self._sources.values())
        return self._current


class IncreaseDecrease(AttributeKeyword):
    """
    Description:
        Additional refers to a percentage bonus to the underlying base value.

    Example:
        Base Damage         = 50
        Increase Damage     = 30
        Total Damage        = 65
    """

    def __init__(self, base=0.0, sources=None):
        super().__init__(base=base, sources=sources)
        self._current = sum([val/100 for val in self._sources.values()])

    def update(self):
        self._current = sum([val/100 for val in self._sources.values()])
        return self._current


class More(AttributeKeyword):
    """
    Description:
        More refers to a cumulative percentage bonus to the total value.

    Example:
        Base Damage         = 50
        Decrease Damage     = 10, 10, 10
        Total Damage        = 66.55
    """

    def __init__(self, base=0.0, sources=None):
        super().__init__(base=base, sources=sources)
        self._current = prod([1 + val/100 for val in self._sources.values()])

    def update(self):
        self._current = prod([1 + val/100 for val in self._sources.values()])
        return self._current


class Less(AttributeKeyword):
    """
    Description:
        Less refers to a cumulative percentage penalty to the total value.

    Example:
        Base Damage         = 50
        Decrease Damage     = 10, 10, 10
        Total Damage        = 36.45
    """

    def __init__(self, base=0.0, sources=None):
        super().__init__(base=base, sources=sources)
        self._current = prod([1 - val/100 for val in self._sources.values()])

    def update(self):
        self._current = prod([1 - val/100 for val in self._sources.values()])
        return self._current


class Attribute:

    def __init__(
            self,
            base=0,
            level_modifier=None,
            strength_modifier=0.0,
            dexterity_modifier=0.0,
            intelligence_modifier=0.0,
            add_mods=None,
            inc_mods=None,
            dec_mods=None,
            more_mods=None,
            less_mods=None
    ):
        self.base                  = base
        self.level_modifier        = LevelModifier(base=level_modifier)
        self.strength_modifier     = SDIModifier(base=strength_modifier)
        self.dexterity_modifier    = SDIModifier(base=dexterity_modifier)
        self.intelligence_modifier = SDIModifier(base=intelligence_modifier)
        self.additional            = Additional(sources=add_mods)
        self.increase              = IncreaseDecrease(sources=inc_mods)
        self.decrease              = IncreaseDecrease(sources=dec_mods)
        self.more                  = More(sources=more_mods)
        self.less                  = Less(sources=less_mods)

    def get_current_total(self, level=0, strength=0, dexterity=0, intelligence=0):
        total = self.base + (level * self.level_modifier.get_current()) + self.additional.get_current()
        total += strength * self.strength_modifier.get_current()
        total += dexterity * self.dexterity_modifier.get_current()
        total += intelligence * self.intelligence_modifier.get_current()
        total *= (1 + self.increase.get_current() + self.decrease.get_current())
        total *= self.more.get_current()
        total *= self.less.get_current()
        return total


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

    def __init__(
            self,
            base=38,
            level_modifier=12,
            strength_modifier=(5/10),
            dexterity_modifier=0.0,
            intelligence_modifier=0.0,
            add_mods=None,
            inc_mods=None,
            dec_mods=None,
            more_mods=None,
            less_mods=None
    ):
        super().__init__(
            base=base,
            level_modifier=level_modifier,
            strength_modifier=strength_modifier,
            dexterity_modifier=dexterity_modifier,
            intelligence_modifier=intelligence_modifier,
            add_mods=add_mods,
            inc_mods=inc_mods,
            dec_mods=dec_mods,
            more_mods=more_mods,
            less_mods=less_mods
        )
