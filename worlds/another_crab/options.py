from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

class ForkLocation(Choice):
    """Choose where the Fork(weapon) location is set.
    - Shuffled: Fork is placed into item pool.
    - Shuffled Early Local: Forces Fork location to be somewhere early in your own game.
    - Shuffled Early Global: Forces Fork location to be somewhere early in any game.
    - Vanilla Location: Forces Fork to be placed at its intended location."""
    display_name: str = "Fork Location"
    option_shuffled = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    option_vanilla_location = 3
    default = 3

class AllowForkless(Toggle):
    """If true, allows for bosses to have to be defeated without the fork.
    Must set fork location to shuffled if true."""
    display_name:str = "Allow Forkless"
    default: bool = False
 
class ShelleportLocation(Choice):
    """Choose where the Shelleport (fast travel) skill location is set
    - Shuffled: Shelleport is placed into the item pool.
    - Shuffled Early Local: Forces Shelleport location to be somewhere early in your own game.
    - Sheffled Early Global: Forces Shelleport location to somewhere early in any game.
    - Starting Items: Places Shelleport in your starting inventory.
    - Vanilla Location: Forces Shelleport to be placed at its intended location"""
    display_name: str = "Shelleport Location"
    option_shuffled = 0
    option_shuffled_early_local = 1
    option_shuffled_early_global = 2
    option_starting_items = 3
    option_vanilla_location = 4
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
    allow_forkless: AllowForkless
    shelleport_location: ShelleportLocation
    fishing_line_location: FishingLineLocation
    remove_costumes: RemoveCostumes
    microplasticMultiplier: MicroplasticMultiplier
    deathlink: DeathLink