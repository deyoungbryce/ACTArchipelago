from typing import Dict, List, NamedTuple, Set
from enum import IntEnum

from .names import region_names as rname, item_names as iname, location_names as lname

'''class ACTType(IntEnum):
    location = 1
    region = 2
    # for now there will probably only be locations, but this is just in case the regions need to be split up more than they are now


class ACTData(NamedTuple):
    type: int  # whether it is a location or region
    rules: List[List[str]] = [] # logic rules for how to access
    # Rule Example: [[grapple],[air_attack]] means that grapple and air_attack are needed to access



availability_requirements: Dict[str, Dict[str, ACTData]] = {
    rname.tide_pool: {
        lname.heartkelp_inital:
            ACTData(ACTType.location)
    },
    rname.starting_cave: {
        lname.fork_pickup:
            ACTData(ACTType.location),
        lname.breadclaw_caveofrespite_ledge:
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
    rname.slacktide_before: {
        lname.breadclaw_slacktide_sandcastle:
            ACTData(ACTType.location),
        lname.limpet_slacktide_stairs:
            ACTData(ACTType.location),
        lname.fishing_line:
            ACTData(ACTType.location),
        lname.seastar_slacktide_grappleroom:
            ACTData(ACTType.location, [[iname.fishing_line]]),
        lname.barnacle_slacktide_bigurchin:
            ACTData(ACTType.location, [[iname.fishing_line]])
    },
    rname.slacktide_after: {

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
}'''

ACT_regions: Dict[str, Set[str]] = {
    rname.menu: {
        rname.shallows
    },
    rname.shallows: {
        rname.tide_pool, rname.starting_cave, rname.central_shallows, rname.snail_cave, rname.fort_slacktide
    },
    rname.tide_pool: set(),
    rname.starting_cave: set(),
    rname.central_shallows: set(),
    rname.snail_cave: set(),
    rname.fort_slacktide: {
        rname.slacktide_before, rname.slacktide_after
    },
    rname.slacktide_before: set(),
    rname.slacktide_after: set(),
    rname.new_carcinia: {
        rname.reefs_edge, rname.new_carcinia_lower, rname.new_carcinia_upper
    },
    rname.reefs_edge: set(),
    rname.new_carcinia_lower: set(),
    rname.new_carcinia_upper: set(),
    rname.sands_between: set(),
    rname.expired_grove: set(),
    rname.flotsam_vale: set(),
    rname.pinbarge: set(),
    rname.unfathom: set(),
    rname.bleached_city: set(),
    rname.drain_bottom: set(),
    rname.trash_island: set()
}