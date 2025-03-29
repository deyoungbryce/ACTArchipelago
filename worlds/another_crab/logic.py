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
def can_deal_damage_hard(state: CollectionState,player:int) -> bool:
    return can_rolling_attack(state,player) | can_magic_damage(state,player) | can_atk_damage_shell(state,player) | has_summon(state,player)  | state.has(iname.fork,player)

def can_deal_damage_easy(state: CollectionState,player:int) -> bool:
    return can_magic_damage(state,player) | can_atk_damage_shell(state,player) | state.has(iname.fork,player)


def can_rolling_attack(state: CollectionState, player: int) -> bool:
    return can_reach_rolling_shells(state,player) and (state.has(iname.lil_isopod,player,2))

#Checks if the player has any of the summonable fish stowaways
def has_summon(state: CollectionState, player: int) -> bool:
    summon_count: int = 0
    if state.has(iname.chum,player):
        summon_count += 1
    
    if state.has(iname.fredrick,player):
        summon_count += 1

    if state.has(iname.lanternfish,player):
        summon_count += 1

    return summon_count >= 2

#Checks if the player has adaptations
#Skips Snail Sanctum since it needs lvl 2 to deal damage
#Skips Tactical Tentacle since it may need the fork to attack
#Skips Bobbit Trap since it may not do enough dmg at lvl 1
def has_adaptation(state: CollectionState, player: int) -> bool:
    return state.has_any({iname.royal_wave, iname.urchin_toss, iname.mantis_punch, iname.bubble_bullet, iname.eelectrocute},player)

def can_magic_damage(state: CollectionState, player: int) -> bool:
    return (can_reach_magic_shells(state,player) ) and can_regen_umami(state,player) #| has_adaptation(state,player)

def can_regen_umami(state: CollectionState, player: int) -> bool:
    return state.has_any_count({iname.phytoplankton_plus:1,iname.zooplankton:2,iname.zooplankton_plus:1,iname.phytoplankton_plus:2},player)

def can_reach_magic_shells(state: CollectionState, player: int) -> bool:
    return can_twist_top(state,player) | can_pop_off(state,player) | can_rollout(state,player) | can_fizzle(state,player) | can_party_time(state,player) | can_shards(state,player) | can_squash(state,player) | can_twinkle(state,player)

def can_reach_msg_dmg_shells(state: CollectionState, player: int) -> bool:
    return can_fizzle(state,player) | can_party_time(state,player) | can_shards(state,player) | can_squash(state,player) | can_twinkle(state,player)

def can_reach_rolling_shells(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.soda_can,sname.bottle_cap,sname.lil_red_cup,sname.shuttlecock,sname.bebop_cup,sname.tin_can,sname.shot_glass,sname.party_hat,sname.coconut,sname.teacup,sname.sauce_nozzle,sname.thimble,sname.tennis_ball,sname.mason_jar,sname.salt_shaker,sname.conchiglie,sname.disco_ball,sname.lil_bro,sname.matryoshka_large,sname.wafer_cone,sname.yoccult,sname.coffee_pod,sname.egg_shell,sname.coffee_mug,sname.cascadia_roll,sname.skull,sname.spring,sname.shotgun_shell,sname.dumptruck,sname.gacha_capsule,sname.lightbulb,sname.doll_head,sname.service_bell,sname.party_popper,sname.scrub_aggie,sname.pill_bottle,sname.detergent_cap,sname.ultrasoft,sname.champagne_flute,sname.dish_scrubber,sname.snow_globe,sname.knights_helmet,iname.snail_sanctum,sname.plug_fuse,sname.piggy_bank},player)

def can_atk_damage_shell(state: CollectionState, player: int) -> bool:
    sponge_val: int = 0
    sponge_val += state.count(iname.sponge,player)
    sponge_val += state.count(iname.sponge_plus,player) * 2
    return can_twist_top(state,player) | (can_pop_off(state,player) and sponge_val >= 3) | (can_rollout(state,player) and sponge_val >= 3) | (can_party_time(state,player) and sponge_val >= 3)


#Check if Shell Spells are Reachable
def can_twist_top(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.sauce_nozzle, sname.shuttlecock,sname.felix_cube,sname.dish_scrubber},player)

def can_pop_off(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.bottle_cap,sname.f_key,sname.ham_tin,sname.legal_brick,sname.spring,sname.detergent_cap},player)

def can_rollout(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.coconut,sname.tennis_ball, sname.dumptruck, sname.gacha_capsule, sname.ultrasoft},player)

def can_bombs_away(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.bartholomew,sname.shotgun_shell},player)

def can_decoy(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.matryoshka_large,sname.matryoshka_medium,sname.matryoshka_small,sname.piggy_bank,sname.crab_husk,sname.rubber_duck},player)

def can_fizzle(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.soda_can,sname.valve,sname.going_under_64},player)

def can_party_time(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.party_hat,sname.trophy,sname.party_popper},player)

def can_shards(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.shot_glass,sname.mason_jar,sname.salt_shaker},player)

def can_squash(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.boxing_glove,sname.sock},player)

def can_twinkle(state: CollectionState, player: int) -> bool:
    return state.has_any({sname.disco_ball,sname.spirit_conch},player)