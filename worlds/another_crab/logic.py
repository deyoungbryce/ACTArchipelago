from typing import TYPE_CHECKING, Dict, List
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState

from .options import ACTGameOptions
from .names import location_names as lname
from .names import item_names as iname
from .names import region_names as rname
from .names import shell_names as sname

if TYPE_CHECKING:
    from . import ACTWorld


#Checks to see if the player can logically consistently deal damage
def can_deal_damage(state: CollectionState,player:int) -> bool:
    return can_rolling_attack(state,player) | can_magic_damage(state,player) | has_summon(state,player) | state.has(iname.fork) | can_atk_damage_shell(state,player)


def can_rolling_attack(state: CollectionState, player: int) -> bool:
    return can_reach_rolling_shells(state,player) and (state.has(iname.lil_isopod,player,2))

#Checks if the player has any of the summonable fish stowaways
def has_summon(state: CollectionState, player: int) -> bool:
    return state.has_any({iname.chum,iname.lanternfish,iname.fredrick},player)

#Checks if the player has adaptations
#Skips Snail Sanctum since it needs lvl 2 to deal damage
#Skips Tactical Tentacle since it may need the fork to attack
#Skips Bobbit Trap since it may not do enough dmg at lvl 1
def has_adaptation(state: CollectionState, player: int) -> bool:
    return state.has_any({iname.royal_wave, iname.urchin_toss, iname.mantis_punch, iname.bubble_bullet, iname.eelectrocute})

def can_magic_damage(state: CollectionState, player: int) -> bool:
    return (can_reach_magic_shells(state,player) | has_adaptation(state,player)) and can_regen_umami(state,player)

def can_regen_umami(state: CollectionState, player: int) -> bool:
    return state.has_any_count({[iname.phytoplankton_plus,1],[iname.zooplankton,2],[iname.zooplankton_plus,1],[iname.phytoplankton_plus,2]},player)

def can_reach_magic_shells(state: CollectionState, player: int) -> bool:
    return state.has(sname.soda_can) | state.has(sname.bottle_cap)

def can_reach_rolling_shells(state: CollectionState, player: int) -> bool:
    return state.has(sname.soda_can) | state.has(sname.bottle_cap)

def can_atk_damage_shell(state: CollectionState, player: int) -> bool:
    twist_top: bool = state.has(sname.sauce_nozzle) | state.has(sname.shuttlecock) | state.has(sname.felix_cube) | state.has(sname.dish_scrubber)
    pop_off: bool = state.has(sname.bottle_cap) | state.has(sname.f_key) | state.has(sname.ham_tin) | state.has(sname.legal_brick) | state.has(sname.spring) | state.has(sname.detergent_cap)
    rollout: bool = state.has(sname.coconut) | state.has(sname.tennis_ball) | state.has(sname.dumptruck) | state.has(sname.gacha_capsule) | state.has(sname.ultrasoft)
    return twist_top | (pop_off and state.has(iname.sponge,player,2)) | (rollout and state.has(iname.sponge,player,2))