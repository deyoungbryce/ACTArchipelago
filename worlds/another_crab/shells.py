from typing import NamedTuple, Dict, List, Optional
from BaseClasses import Location, Item, ItemClassification

from .names import region_names as rname
from .names import shell_names as sname
from .names import shell_location_names as slname

class ACTShell(Item):
    game: str = "Another Crabs Treasure"

class ACTShellLocations(Location):
    game: str = "Another Crabs Treasure"

shell_base_id: int = 483021700

class ShellData(NamedTuple):
    shell_id_offset: int
    rolling_attack: bool
    magic_damage: bool
    regions: List[str]

shell_table: Dict[str, ShellData] = {
    sname.soda_can: (1, True, True, [rname.central_shallows, rname.snail_cave]),
    sname.bottle_cap: (2, True, False)
}

shell_name_to_id: Dict[str, int] = {name: shell_base_id + data.shell_id_offset for name, data in shell_table.items()}