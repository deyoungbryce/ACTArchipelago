from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class ForkLocation(Choice):
    """Choose where the Fork(weapon) location is set.
    Available Options: vanilla_location, shuffled, shuffled_early"""
    display_name: str = "Randomize Fork"
    vanilla_location = 0
    shuffled = 1
    shuffled_early = 2
    default = 0

class ShelleportLocation(Choice):
    """Choose where the Shelleport (fast travel) skill location will be
    Available Options: shuffled, starting_items, vanilla_location"""
    display_name: str = "Shelleport Location"
    shuffled = 0
    starting_items = 1
    vanilla_location = 2
    default = 0

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
    forkLocation: ForkLocation
    shelleportLocation: ShelleportLocation
    removeCostumes: RemoveCostumes
    microplasticMultiplier: MicroplasticMultiplier
    deathlink: DeathLink