from typing import Dict, NamedTuple, Set, Optional
from .names import location_names as lname

location_base_id = 483022700

class ACTLocationData(NamedTuple):
    region: str
    location_group: Optional[str] = None


location_table: Dict[str, ACTLocationData] = {

}

location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)