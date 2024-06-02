from typing import Dict, NamedTuple, Set, Optional
from .names import location_names as lname, region_names as rname

location_base_id = 483021700


class ACTLocationData(NamedTuple):
    region: str
    location_group: Optional[str] = None


location_table: Dict[str, ACTLocationData] = {
    # starting item locations (will probably just include heartkelp_initial and fork pickup because they are the items you pick up right at the beginning of the game)
    lname.heartkelp_inital: ACTLocationData(rname.tide_pool, "Starting Items"),
    lname.fork_pickup: ACTLocationData(rname.starting_cave, "Starting Items"),
    
    # currency item locations
    lname.breadclaw_ledge_cave: ACTLocationData(rname.starting_cave, "Currency"),
    lname.breadclaw_slacktide_sandcastle: ACTLocationData(rname.slacktide_before, "Currency"),

    # upgrade item locations
    lname.bloodstar_shallows_help: ACTLocationData(rname.central_shallows, "Upgrades"),

    # stowaway locations
    lname.siphonophore_shallows: ACTLocationData(rname.central_shallows, "Stowaways")
}

location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)
