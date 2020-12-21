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
    def __init__(self, sources=None):
        self.sources = {}.update(sources)
        self.current = 0

    def update(self):
        return self.current


class LevelModifier(AttributeKeyword):
    """
    Description:
        How much either Strength, Dexterity, or Intelligence contributes to an attribute

    Example:
        Strength                = 50
        Contribution to life    = (5/10)
        Total                   = 25
    """
    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = sum(self.sources.values())

    def update(self):
        self.current = sum(self.sources.values())
        return self.current


class SDIModifier(AttributeKeyword):
    """
    Description:
        How much either Strength, Dexterity, or Intelligence contributes to an attribute

    Example:
        Strength                = 50
        Contribution to life    = (5/10)
        Total                   = 25
    """
    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = sum(self.sources.values())

    def update(self):
        self.current = sum(self.sources.values())
        return self.current


class Additional(AttributeKeyword):
    """
    Description:
        Additional refers to a flat bonus to the underlying base value.

    Example:
        Base Damage         = 50
        Additional Damage   = 30
        Total Damage        = 80
    """
    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = sum(self.sources.values())

    def update(self):
        self.current = sum(self.sources.values())
        return self.current


class Increase(AttributeKeyword):
    """
    Description:
        Additional refers to a percentage bonus to the underlying base value.

    Example:
        Base Damage         = 50
        Increase Damage     = 30
        Total Damage        = 65
    """

    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = sum([val/100 for val in self.sources.values()])

    def update(self):
        self.current = sum([val/100 for val in self.sources.values()])
        return self.current


class Decrease(AttributeKeyword):
    """
    Description:
        Decrease refers to a percentage penalty to the underlying base value.

    Example:
        Base Damage         = 50
        Decrease Damage     = 30
        Total Damage        = 35
    """

    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = -sum([val/100 for val in self.sources.values()])

    def update(self):
        self.current = -sum([val/100 for val in self.sources.values()])
        return self.current


class More(AttributeKeyword):
    """
    Description:
        More refers to a cumulative percentage bonus to the total value.

    Example:
        Base Damage         = 50
        Decrease Damage     = 10, 10, 10
        Total Damage        = 66.55
    """

    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = prod([1 + val/100 for val in self.sources.values()])

    def update(self):
        self.current = prod([1 + val/100 for val in self.sources.values()])
        return self.current


class Less(AttributeKeyword):
    """
    Description:
        Less refers to a cumulative percentage penalty to the total value.

    Example:
        Base Damage         = 50
        Decrease Damage     = 10, 10, 10
        Total Damage        = 36.45
    """

    def __init__(self, sources=None):
        super().__init__(sources=sources)
        self.current = prod([1 - val/100 for val in self.sources.values()])

    def update(self):
        self.current = prod([1 - val/100 for val in self.sources.values()])
        return self.current


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
        self._base                  = base
        self._per_level             = LevelModifier(sources=level_modifier)
        self._sdi_modifiers   = {
            "strength":     SDIModifier(sources={"base": strength_modifier}),
            "dexterity":    SDIModifier(sources={"base": dexterity_modifier}),
            "intelligence": SDIModifier(sources={"base": intelligence_modifier}),
        }
        self._additional            = Additional(sources=add_mods)
        self._increase              = Increase(sources=inc_mods)
        self._decrease              = Decrease(sources=dec_mods)
        self._more                  = More(sources=more_mods)
        self._less                  = Less(sources=less_mods)

    def get_total(self, level=0):
        base = self._base + (level * self._per_level.current) + self._additional.current
        base += sum([val.current for val in self._sdi_modifiers.values()])


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

