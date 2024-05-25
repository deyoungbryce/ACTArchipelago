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



availability_requirements: Dict[str, Dict[str, ACTData]] = {
    rname.menu: {

    },
    rname.tide_pool: {
        lname.heartkelp_inital:
            ACTData(ACTType.location)
    },
    rname.starting_cave: {
        lname.fork_pickup:
            ACTData(ACTType.location),
        lname.breadclaw_ledge_cave:
            ACTData(ACTType.location)
    },
    rname.central_shallows: {

    },
    rname.fort_slacktide: {
        rname.slacktide_before:
            ACTData(ACTType.region, [[iname.shell_access]]),
        rname.slacktide_after:
            ACTData(ACTType.region, [[iname.fishing_line],[iname.pristine_pearl]])
    },
    rname.snail_cave: {

    },
    rname.reefs_edge: {

    },
    rname.new_carcinia: {

    },
    rname.sands_between: {
        
    },
    rname.expired_grove: {

    },
    rname.flotsam_vale: {

    },
    rname.pinbarge: {

    },
    rname.unfathom: {

    },
    rname.bleached_city: {

    },
    rname.drain_bottom: {

    },
    rname.trash_island: {

    }
}