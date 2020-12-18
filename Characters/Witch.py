from Characters.character import Character


class Witch(Character):

    def __init__(
            self,
            base_str=14,
            base_dex=14,
            base_int=32
    ):
        super().__init__(
            base_str=base_str,
            base_dex=base_dex,
            base_int=base_int
        )