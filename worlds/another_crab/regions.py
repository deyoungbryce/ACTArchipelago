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
        rname.snail_cave,
        rname.slacktide_before,
        rname.slacktide_after
    },
    rname.snail_cave: set(),
    rname.slacktide_before: set(),
    rname.slacktide_after: {
        rname.reefs_edge
    },
    rname.reefs_edge: {
        rname.new_carcinia
    },
    rname.new_carcinia: {
        rname.sands_between
    },
    rname.sands_between: {
        rname.post_pag,
        rname.secluded_ridge,
        rname.grove_main,
        rname.flotsam_vale
    },
    rname.post_pag: set(),
    rname.secluded_ridge: set(),
    rname.grove_main: {
        rname.grove_village
    },
    rname.grove_village: set(),
    rname.flotsam_vale: {
        rname.grove_village,
        rname.scuttleport
    },
    rname.scuttleport: set(),
    rname.pinbarge: {
        rname.unfathom
    },
    rname.unfathom: {
        rname.bleached_city
    },
    rname.bleached_city: {
        rname.drain_bottom
    },
    rname.drain_bottom: {
        rname.trash_island
    },
    rname.trash_island: {
        rname.carcinia_end
    },
    rname.carcinia_end: set()
}

