from typing import Dict, Set

from .names import region_names as rname

ACT_regions: Dict[str, Set[str]] = {
    rname.menu: {
        rname.central_shallows
    },
    rname.tide_pool: {
        rname.starting_cave
    },
    rname.starting_cave: {
        rname.central_shallows
    },
    rname.central_shallows: {
        rname.snail_cave, rname.slacktide_before, rname.slacktide_after
    },
    rname.snail_cave: set(),
    rname.slacktide_before: set(),
    rname.slacktide_after: {
        rname.reefs_edge
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

