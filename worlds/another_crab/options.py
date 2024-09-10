from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class ForkLocation(Choice):
    """Choose where the Fork(weapon) location is set.
    Available Options: vanilla_location, shuffled, shuffled_early"""
    display_name: str = "Fork Location"
    option_vanilla_location = 0
    option_shuffled = 1
    option_shuffled_early = 2
    default = 0

class ShelleportLocation(Choice):
    """Choose where the Shelleport (fast travel) skill location is set
    Available Options: shuffled, starting_items, vanilla_location"""
    display_name: str = "Shelleport Location"
    option_shuffled = 0
    option_starting_items = 1
    option_vanilla_location = 2
    default = 0

class FishingLineLocation(Choice):
    """Choose where the Fishing Line (grapple) location is set
    Available Options: shuffled, vanilla_location"""
    display_name:str = "Fishing Line Location"
    option_shuffled = 0
    option_vanilla_location = 1
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
    fork_location: ForkLocation
    shelleport_location: ShelleportLocation
    fishing_line_location: FishingLineLocation
    remove_costumes: RemoveCostumes
    microplasticMultiplier: MicroplasticMultiplier
    deathlink: DeathLink