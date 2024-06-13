from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState

from .options import ACTGameOptions
from .names import location_names as lname
from .names import item_names as iname
if TYPE_CHECKING:
    from . import ACTWorld

def set_region_rules(world: "ACTWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    #options = world.options

    multiworld.get_entrance("Central Shallows -> Moon Snail's Cave", player).access_rule = \
        lambda state: state.has(iname.fishing_line, player)
    
def set_location_rules(world: "ACTWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    #options = world.options

# Central Shallows
    set_rule(multiworld.get_location(lname.breadclaw_shallows_sandcastle, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.breadclaw_shallows_eastledge, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.hairclaw_shallows_turret, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.chipclaw_shallows_sandcastle, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.bloodstar_shallows_clam, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.sponge_shallows_puffer, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.anothercrab_shallows_pillar, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.sanddollar_shallows_arch, player),
             lambda state: state.has(iname.fishing_line, player))

# Fort Slacktide
    set_rule(multiworld.get_location(lname.chipclaw_slacktide_brokenwall, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.bloodstar_slacktide_clam, player),
             lambda state: state.has(iname.fishing_line, player))
    
    set_rule(multiworld.get_location(lname.royal_wave_reward, player),
             lambda state: state.has(iname.fishing_line, player))