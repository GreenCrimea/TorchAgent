from config import config

'''
FAMILY TREE
'''


class FamilyTree():


    def __init__(   self,
                    config: dict = config,
                    parent_1: list = [],
                    parent_2: list = [],
                    init_generation: bool = False):

        self.config = config

        self.parent_1 = parent_1
        self.parent_2 = parent_2

        self.family_tree = []

        if init_generation:
            self.family_tree = ['', 'FIRST_GENERATION', 'FIRST_GENERATION']
        else:
            self.family_tree.append('')
            self.family_tree.append(parent_1)
            self.family_tree.append(parent_2)

    
    def __call__(self):

        return self.family_tree


default_family_tree = FamilyTree(init_generation=True)