from typing import NamedTuple, Dict, List, Optional
from BaseClasses import Location, Item, ItemClassification

from .names import region_names as rname
from .names import shell_names as sname
from .names import shell_location_names as slname

class ACTShell(Item):
    game: str = "Another Crabs Treasure"

shell_base_id: int = 483021700

class ShellData(NamedTuple):
    shell_id_offset: int
    rolling_attack: bool
    magic_damage: bool

shell_table: Dict[str, ShellData] = {
    sname.soda_can: (1, True, True),
    sname.bottle_cap: (2, True, False)
}

class ACTShellLocations(Location):
    game: str = "Another Crabs Treasure"

shell_location_base_id: int = 483021700

class ShellLocationData(NamedTuple):
    region: str
    shell_location_id_offset: int
    shell_location_group: Optional[str] = None

shell_location_table: Dict[str, ShellLocationData] = {
    slname.soda_can_nephro1: (rname.central_shallows, 1, "Soda Cans")
}