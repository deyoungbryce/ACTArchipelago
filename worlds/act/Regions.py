from typing import Dict, List, NamedTuple
from enum import IntEnum

from .names import region_names as rname, item_names as iname, location_names as lname

class ACTType(IntEnum):
    location = 1
    region = 2
    # for now there will probably only be locations, but this is just in case the regions need to be split up more than they are now


class ACTData(NamedTuple):
    type: int  # whether it is a location or region
    rules: List[List[str]] = [] # logic rules for how to access
    # Rule Example: [[grapple],[air_attack]] means that grapple and air_attack are needed to access



traversal_requirements: Dict[str, Dict[str, ACTData]] = {
    rname.tide_pool: {
        
    }
    rname.starting_cave: {

    }
    rname.central_shallows: {

    }
    rname.slacktide_before: {

    }
    rname.slacktide_after: {

    }
    rname.snail_cave: {

    }
    rname.reefs_edge: {

    }
    rname.new_carcinia_upper: {

    }
    rname.new_carcinia_lower: {

    }
    rname.sands_between: {
        
    }
}