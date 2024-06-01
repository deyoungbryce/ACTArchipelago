from typing import Dict, TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item
from BaseClasses import CollectionState
from .options import ACTGameOptions
from .names import region_names as rname
from .names import location_names as lname
if TYPE_CHECKING:
    from . import ACTWorld

def has_grapple(state: CollectionState, player: int) -> bool:
    return state.has("Fishing Line", player)

def has_pearl(state: CollectionState, player: int) -> bool:
    return state.has("Pristine Pearl", player)

def has_rwave(state: CollectionState, player: int)  -> bool:
    return state.has(lname.royal_wave_reward, player)

def set_region_rules(world: "ACTWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    #options = world.options

    multiworld.get_entrance("Central Shallows -> Moon Snail's Cave", player).access_rule = \
        lambda state: has_grapple(state, player)
    #multiworld.get_entrance(rname.slacktide_after, player).access_rule = \
        #lambda state: has_pearl(state, player)

    #multiworld.completion_condition[player] = lambda state: has_rwave(state, player)
    
def set_location_rules(world: "ACTWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

# Central Shallows
    set_rule(multiworld.get_location("Breadclaw (Central Shallows - Southeast Sandcastle)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Breadclaw (Central Shallows - East Grapple Ledge)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Hairclaw (Central Shallows - Grapple to Castle Turret)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Chipclaw (Central Shallows - Southwest Sandcastle)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Bloodstar Limb (Central Shallow - Southwest Sandcastle Clam)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Sponge (Central Shallows - East Ledge Near Pufferfish)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Another Crab (Central Shallows - Tall Pillar Near Royal Shellsplitter)", player),
             lambda state: has_grapple(state, player))
    set_rule(multiworld.get_location("Sand Dollar (Central Shallows - South Arch Wall)", player),
             lambda state: has_grapple(state, player))

# Fort Slacktide
    set_rule(multiworld.get_location("Chipclaw (Fort Slacktide - Behind Broken Wall)", player),
             lambda state: has_grapple(state, player) and has_pearl(state, player))
    set_rule(multiworld.get_location("Bloodstar Limb (Slacktide - Clam Above Duchess's Chamber)", player),
             lambda state: has_grapple(state, player) and has_pearl(state, player))
    set_rule(multiworld.get_location("Royal Wave Adaptation (Fort Slacktide - Defeat Magista)", player),
             lambda state: has_grapple(state, player) and has_pearl(state, player))