from Characters.character import Character


class Templar(Character):

    def __init__(
            self,
            base_str=23,
            base_dex=14,
            base_int=23
    ):
        super().__init__(
            base_str=base_str,
            base_dex=base_dex,
            base_int=base_int
        )