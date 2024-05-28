from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions

class DeathLink(Toggle):
    """Enables Death Link"""
    display_name = "Death Link"
    default = False

class RandomizeFork(Toggle):
    """If enabled, the fork is added to the item pool. If disabled, the fork is left in its default location"""
    display_name = "Randomize Fork"
    default = False

class MicroplasticMultiplier(Range):
    """Multiplies the ammount of microplastics you recieve"""
    display_name = "Microplastic Multiplier"
    range_start = 0.01
    range_end = 100
    default = 1

@dataclass
class ACTGameOptions(PerGameCommonOptions):
    randomizeFork: RandomizeFork
    microplasticMultiplier: MicroplasticMultiplier