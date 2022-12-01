import random
from config import config

'''
GENOME
'''


class Genome():


    def __init__(   self,
                    config: dict = config, 
                    parent_1: list = [],
                    parent_2: list = [],
                    init_generation: bool = False):

        self.config = config

        self.parent_1 = parent_1
        self.parent_2 = parent_2

        self.genome = []
        
        if init_generation:
            self.GenerateInitGenome()
        else:
            self.CombineFamilyGenes()


    def __call__(self):
        
        return self.genome


    def GenerateInitGenome(self):

        for i in range(self.config['genome_size']):
            self.genome.append(random.choice(self.config['genes_available']))


    def CombineFamilyGenes(self):

        for i in range(self.config['genome_size'] / 2):
            if random.randrange(1) == 1:
                self.genome.append(self.parent_1[i])
            else:
                self.genome.append(self.parent_2[i])


default_genome = Genome(init_generation=True)