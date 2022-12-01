from config import config
import torch
from torch import nn
from genome import Genome, default_genome

'''
BRAIN
'''


class Brain(nn.Module):


    def __init__(   self,
                    config: dict = config,
                    genome: Genome = default_genome,
                    input_shape: int = 1,
                    hidden_units: int = 1,
                    output_shape: int = 1,
                    architecture: str = ""):
        
        super().__init__()


    def forward(self, x: torch.Tensor):
        pass


default_brain = Brain()