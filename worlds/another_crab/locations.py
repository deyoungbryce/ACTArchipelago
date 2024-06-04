from typing import Dict, NamedTuple, Set, Optional
from BaseClasses import Location

from .names import location_names as lname
from .names import region_names as rname

class ACTLocation(Location):
    game: str = "Another Crabs Treasure"

location_base_id = 483021700

class ACTLocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None

location_table: Dict[str, ACTLocationData] = {
    # starting item locations (will probably just include heartkelp_initial and fork pickup because they are the items you pick up right at the beginning of the game)

    # Last used number: 46
    #lname.heartkelp_inital: ACTLocationData(rname.tide_pools, "Starting Items"),#950e628c-f657-48d4-b93b-f8717627f6b3-2_A-ShallowsTidePools
    #lname.fork_pickup: ACTLocationData(rname.starting_cave, 1,"Starting Items"),#73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools

    # progression item locations
    lname.fishing_line: ACTLocationData(rname.slacktide_before, 2, "Fort Slacktide - Before Destruction"),
    lname.pristine_pearl: ACTLocationData(rname.snail_cave, 3, "Moon Snail's Cave"),
    
    # currency item locations

    lname.breadclaw_caveofrespite_ledge: ACTLocationData(rname.starting_cave, 4,"Cave of Respite"),#73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools

    lname.breadclaw_shallows_southsandal: ACTLocationData(rname.central_shallows, 5, "Central Shallows"),#0171a152-809a-47cf-9fcc-60ddb61511bb-2_B-ShallowsBigSand
    lname.breadclaw_shallows_westwall: ACTLocationData(rname.central_shallows, 6, "Central Shallows"), #ae27274c-c3f7-4721-9ddb-7c5a880578a4-2_B-ShallowsBigSand
    lname.breadclaw_shallows_bridge: ACTLocationData(rname.central_shallows, 7, "Central Shallows"), #8b269a88-c6d1-4b2a-8e5f-9d60c6d6fd15-2_B-ShallowsBigSand
    lname.breadclaw_shallows_eastwall: ACTLocationData(rname.central_shallows, 8, "Central Shallows"), #6aba5604-8269-46a5-b734-ef4dc3983265-2_B-ShallowsBigSand
    lname.breadclaw_shallows_eastsandal: ACTLocationData(rname.central_shallows, 9, "Central Shallows"), #889c343a-b969-4295-b059-a837fc457444-2_B-ShallowsBigSand
    lname.breadclaw_shallows_cigarette: ACTLocationData(rname.central_shallows, 10, "Central Shallows"), #d1ddf122-d283-4509-8bfa-bff8fa209f35-2_B-ShallowsBigSand
    lname.breadclaw_shallows_fortwall: ACTLocationData(rname.central_shallows, 11, "Central Shallows"), #20bede55-9eae-40a3-a80a-63ee5b52d0bf-2_B-ShallowsBigSand
    lname.breadclaw_shallows_wallpiece: ACTLocationData(rname.central_shallows, 12, "Central Shallows"), #5732b602-c599-41b5-bc5d-93e88277a4b7-2_B-ShallowsBigSand
    lname.breadclaw_shallows_sandcastle: ACTLocationData(rname.central_shallows, 13, "Central Shallows"), #984eda06-d10e-4b2b-a5c4-389784ed18f6-2_B-ShallowsBigSand
    lname.breadclaw_shallows_eastledge: ACTLocationData(rname.central_shallows, 14, "Central Shallows"), #51dbcbfd-4a82-4c22-b2ee-1a03deeca4cc-2_B-ShallowsBigSand
    lname.hairclaw_shallows_turret: ACTLocationData(rname.central_shallows, 15, "Central Shallows"), #b2d21ade-41ab-47fc-960b-0beb6d07359d-2_B-ShallowsBigSand
    lname.chipclaw_shallows_sandcastle: ACTLocationData(rname.central_shallows, 16, "Central Shallows"), #12c6e5c5-eee1-4f9a-a3c4-68c2bd098a14-2_B-ShallowsBigSand
    lname.clothesclaw_shallows_shellsplitter: ACTLocationData(rname.central_shallows, 17, "Central Shallows"), #AUTO NEEDS TO DO BOSS SCRIPT
    lname.clothesclaw_shallows_southwestfort: ACTLocationData(rname.central_shallows, 45, "Central Shallows"), #e13e2c76-a638-4023-aa84-f6f29fd7bf65-2_B-ShallowsBigSand

    lname.breadclaw_slacktide_crates: ACTLocationData(rname.slacktide_before, 18, "Fort Slacktide - Before Destruction"), #8c1e68dc-eb15-41f4-9a5d-c1b20dd76f52-2_B-ShallowsBigSand

    lname.breadclaw_snailcave_entrance: ACTLocationData(rname.snail_cave, 19, "Moon Snail's Cave"), #5bb2169d-f820-41f0-9783-336c006861c6-2_D-MoonSnailShellCave
    lname.breadclaw_snailcave_shortcut: ACTLocationData(rname.snail_cave, 20, "Moon Snail's Cave"), #436eff44-09df-451e-93c8-3a5714ec55c2-2_D-MoonSnailShellCave
    lname.breadclaw_snailcave_jelly: ACTLocationData(rname.snail_cave, 21, "Moon Snail's Cave"), #07977d86-44ec-40d0-b331-8b45b1d44838-2_D-MoonSnailShellCave

    lname.breadclaw_slacktide_crabtrio: ACTLocationData(rname.slacktide_after, 22, "Fort Slacktide - After Destruction"), #2af7f575-51f3-4da9-b3bf-eab9d32a3bd8-2_C-Slacktide2
    lname.chipclaw_slacktide_brokenwall: ACTLocationData(rname.slacktide_after, 23, "Fort Slacktide - After Destruction"), #45f42ae3-41b6-4333-875f-3a9e8387e087-2_C-Slacktide2

    # upgrade item locations
    lname.bloodstar_shallows_help: ACTLocationData(rname.central_shallows, 24, "Central Shallows"), #AUTO NEEDS TO DO QUEST SCRIPT
    lname.bloodstar_shallows_parkour: ACTLocationData(rname.central_shallows, 25, "Central Shallows"),#ff9d47b6-7f55-4ad2-a110-e7c4492d87c1-2_B-ShallowsBigSand
    lname.bloodstar_shallows_bridge: ACTLocationData(rname.central_shallows, 26, "Central Shallows"),#32fb25ee-9262-4e87-98f9-2e64d369e7ae-2_B-ShallowsBigSand
    lname.bloodstar_shallows_clam: ACTLocationData(rname.central_shallows, 27, "Central Shallows"), #0474f3a7-0eb7-4d3c-b61e-cbb782ceab03-2_B-ShallowsBigSand

    lname.kelpsprout_snailcave_elevator: ACTLocationData(rname.snail_cave, 28, "Moon Snail's Cave"), #15a2e4c0-4950-4de0-8b5c-e2b1400f76c1-2_D-MoonSnailShellCave
    lname.bloodstar_snailcave_platoon: ACTLocationData(rname.snail_cave, 29, "Moon Snail's Cave"), #00fc94c3-320c-4d0a-a4e0-2b5eccd42d55-2_D-MoonSnailShellCave

    lname.bloodstar_slacktide_clam: ACTLocationData(rname.slacktide_after, 30, "Fort Slacktide - After Destruction"), #451b4cfb-7176-4103-999f-358b09374e0c-2_B-ShallowsBigSand

    # stowaway locations
    lname.siphonophore_shallows_westwall: ACTLocationData(rname.central_shallows, 31, "Central Shallows"),#4d4ac114-06e4-400f-b888-b500a7348cc9-2_B-ShallowsBigSand
    lname.seastar_shallows_eastledge: ACTLocationData(rname.central_shallows, 32, "Central Shallows"), #e9a5a6cf-2a19-4db5-bb0d-d85b260f3e2b-2_B-ShallowsBigSand
    lname.sponge_shallows_puffer: ACTLocationData(rname.central_shallows, 33, "Central Shallows"), #95c0077d-518f-4ab7-85e2-ac1e0c1bb0b9-2_B-ShallowsBigSand
    lname.anothercrab_shallows_pillar: ACTLocationData(rname.central_shallows, 34, "Central Shallows"), #924670c2-839f-4e42-9cf5-8c081b17f946-2_B-ShallowsBigSand
    lname.sanddollar_shallows_arch: ACTLocationData(rname.central_shallows, 35, "Central Shallows"), #804d3848-3e86-474f-8622-547d020c4cc4-2_B-ShallowsBigSand

    lname.limpet_slacktide_stairs: ACTLocationData(rname.slacktide_before, 36, "Fort Slacktide - Before Destruction"), #b5e751fb-8ff5-440e-aa9c-9d9c75977be7-2_B-ShallowsBigSand
    lname.seastar_slacktide_grappleroom: ACTLocationData(rname.slacktide_before, 37, "Fort Slacktide - Before Destruction"), #35603032-802e-4811-ae95-8e8eb11c1dfa-2_B-ShallowsBigSand
    lname.barnacle_slacktide_bigurchin: ACTLocationData(rname.slacktide_before, 38, "Fort Slacktide - Before Destruction"), #98329dde-9889-4cbb-a656-61f83dca2eca-2_B-ShallowsBigSand

    lname.limpet_snailcave_jelly: ACTLocationData(rname.snail_cave, 39, "Moon Snail's Cave"), #c1a31dc1-9ec5-42e9-8dcf-291f7cdc8a26-2_D-MoonSnailShellCave

    lname.mussel_slacktide_fortentrance: ACTLocationData(rname.slacktide_after, 40, "Fort Slacktide - After Destruction"), #694c4c66-fefc-4539-962f-a343e13b044b-2_C-Slacktide2
    lname.anemone_slacktide_fortwall: ACTLocationData(rname.slacktide_after, 41, "Fort Slacktide - After Destruction"), #557546a8-096b-49cd-b63b-452fb751a8bf-2_C-Slacktide2
    lname.whelk_slacktide_turrettop: ACTLocationData(rname.slacktide_after, 42, "Fort Slacktide - After Destruction"), #e1848736-945b-406d-853e-d213f7c80f14-2_C-Slacktide2

    # costume locations
    lname.captain_costume_pickup: ACTLocationData(rname.central_shallows, 43, "Central Shallows"),#7c307763-a7b4-4e81-88d6-e1baf1b04608-2_B-ShallowsBigSand

    # adaptation locations
    lname.royal_wave_reward: ACTLocationData(rname.slacktide_after, 44, "Fort Slacktide - After Destruction") #AUTO NEEDS TO DO BOSS SCRIPT
}

location_name_to_id: Dict[str, int] = {name: location_base_id + data.location_id_offset for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)