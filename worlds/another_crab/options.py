from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class ForkLocation(Choice):
    """Choose where the Fork(weapon) location is set.
    - Shuffled: Fork is placed into item pool.
    - Shuffled Early: Forces Fork to be required to beat The Duchess, Magista. This means you will get the Fork earlier.
    - Vanilla Location: Forces Fork to be placed at its intended location."""
    display_name: str = "Fork Location"
    option_shuffled = 0
    option_shuffled_early = 1
    option_vanilla_location = 2
    default = 2

class ShelleportLocation(Choice):
    """Choose where the Shelleport (fast travel) skill location is set
    - Shuffled: Shelleport is placed into the item pool.
    - Shuffled Early: Forces Shelleport to be required before reaching The Duchess, Magista. This means you will get Shelleport earlier.
    - Starting Items: Places Shelleport in your starting inventory.
    - Vanilla Location: Forces Shelleport to be placed at its intended location"""
    display_name: str = "Shelleport Location"
    option_shuffled = 0
    option_shuffled_early = 1
    option_starting_items = 2
    option_vanilla_location = 3
    default = 1

class FishingLineLocation(Choice):
    """Choose where the Fishing Line (grapple) location is set
    - Shuffled: Fishing Line is placed into item pool.
    - Vanilla Location: Forces Fishing Line to be placed at its intended location"""
    display_name:str = "Fishing Line Location"
    option_shuffled = 0
    option_vanilla_location = 1
    default = 0

class RemoveCostumes(Toggle):
    """Set to true to remove costumes from the item pool."""
    display_name: str = "Remove Costumes"
    default: bool = False

class MicroplasticMultiplier(Range):
    """Multiplies the ammount of microplastics you recieve."""
    display_name: str = "Microplastic Multiplier"
    range_start: float = 0.01
    range_end: float = 100
    default: float = 1

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