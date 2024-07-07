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
    rname.reefs_edge: {
        rname.new_carcinia_lower,
        rname.new_carcinia_upper
    },
    rname.new_carcinia_lower: {rname.sands_between},
    rname.new_carcinia_upper: {rname.sands_between},
    rname.sands_between: {
        rname.post_pag,
        rname.secluded_ridge,
        rname.expired_grove,
        rname.flotsam_vale
    },
    rname.post_pag: set(),
    rname.secluded_ridge: set(),
    rname.expired_grove_lower: set(),
    rname.expired_grove_upper: set(),
    rname.flotsam_vale: set(),
    rname.pinbarge: set(),
    rname.unfathom: set(),
    rname.bleached_city: set(),
    rname.drain_bottom: set(),
    rname.trash_island: set()
}

