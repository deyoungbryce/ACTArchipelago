from typing import Dict, Set

from .names import region_names as rname

ACT_regions: Dict[str, Set[str]] = {
    rname.menu: {
        rname.tide_pool
    },
    rname.tide_pool: {
        rname.starting_cave
    },
    rname.starting_cave: {
        rname.central_shallows
    },
    rname.central_shallows: {
        rname.slacktide_before,
    },
    rname.slacktide_before: {
        rname.snail_cave
    },
    rname.snail_cave: {
        rname.slacktide_after
    },
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
        rname.scuttleport,
        rname.pinbarge
    },
    rname.scuttleport: set(),
    rname.pinbarge: {
        rname.unfathom
    },
    rname.unfathom: {
        rname.plains
    },
    rname.plains: {
        rname.old_ocean
    },
    rname.old_ocean: {
        rname.drain_bottom
    },
    rname.drain_bottom: {
        rname.trash_island
    },
    rname.trash_island: {
        rname.carcinia_ruins
    },
    rname.carcinia_ruins: set()
}

