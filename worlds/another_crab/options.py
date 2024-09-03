from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class RandomizeFork(Toggle):
    """If enabled, the fork is added to the item pool. If disabled, the fork is left in its default location"""
    display_name: str = "Randomize Fork"
    default: bool = False

class RemoveCostumes(Toggle):
    """If enabled, removes costumes from the item pool"""
    display_name: str = "Remove Costumes"
    default: bool = False

class MicroplasticMultiplier(Range):
    """Multiplies the ammount of microplastics you recieve"""
    display_name: str = "Microplastic Multiplier"
    range_start: float = 0.01
    range_end: float = 100
    default: int = 1

class DeathLink(Toggle):
    """Enables Death Link"""
    display_name: str = "Death Link"
    default: bool = False

@dataclass
class ACTGameOptions(PerGameCommonOptions):
    randomizeFork: RandomizeFork
    removeCostumes: RemoveCostumes
    microplasticMultiplier: MicroplasticMultiplier
    deathlink: DeathLink