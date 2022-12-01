from config import config

'''
APPEARANCE
'''


class Appearance():


    def __init__(   self,
                    config: dict = config,
                    parent_1: dict = {},
                    parent_2: dict = {},
                    init_generation: bool = False):

        self.config = config

        self.parent_1 = parent_1
        self.parent_2 = parent_2

        self.appearance = {}


    def __call__(   self,
                    key: str = "",
                    indexable: bool = False,
                    index: int = -1):

        if indexable:
            if index != -1:
                return (list(self.appearance.values))[index]
            else:
                return (list(self.appearance.values))
        else:
            if key != "":
                return self.appearance[key]
            else:
                return self.appearance


default_appearance = Appearance(init_generation=True)