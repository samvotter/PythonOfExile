from Characters.character import Character


class Duelist(Character):

    def __init__(
            self,
            base_str=23,
            base_dex=23,
            base_int=14
    ):
        super().__init__(
            base_str=base_str,
            base_dex=base_dex,
            base_int=base_int
        )