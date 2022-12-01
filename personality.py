from config import config

'''
PERSONALITY
'''


class Personality():


    def __init__(   self,
                    config: dict = config,
                    parent_1: dict = {},
                    parent_2: dict = {},
                    init_generation: bool = False):

        self.config = config

        self.parent_1 = parent_1
        self.parent_2 = parent_2

        self.personality = self.config['personality']

        if init_generation:
            self.GenerateInitPersonality()
        else:
            self.CombineFamilyPersonality()

    
    def __call__(   self, 
                    key: str = "", 
                    indexable: bool = False, 
                    index: int = -1):

        if indexable:
                if index is not -1:
                    return list(self.personality.values())[index]
                else:
                    return list(self.personality.values())
        else:   
            if key is not "":
                return self.personality[key]
            else:
                return self.personality


    def GenerateInitPersonality(self):

        pass


    def CombineFamilyPersonality(self):

        pass


default_personality = Personality(init_generation=True)