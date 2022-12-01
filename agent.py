from torch import nn
from genome import Genome, default_genome
from personality import Personality, default_personality
from familyTree import FamilyTree, default_family_tree
from appearance import Appearance, default_appearance
from config import config

'''
AGENT CLASS
'''


class Agent():


    def __init__(   self,
                    brain: nn.Module, 
                    name: str = '',
                    appearance: Appearance = default_appearance,
                    family_tree: FamilyTree = default_family_tree,
                    personality: Personality = default_personality,
                    config: dict = config,
                    genome: Genome = default_genome,
                    sight_range: int = 0,
                    location_x: float = 0.0,
                    location_y: float = 0.0,
                    age: float = 0.0,
                    direction: float = 0.0,
                    speed: float = 0.0,
                    generation: int = 0,
                    constructed: bool = False):

        self.config = config

        #movement and location vectors
        self.sight_range = sight_range
        self.location_x = location_x
        self.location_y = location_y
        self.direction = direction
        self.speed = speed

        #build agent from param modules
        if constructed:
            self.brain = brain
            self.genome = genome
            self.personality = personality

        #assorted
        self.generation = generation
        self.age = age
        self.name = name
        self.appearance = appearance
        self.family_tree = family_tree


    

