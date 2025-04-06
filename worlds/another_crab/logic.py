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


#world: ACTWorld  #= ACTWorld()
# regions_to_exclude = []

# def set_options (options: ACTGameOptions):
#     if options.goal == "roland":
#         regions_to_exclude = [rname.unfathom,rname.plains,rname.old_ocean,rname.drain_bottom,rname.trash_island,rname.carcinia_ruins]

#     if options.goal == "voltai":
#         regions_to_exclude = [rname.pinbarge,rname.unfathom,rname.plains,rname.old_ocean,rname.drain_bottom,rname.trash_island,rname.carcinia_ruins]

#     if options.goal == "magista":
#         regions_to_exclude = [rname.reefs_edge,rname.new_carcinia,rname.sands_between,rname.post_pag,rname.secluded_ridge,rname.expired_grove,rname.grove_main,rname.grove_village,rname.flotsam_vale,rname.scuttleport,rname.pinbarge,rname.unfathom,rname.plains,rname.old_ocean,rname.drain_bottom,rname.trash_island,rname.carcinia_ruins]





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
    rolling_shells = [sname.soda_can,sname.bottle_cap,sname.lil_red_cup,sname.shuttlecock,sname.bebop_cup,sname.tin_can,sname.shot_glass,sname.party_hat,sname.coconut,sname.teacup,sname.sauce_nozzle,sname.thimble,sname.tennis_ball,sname.mason_jar,sname.salt_shaker,sname.conchiglie,sname.disco_ball,sname.lil_bro,sname.matryoshka_large,sname.wafer_cone,sname.yoccult,sname.coffee_pod,sname.egg_shell,sname.coffee_mug,sname.cascadia_roll,sname.skull,sname.spring,sname.shotgun_shell,sname.dumptruck,sname.gacha_capsule,sname.lightbulb,sname.doll_head,sname.service_bell,sname.party_popper,sname.scrub_aggie,sname.pill_bottle,sname.detergent_cap,sname.ultrasoft,sname.champagne_flute,sname.dish_scrubber,sname.snow_globe,sname.knights_helmet,iname.snail_sanctum,sname.plug_fuse,sname.piggy_bank]
    # for shell in rolling_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         rolling_shells.remove(shell)

    return state.has_any(rolling_shells,player)

def can_atk_damage_shell(state: CollectionState, player: int) -> bool:
    sponge_val: int = 0
    sponge_val += state.count(iname.sponge,player)
    sponge_val += state.count(iname.sponge_plus,player) * 2
    return can_twist_top(state,player) | (can_pop_off(state,player) and sponge_val >= 3) | (can_rollout(state,player) and sponge_val >= 3) | (can_party_time(state,player) and sponge_val >= 3)


#Check if Shell Spells are Reachable

#Twist Top
def can_twist_top(state: CollectionState, player: int) -> bool:
    twist_top_shells = [sname.sauce_nozzle, sname.shuttlecock,sname.felix_cube,sname.dish_scrubber]
    # for shell in twist_top_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         twist_top_shells.remove(shell)

    return state.has_any(twist_top_shells,player)

#Pop Off
def can_pop_off(state: CollectionState, player: int) -> bool:
    pop_off_shells = [sname.bottle_cap,sname.f_key,sname.ham_tin,sname.legal_brick,sname.spring,sname.detergent_cap]
    # for shell in pop_off_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         pop_off_shells.remove(shell)
    return state.has_any(pop_off_shells,player)

#Rollout
def can_rollout(state: CollectionState, player: int) -> bool:
    rollout_shells = [sname.coconut,sname.tennis_ball, sname.dumptruck, sname.gacha_capsule, sname.ultrasoft]
    # for shell in rollout_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         rollout_shells.remove(shell)

    return state.has_any(rollout_shells,player)

#Bombs Away
def can_bombs_away(state: CollectionState, player: int) -> bool:
    bombs_away_shells = [sname.bartholomew,sname.shotgun_shell]
    # for shell in bombs_away_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         bombs_away_shells.remove(shell)

    return state.has_any(bombs_away_shells,player)

#Decoy
def can_decoy(state: CollectionState, player: int) -> bool:
    decoy_shells = [sname.matryoshka_large,sname.piggy_bank,sname.crab_husk,sname.rubber_duck]
    # for shell in decoy_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         decoy_shells.remove(shell)

    return state.has_any(decoy_shells,player)

#Fizzle
def can_fizzle(state: CollectionState, player: int) -> bool:
    fizzle_shells = [sname.soda_can,sname.valve,sname.going_under_64]

    # for shell in fizzle_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         fizzle_shells

    return state.has_any(fizzle_shells,player)

#Party Time
def can_party_time(state: CollectionState, player: int) -> bool:
    party_time_shells = [sname.party_hat,sname.trophy,sname.party_popper]

    # for shell in party_time_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         party_time_shells.remove(shell)

    return state.has_any(party_time_shells,player)

#Shards
def can_shards(state: CollectionState, player: int) -> bool:
    shards_shells = [sname.shot_glass,sname.mason_jar,sname.salt_shaker]
    # for shell in shards_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         shards_shells.remove(shell)

    return state.has_any(shards_shells,player)

#Squash
def can_squash(state: CollectionState, player: int) -> bool:
    squash_shells = [sname.boxing_glove,sname.sock]
    # for shell in squash_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         squash_shells.remove(shell)

    return state.has_any(squash_shells,player)

#Twinkle
def can_twinkle(state: CollectionState, player: int) -> bool:
    twinkle_shells = [sname.disco_ball,sname.spirit_conch]
    # for shell in twinkle_shells:
    #     if ACTWorld.multiworld.get_region(ACTWorld.multiworld.find_item(shell,player).parent_region,player).entrances[0].parent_region in regions_to_exclude:
    #         twinkle_shells.remove(shell)

    return state.has_any(twinkle_shells,player)