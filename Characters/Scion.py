from Characters.character import Character


class Scion(Character):

    def __init__(
            self,
            base_str=20,
            base_dex=20,
            base_int=20
    ):
        super().__init__(
            base_str=base_str,
            base_dex=base_dex,
            base_int=base_int
        )