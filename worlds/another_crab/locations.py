from typing import Dict, NamedTuple, Set, Optional
from BaseClasses import Location

from .names import location_names as lname
from .names import region_names as rname

class ACTLocation(Location):
    game: str = "Another Crabs Treasure"

location_base_id: int = 483021700

class ACTLocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


location_table: Dict[str, ACTLocationData] = {
    # starting item locations (will probably just include heartkelp_initial and fork pickup because they are the items you pick up right at the beginning of the game)


    #Last used number: 316

    #lname.heartkelp_inital: ACTLocationData("Tide Pools", "Starting Items"),#950e628c-f657-48d4-b93b-f8717627f6b3-2_A-ShallowsTidePools
    #lname.fork_pickup: ACTLocationData("Cave of Respite", 1,"Starting Items"),#73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools

    # progression item locations
    lname.fishing_line: ACTLocationData(rname.slacktide_before, 2, "Fort Slacktide - Before Destruction"),
    #lname.pristine_pearl: ACTLocationData(rname.snail_cave, x, "Moon Snail's Cave"), #Redundant, overlaps with Platoon Pathfinder

    # boss locations
    lname.nephro: ACTLocationData(rname.central_shallows, 3, "Central Shallows"),
    lname.platoon_pathfinder: ACTLocationData(rname.snail_cave, 46, "Moon Snail's Cave"),
    lname.magista: ACTLocationData(rname.slacktide_after, 44, "Fort Slacktide - After Destruction"),
    lname.royal_shellsplitter: ACTLocationData(rname.central_shallows, 47, "Central Shallows"),
    lname.pagurus: ACTLocationData(rname.sands_between, 48, "Sands Between"),
    lname.lichenthrope: ACTLocationData(rname.grove_main, 253, "Expired Grove Main"), #must fix region name and location group before re-adding
    lname.carbonara_connoisseur: ACTLocationData(rname.grove_main, 254, "Expired Grove Main"),
    lname.heikea: ACTLocationData(rname.grove_main, 255, "Expired Grove Main"),
    lname.topoda: ACTLocationData(rname.central_shallows, 52, "Central Shallows"),
    #lname.consortium: ACTLocationData(rname.central_shallows, 53, "Central Shallows"),
    #lname.sludge_steamroller: ACTLocationData(rname.central_shallows, 54, "Central Shallows"),
    #lname.ceviche_sisters: ACTLocationData(rname.central_shallows, 55, "Central Shallows"),
    #lname.voltai: ACTLocationData(rname.central_shallows, 56, "Central Shallows"),
    #lname.roland: ACTLocationData(rname.central_shallows, 57, "Central Shallows"),
    #lname.petroch: ACTLocationData(rname.central_shallows, 58, "Central Shallows"),
    #lname.inkerton: ACTLocationData(rname.central_shallows, 59, "Central Shallows"),
    #lname.camtscha: ACTLocationData(rname.central_shallows, 60, "Central Shallows"),
    #lname.praya_dubia: ACTLocationData(rname.central_shallows, 61, "Central Shallows"),
    #lname.firth: ACTLocationData(rname.central_shallows, 62, "Central Shallows"),
    
    ##### currency item locations

    lname.breadclaw_caveofrespite_ledge: ACTLocationData(rname.starting_cave, 4,"Cave of Respite"), #73329d8e-7c96-4e82-9d3c-e57cc61b46b4-2_A-ShallowsTidePools
    lname.chipclaw_caveofrespite_forkroomfishing: ACTLocationData(rname.starting_cave, 120,"Cave of Respite"), #d985ffba-0ece-414d-8161-fa65241dd2b1-2_B-ShallowsBigSand
    lname.mussel_caveofrespite_crabfightfishing: ACTLocationData(rname.starting_cave, 121,"Cave of Respite"), #d1af097b-c6c9-44a4-9ced-4a09a973c0d5-2_B-ShallowsBigSand
    lname.clothesclaw_caveofrespite_entrancefishing: ACTLocationData(rname.starting_cave, 122,"Cave of Respite"), #0ac3fa03-5aab-4f12-86e4-8e9dfde8c04f-2_B-ShallowsBigSand
    lname.sanddollar_caveofrespite_pathfishing: ACTLocationData(rname.starting_cave, 123,"Cave of Respite"), #9ef4b1f3-5a80-408c-962a-b3fed8c68770-2_B-ShallowsBigSand

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
    lname.breadclaw_shallows_sunkentower: ACTLocationData(rname.central_shallows, 124, "Central Shallows"), #1e33dfd0-6445-47f9-b1bf-3e8be7897a79-2_B-ShallowsBigSand
    lname.breadclaw_shallows_slacktidesouthfish: ACTLocationData(rname.central_shallows, 126, "Central Shallows"), #0f64d031-4163-4979-9497-116cac06e234-2_B-ShallowsBigSand


    lname.breadclaw_slacktide_crates: ACTLocationData(rname.slacktide_before, 18, "Fort Slacktide - Before Destruction"), #8c1e68dc-eb15-41f4-9a5d-c1b20dd76f52-2_B-ShallowsBigSand
    lname.breadclaw_slacktide_training: ACTLocationData(rname.slacktide_before, 130, "Fort Slacktide - Before Destruction"), #0ad90b46-ca8b-46ed-9cc6-f72ffcdb9d33-2_B-ShallowsBigSand

    lname.breadclaw_snailcave_entrance: ACTLocationData(rname.snail_cave, 19, "Moon Snail's Cave"), #5bb2169d-f820-41f0-9783-336c006861c6-2_D-MoonSnailShellCave
    lname.breadclaw_snailcave_shortcut: ACTLocationData(rname.snail_cave, 20, "Moon Snail's Cave"), #436eff44-09df-451e-93c8-3a5714ec55c2-2_D-MoonSnailShellCave
    lname.breadclaw_snailcave_jelly: ACTLocationData(rname.snail_cave, 21, "Moon Snail's Cave"), #07977d86-44ec-40d0-b331-8b45b1d44838-2_D-MoonSnailShellCave

    lname.breadclaw_slacktide_crabtrio: ACTLocationData(rname.slacktide_after, 22, "Fort Slacktide - After Destruction"), #2af7f575-51f3-4da9-b3bf-eab9d32a3bd8-2_C-Slacktide2
    lname.chipclaw_slacktide_brokenwall: ACTLocationData(rname.slacktide_after, 23, "Fort Slacktide - After Destruction"), #45f42ae3-41b6-4333-875f-3a9e8387e087-2_C-Slacktide2
    lname.breadclaw_slacktide_roofhiddenfish: ACTLocationData(rname.slacktide_after, 131, "Fort Slacktide - After Destruction"), #59e2ec5a-b650-43fa-879d-3af1569fb640-2_B-ShallowsBigSand

    lname.chipclaw_reefsedge_brokenbridge: ACTLocationData(rname.reefs_edge, 63, "Reef's Edge"), #e9bf56b8-1362-42a9-87a2-00bed3a6f5d2-2_A-NCTradeRoute
    lname.breadclaw_reefsedge_thimblecrab: ACTLocationData(rname.reefs_edge, 67, "Reef's Edge"), #1f5a8d6b-10ab-4e4e-b240-284e2ec2c77a-2_A-NCTradeRoute
    lname.hairclaw_reefsedge_sign: ACTLocationData(rname.reefs_edge, 71, "Reef's Edge"), #b478df52-084c-4c14-8a55-215fdbaeaffe-2_A-NCTradeRoute

    lname.breadclaw_newcarcinia_entrance: ACTLocationData(rname.new_carcinia, 74, "New Carcinia"), #fb5e2e88-b498-4af4-b7a6-4f176eb4016c-2_B-NCCity
    lname.breadclaw_newcarcinia_hammerhead: ACTLocationData(rname.new_carcinia, 76, "New Carcinia"), #e26a7cee-15af-4f6c-b6fb-253f8dfac6e4-2_B-NCCity
    lname.breadclaw_newcarcinia_bottomalley: ACTLocationData(rname.new_carcinia, 79, "New Carcinia"), #4058fdd6-84f5-4f1e-b8f1-3dcccb288aa2-2_B-NCCity
    lname.breadclaw_newcarcinia_prawnalley: ACTLocationData(rname.new_carcinia, 80, "New Carcinia"), #d538af5f-81e0-452c-8800-756bb635a16b-2_B-NCCity
    lname.chipclaw_newcarcinia_leg: ACTLocationData(rname.new_carcinia, 81, "New Carcinia"), #4f62e34e-df79-4e33-99bb-b65844e50304-2_B-NCCity
    lname.breadclaw_newcarcinia_tallbuilding: ACTLocationData(rname.new_carcinia, 82, "New Carcinia"), #0e59ec85-36b5-4750-baf4-cc9899525ca6-2_B-NCCity
    lname.breadclaw_newcarcinia_shortbuilding: ACTLocationData(rname.new_carcinia, 83, "New Carcinia"), #c91a3fa0-f774-4e5f-a43e-90dd9a1d5e3a-2_B-NCCity
    lname.chipclaw_newcarcinia_prawnshop: ACTLocationData(rname.new_carcinia, 84, "New Carcinia"), #d2b95a55-ec16-48cc-bce4-c7e39a16a78a-2_B-NCCity

    lname.breadclaw_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 87, "The Sands Between"), #4a22c058-bbb2-467a-b204-9c1a82dc0d9c-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southernreef: ACTLocationData(rname.sands_between, 94, "The Sands Between"), #cc1a7d82-3803-474e-8f66-c149055c4cb9-2_A-OOGroveRadius
    lname.chipclaw_sandsbetween_grove: ACTLocationData(rname.sands_between, 102, "The Sands Between"), #0bae76f4-e90b-435b-9089-356ef62ba0fa-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_chains: ACTLocationData(rname.sands_between, 106, "The Sands Between"), #d78747bd-2da0-4421-add8-3c5842fa0f61-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_bobbit: ACTLocationData(rname.sands_between, 107, "The Sands Between"), #e128b8e9-0c20-426f-8f47-783043f829dc-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_bobbit: ACTLocationData(rname.sands_between, 108, "The Sands Between"), #8d9edda5-d554-4e75-8842-8239075a334a-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_northwest: ACTLocationData(rname.sands_between, 111, "The Sands Between"), #7e93197a-47f1-4bdd-b7f0-5d0ecffb39f4-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_grove: ACTLocationData(rname.sands_between, 112, "The Sands Between"), #cd2f3731-b9f4-4f88-abd2-44d142eca493-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_propanecliff: ACTLocationData(rname.sands_between, 135, "The Sands Between"), #f553b94c-14ea-4852-8ae7-564b8d30b24d-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_northchains: ACTLocationData(rname.sands_between, 137, "The Sands Between"), #7e4ef7d0-214a-4358-a0c3-866a869d71e0-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_litterpitfall: ACTLocationData(rname.sands_between, 138, "The Sands Between"), #9faef117-fd92-47cb-b4d8-cc2a07404a69-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southgrovepit: ACTLocationData(rname.sands_between, 139, "The Sands Between"), #305be10e-d5a7-42e6-88f1-2cebdd524bbb-2_A-OOGroveRadius
    lname.paperclaw_sandsbetween_southeelshortcut: ACTLocationData(rname.sands_between, 147, "The Sands Between"), #0e2d558b-26a7-4213-be83-77355fe06128-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southeel: ACTLocationData(rname.sands_between, 150, "The Sands Between"), #5c8133eb-ddb3-4b24-9849-f4d3f03491e0-2_A-OOGroveRadius
    lname.paperclaw_sandsbetween_trashanchor: ACTLocationData(rname.sands_between, 155, "The Sands Between"), #98e4d994-92c4-4b3b-82b7-f460a49d604b-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_anchorfish: ACTLocationData(rname.sands_between, 156, "The Sands Between"), #cab91803-4006-456d-95c7-6ec17d90c26a-2_A-OOGroveRadius
    lname.chipclaw_sandsbetween_northeastchainfish: ACTLocationData(rname.sands_between, 157, "The Sands Between"), #b0bf9c58-ff96-404c-bd1b-361fb1711b64-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_propanefish: ACTLocationData(rname.sands_between, 158, "The Sands Between"), #17b29697-5b33-4568-a311-2dbfac60317a-2_A-OOGroveRadius
    lname.clothesclaw_sandsbetween_anchorcentralfish: ACTLocationData(rname.sands_between, 160, "The Sands Between"), #628bf319-c5f3-448b-8ec0-71a173246a09-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_nailfish: ACTLocationData(rname.sands_between, 162, "The Sands Between"), #98c3bf98-c4bd-4c67-8678-0464e7095970-2_A-OOGroveRadius
    lname.breadclaw_sandsbetween_palletfish: ACTLocationData(rname.sands_between, 163, "The Sands Between"), #69ac316d-8d42-48a4-8d55-4ec4d6429c7c-2_A-OOGroveRadius
    lname.hairclaw_sandsbetween_southeelfish: ACTLocationData(rname.sands_between, 164, "The Sands Between"), #38edc1a4-dea8-4000-8683-6cda7f6ba3bc-2_A-OOGroveRadius
    lname.chipclaw_sandsbetween_anchoreelhiddenfish: ACTLocationData(rname.sands_between, 165, "The Sands Between"), #01999bed-4813-4fe3-ab9b-5ed19cce90f1-2_A-OOGroveRadius

    lname.stapleclaw_postpag_litter: ACTLocationData(rname.post_pag, 170, "The Sands Between - Post Pagurus"), #e872d437-5bdb-4e70-820a-030bc21d66d5-2_A-OOGroveRadius
    lname.hairclaw_postpag_chains: ACTLocationData(rname.post_pag, 171, "The Sands Between - Post Pagurus"), #4e9d02aa-75f5-4b87-b029-6ee1e7d62f7a-2_A-OOGroveRadius
    lname.clothesclaw_postpag_chains: ACTLocationData(rname.post_pag, 172, "The Sands Between - Post Pagurus"), #2fa3fdd0-b3da-4c69-b579-a5d316075635-2_A-OOGroveRadius
    lname.hairclaw_postpag_nridge: ACTLocationData(rname.post_pag, 179, "The Sands Between - Post Pagurus"), #55fafe55-5d22-49a8-8b2b-aea149468a61-2_A-OOGroveRadius
    lname.hairclaw_postpag_ecentral: ACTLocationData(rname.post_pag, 180, "The Sands Between - Post Pagurus"), #c2d06d3f-65f4-46cf-b069-0b4098b425d0-2_A-OOGroveRadius
    lname.chipclaw_postpag_nwpropane: ACTLocationData(rname.post_pag, 182, "The Sands Between - Post Pagurus"), #45af0c47-a8e0-498f-8345-9c9ddabbd6b3-2_A-OOGroveRadius
    lname.paperclaw_postpag_schain: ACTLocationData(rname.post_pag, 185, "The Sands Between - Post Pagurus"), #16dfae13-103f-45eb-9661-3e6463a2b805-2_A-OOGroveRadius

    lname.clothesclaw_ridge_neridge: ACTLocationData(rname.secluded_ridge, 189, "The Sands Between - Secluded Ridge"), #e2803d8a-feea-45a7-addf-3330748d9e4b-2_A-OOGroveRadius
    lname.paperclaw_ridge_nearoverlook: ACTLocationData(rname.secluded_ridge, 193, "The Sands Between - Secluded Ridge"), #f6db9d48-5df1-4a7f-9f17-b760901954c9-2_A-OOGroveRadius
    lname.clothesclaw_ridge_broom: ACTLocationData(rname.secluded_ridge, 195, "The Sands Between - Secluded Ridge"), #3f8d4c85-202f-42dc-9105-434d601d1d75-2_A-OOGroveRadius
    lname.breadclaw_ridge_south: ACTLocationData(rname.secluded_ridge, 197, "The Sands Between - Secluded Ridge"), #d1883b57-b339-4c31-826a-e76a3de0ee4b-2_A-OOGroveRadius
    lname.clothesclaw_ridge_overlookfish: ACTLocationData(rname.secluded_ridge, 206, "The Sands Between - Secluded Ridge"), #4f737f9e-a952-490c-b54d-1f74735af9cc-2_A-OOGroveRadius
    lname.chipclaw_ridge_southfish: ACTLocationData(rname.secluded_ridge, 207, "The Sands Between - Secluded Ridge"), #82043889-30eb-45f4-8f87-45dd2f5d69ed-2_A-OOGroveRadius

    lname.stapleclaw_trashbin_eelfish: ACTLocationData(rname.secluded_ridge, 209, "The Sands Between - Trashbin Plataeu"), #190034bb-c13e-42ec-bac4-037cc828fde3-2_A-OOGroveRadius

    lname.breadclaw_grovemain_takeout: ACTLocationData(rname.grove_main, 219, "Expired Grove Main"), #4933d4b0-a56a-4472-b9a6-4469fd335fa4-2_A-GroveForestLow
    lname.breadclaw_grovemain_tiretop: ACTLocationData(rname.grove_main, 224, "Expired Grove Main"), #da04ed8f-2d99-48f9-8412-67748d983d2b-2_A-GroveForestLow
    lname.chipclaw_grovemain_plastic: ACTLocationData(rname.grove_main, 225, "Expired Grove Main"), #902c2deb-1b51-4226-9fd0-1c76bea668c3-2_A-GroveForestLow
    lname.clothesclaw_grovemain_choccymilk: ACTLocationData(rname.grove_main, 226, "Expired Grove Main"), #e38ef2da-daaf-4312-bf7f-2e0a97d3d67b-2_A-GroveForestLow
    lname.breadclaw_grovemain_insidetire: ACTLocationData(rname.grove_main, 227, "Expired Grove Main"), #def84515-cfc0-4124-a1e1-81f6953b0c06-2_A-GroveForestLow
    lname.chipclaw_grovemain_sniper: ACTLocationData(rname.grove_main, 245, "Expired Grove Main"), #070b84a6-7a8b-4d88-8216-f55882856713-2_A-GroveForestLow
    lname.hairclaw_grovemain_milkurchins: ACTLocationData(rname.grove_main, 246, "Expired Grove Main"), #e78f03e8-2827-45d7-8cfa-cbaa0f17cd3d-2_A-GroveForestLow
    lname.breadclaw_grovemain_smallhall: ACTLocationData(rname.grove_main, 231, "Expired Grove Main"), #be378f83-9ec2-4a3b-85b2-9a7499e6d693-2_A-GroveForestLow
    lname.chipclaw_grovemain_apples: ACTLocationData(rname.grove_main, 232, "Expired Grove Main"), #faa3c9ce-87c7-4f6d-b07e-be334c3bc447-2_A-GroveForestLow
    lname.chipclaw_grovemain_sodacans: ACTLocationData(rname.grove_main, 233, "Expired Grove Main"), #25737275-a222-4a6e-af6b-0c66c197cab7-2_A-GroveForestLow
    lname.hairclaw_grovemain_moonshine: ACTLocationData(rname.grove_main, 234, "Expired Grove Main"), #fd557b69-ddba-4b14-bd80-f0cb0d786203-2_A-GroveForestLow
    lname.chipclaw_grovemain_circlerock: ACTLocationData(rname.grove_main, 238, "Expired Grove Main"), #1b74ef4f-528c-484b-9a5f-abbb3434f133-2_A-GroveForestLow
    lname.clothesclaw_grovemain_alcove: ACTLocationData(rname.grove_main, 239, "Expired Grove Main"), #f99a120b-43c2-4e65-91fd-71cbfbf3e8f7-2_A-GroveForestLow
    lname.hairclaw_grovemain_sniper: ACTLocationData(rname.grove_main, 240, "Expired Grove Main"), #8f4a1f33-e567-4c84-b34b-739353b3ba08-2_A-GroveForestLow
    lname.breadclaw_grovemain_amongus: ACTLocationData(rname.grove_main, 243, "Expired Grove Main"), #c859129f-cc29-4624-a161-fdeffa00d0ca-2_B-GroveForestHigh
    lname.breadclaw_grovemain_oildrum: ACTLocationData(rname.grove_main, 244, "Expired Grove Main"), #b85cb09c-f1d7-4396-85cb-fde4dc845acd-2_B-GroveForestHigh
    lname.breadclaw_grovemain_oilgrapple: ACTLocationData(rname.grove_main, 249, "Expired Grove Main"), #bc18b92b-a6c6-420c-9095-e15c34c2f921-2_B-GroveForestHigh
    lname.clothesclaw_grovemain_mantisfish: ACTLocationData(rname.grove_main, 256, "Expired Grove Main"), #048736b5-59c1-4dd2-b36a-e11b6bd9304f-2_A-GroveForestLow
    lname.hairclaw_grovemain_fishing: ACTLocationData(rname.grove_main, 257, "Expired Grove Main"), #23907bde-1820-4c4d-9c59-aab72c64139a-2_A-GroveForestLow
    lname.clothesclaw_grovemain_river: ACTLocationData(rname.grove_main, 258, "Expired Grove Main"), #ebad553d-fbff-441e-8c1d-0ccc65fe81ae-2_A-GroveForestLow

    lname.breadclaw_grovevillage_oildrum: ACTLocationData(rname.grove_village, 268, "Expired Grove Village"), #66a4a627-ad3a-45d6-aaf1-1e505dac0495-2_B-GroveForestHigh
    lname.breadclaw_grovevillage_bottle1: ACTLocationData(rname.grove_village, 269, "Expired Grove Village"), #a6e719fc-65b0-4c3a-830e-43065a819c7d-2_B-GroveForestHigh
    lname.breadclaw_grovevillage_bottle2: ACTLocationData(rname.grove_village, 270, "Expired Grove Village"), #507a5ca4-3de6-4d85-ba51-04c1e42c891e-2_B-GroveForestHigh
    lname.chipclaw_grovevillage_netorbs: ACTLocationData(rname.grove_village, 269, "Expired Grove Village"), #df0386e0-99ee-478a-873d-b40e973fc16b-2_D-Caves
    lname.hairclaw_grovevillage_river: ACTLocationData(rname.grove_village, 272, "Expired Grove Village"), #ec08fee3-e62f-45ee-9fbe-9101522d4f30-2_B-GroveForestHigh
    lname.chipclaw_grovevillage_NWcarton: ACTLocationData(rname.grove_village, 276, "Expired Grove Village"), #84c9cc27-0876-4e4d-a9e2-c28f06abdfc3-2_C-Village
    lname.chipclaw_grovevillage_SEcarton: ACTLocationData(rname.grove_village, 281, "Expired Grove Village"), #c83c8f42-474a-4dd4-bbae-99df2ad1681a-2_C-Village
    lname.chipclaw_grovevillage_NEcarton: ACTLocationData(rname.grove_village, 283, "Expired Grove Village"), #1cd62e82-14b4-4a8a-8dc1-7e8f0ff9b11b-2_C-Village
    lname.breadclaw_grovevillage_shortcut: ACTLocationData(rname.grove_village, 289, "Expired Grove Village"), #ff8f29f4-2859-4ff7-857f-54e0a9c185fa-2_D-Caves
    lname.chipclaw_grovevillage_cave: ACTLocationData(rname.grove_village, 291, "Expired Grove Village"), #6dbab2ee-2440-4b3d-944e-688f11a88199-2_D-Caves
    lname.hairclaw_grovevillage_entrance: ACTLocationData(rname.grove_village, 292, "Expired Grove Village"), #7434f4f5-8e47-40f0-b3a3-507ada236333-2_D-Caves
    lname.breadclaw_grovevillage_Scarton: ACTLocationData(rname.grove_village, 293, "Expired Grove Village"), #b1b6be9e-1973-4562-8e96-43adf0d8fcd5-2_C-Village
    lname.breadclaw_grovevillage_entrance: ACTLocationData(rname.grove_village, 294, "Expired Grove Village"), #dc39a6c7-45be-4e9a-9ac2-4da3094395dd-2_C-Village
    lname.hairclaw_grovevillage_NEcarton: ACTLocationData(rname.grove_village, 297, "Expired Grove Village"), #3eee4944-4b1e-4680-92de-0ee564c91330-2_C-Village
    lname.clothesclaw_grovevillage_upsidedown: ACTLocationData(rname.grove_village, 299, "Expired Grove Village"), #8e368d78-572e-4fed-8607-2fb4c35b23e8-2_C-Village
    lname.clothesclaw_grovevillage_dock: ACTLocationData(rname.grove_village, 311, "Expired Grove Village"), #2a160afc-7439-4e22-9f2b-62fa152f6626-2_C-Village
    lname.hairclaw_grovevillage_dock: ACTLocationData(rname.grove_village, 312, "Expired Grove Village"), #08e5033e-a401-4e90-a1a5-7e9e76ed72a5-2_C-Village
    lname.clothesclaw_grovevillage_hidden: ACTLocationData(rname.grove_village, 314, "Expired Grove Village"), #3bd305d9-8d6b-43c4-99c7-1f2be904de06-2_E-Cliffs
    lname.carclaw_grovevillage_topoda: ACTLocationData(rname.grove_village, 315, "Expired Grove Village"), #2601baa3-999e-443b-ae33-ea619346413b-2_E-Cliffs

    ##### upgrade item locations
    lname.bloodstar_shallows_help: ACTLocationData(rname.central_shallows, 24, "Central Shallows"), #AUTO NEEDS TO DO QUEST SCRIPT
    lname.bloodstar_shallows_parkour: ACTLocationData(rname.central_shallows, 25, "Central Shallows"),#ff9d47b6-7f55-4ad2-a110-e7c4492d87c1-2_B-ShallowsBigSand
    lname.bloodstar_shallows_bridge: ACTLocationData(rname.central_shallows, 26, "Central Shallows"),#32fb25ee-9262-4e87-98f9-2e64d369e7ae-2_B-ShallowsBigSand
    lname.bloodstar_shallows_clam: ACTLocationData(rname.central_shallows, 27, "Central Shallows"), #0474f3a7-0eb7-4d3c-b61e-cbb782ceab03-2_B-ShallowsBigSand

    lname.kelpsprout_snailcave_elevator: ACTLocationData(rname.snail_cave, 28, "Moon Snail's Cave"), #15a2e4c0-4950-4de0-8b5c-e2b1400f76c1-2_D-MoonSnailShellCave
    lname.bloodstar_snailcave_platoon: ACTLocationData(rname.snail_cave, 29, "Moon Snail's Cave"), #00fc94c3-320c-4d0a-a4e0-2b5eccd42d55-2_D-MoonSnailShellCave

    lname.bloodstar_slacktide_clam: ACTLocationData(rname.slacktide_after, 30, "Fort Slacktide - After Destruction"), #451b4cfb-7176-4103-999f-358b09374e0c-2_B-ShallowsBigSand

    lname.stainlessrelic_reefsedge_coral: ACTLocationData(rname.reefs_edge, 64, "Reef's Edge"), #d8433d6b-5400-4dec-aad0-032e27babdeb-2_A-NCTradeRoute

    lname.bloodstar_sandsbetween_playground: ACTLocationData(rname.sands_between, 91, "The Sands Between"), #6801f8fb-6dd9-4129-a182-791a7e66d1c2-2_A-OOGroveRadius
    lname.tacklepouch_sandsbetween_cooler: ACTLocationData(rname.sands_between, 97, "The Sands Between"), #550401bf-30db-4deb-8267-ac73d522236d-2_A-OOGroveRadius
    lname.bloodstar_sandsbetween_southwestcentral: ACTLocationData(rname.sands_between, 133, "The Sands Between"), #956ad9a9-5b43-4f18-a7d9-f67f21c50137-2_A-OOGroveRadius
    lname.oldworldwhorl_sandsbetween_mantispitfall: ACTLocationData(rname.sands_between, 143, "The Sands Between"), #8c7fdc4d-423b-4456-8869-56387a4d7665-2_A-OOGroveRadius
    lname.stainlessrelic_sandsbetween_eelectrocute: ACTLocationData(rname.sands_between, 145, "The Sands Between"), #83daf909-77d3-4302-858b-6e92fe54fe74-2_A-OOGroveRadius
    lname.tacklepouch_sandsbetween_eelnorthchain: ACTLocationData(rname.sands_between, 146, "The Sands Between"), #699b7323-fe71-4bfe-864f-cdd0c9186bbd-2_A-OOGroveRadius
    lname.kelpsprout_sandsbetween_southeelside: ACTLocationData(rname.sands_between, 151, "The Sands Between"), #a7c60b04-8f1b-4833-a6f4-d472e79748c5-2_A-OOGroveRadius

    lname.bloodstar_postpag_anchorswarm: ACTLocationData(rname.post_pag, 169, "The Sands Between - Post Pagurus"), #29e54e45-4248-4a3d-96bf-ddf5cf6046c7-2_A-OOGroveRadius

    lname.stainlessrelic_ridge_overlook: ACTLocationData(rname.secluded_ridge, 186, "The Sands Between - Secluded Ridge"), #c56be461-0e5c-406e-8af0-83021f2f2fb6-2_A-OOGroveRadius
    lname.kelpsprout_ridge_eelend: ACTLocationData(rname.secluded_ridge, 188, "The Sands Between - Secluded Ridge"), #d56339c0-fc26-4f53-a289-2c00b6f7ab38-2_A-OOGroveRadius
    lname.oldworldwhorl_ridge_ncliff: ACTLocationData(rname.secluded_ridge, 190, "The Sands Between - Secluded Ridge"), #8e381b9e-ab7a-44ad-81c3-19157c97e0c6-2_A-OOGroveRadius
    lname.oldworldwhorl_ridge_ncliff: ACTLocationData(rname.secluded_ridge, 205, "The Sands Between - Secluded Ridge"), #80e66e11-8e9a-4896-9db1-f8cd4a25fefc-2_A-OOGroveRadius

    lname.oldworldwhorl_grovemain_southclam: ACTLocationData(rname.grove_main, 217, "Expired Grove Main"), #09b60c18-2172-41bb-9588-a3e764559b15-2_B-GroveForestHigh
    lname.bloodstar_grovemain_waterfall: ACTLocationData(rname.grove_main, 229, "Expired Grove Main"), #f1d3eafe-c252-4768-abcd-7f459e734d35-2_A-GroveForestLow
    lname.kelpsprout_grovemain_carts: ACTLocationData(rname.grove_main, 261, "Expired Grove Main"), #7069eee2-4c77-4a80-a276-1131e6cfe4b8-2_A-GroveForestLow

    lname.bloodstar_grovevillage_carton: ACTLocationData(rname.grove_village, 295, "Expired Grove Village"), #e9f1284d-a5cf-441e-a358-8cabf5e3a7b1-2_C-Village
    lname.tacklepouch_grovevillage_clam: ACTLocationData(rname.grove_village, 298, "Expired Grove Village"), #c69ffc64-04af-44d1-b470-a867c5f06199-2_D-Caves
    lname.stainlessrelic_grovevillage_clam: ACTLocationData(rname.grove_village, 307, "Expired Grove Village"), #269526ef-6bb0-42cf-a93d-e2cac970e424-2_E-Cliffs
    lname.oldworldwhorl_grovevillage_topoda: ACTLocationData(rname.grove_village, 316, "Expired Grove Village"), #8b9b3b77-b95f-46a2-adfd-ca962e8f0cef-2_E-Cliffs

    ##### consumable item locations
    lname.barbedhook_reefsedge_undercoral: ACTLocationData(rname.reefs_edge, 65, "Reef's Edge"), #c44729ce-4c25-4059-8432-212381ca6835-2_A-NCTradeRoute
    lname.barbedhook_reefsedge_seahorses: ACTLocationData(rname.reefs_edge, 66, "Reef's Edge"), #08434b00-0100-4ea1-8f2a-f1567b84bdf2-2_A-NCTradeRoute
    lname.barbedhook_reefsedge_shortcut: ACTLocationData(rname.reefs_edge, 69, "Reef's Edge"), #2b4849b0-2798-4600-8db1-c5d6bf6952b1-2_A-NCTradeRoute
    lname.barbedhook_reefsedge_cliff: ACTLocationData(rname.reefs_edge, 72, "Reef's Edge"), #76ad26b0-4305-498c-8510-4940ad569210-2_A-NCTradeRoute

    lname.barbedhook_newcarcinia_citycenter: ACTLocationData(rname.new_carcinia, 78, "New Carcinia"), #c3b90e59-5289-4ca3-8639-a5c90d656403-2_B-NCCity

    lname.barbedhook_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 88, "The Sands Between"), #6c5631a3-d941-4990-818f-117140982384-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southernreef: ACTLocationData(rname.sands_between, 95, "The Sands Between"), #20b38e81-1198-4905-809a-e42ac4e4759d-2_A-OOGroveRadius
    lname.barbedhook3_sandsbetween_cooler: ACTLocationData(rname.sands_between, 98, "The Sands Between"), #74dac1c4-2458-4cca-a280-11e643e610ce-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_fence: ACTLocationData(rname.sands_between, 99, "The Sands Between"), #21b40d22-140c-493c-98e0-218a5ff29c02-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_spire: ACTLocationData(rname.sands_between, 115, "The Sands Between"), #c192eaf1-dd16-459b-a489-376899aabb9b-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southcentral: ACTLocationData(rname.sands_between, 132, "The Sands Between"), #4ebb3072-53e8-4cff-9672-5f82f926035e-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_bobbitbase: ACTLocationData(rname.sands_between, 134, "The Sands Between"), #90171fe5-d483-4905-a440-a9ab5a7bc074-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_northofridge: ACTLocationData(rname.sands_between, 136, "The Sands Between"), #f8b96a25-70ba-492b-bb87-7b51c81d6102-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southeel: ACTLocationData(rname.sands_between, 152, "The Sands Between"), #771e0942-ebf4-4938-a7e7-c03ce67f9c16-2_A-OOGroveRadius
    lname.barbedhook_sandsbetween_southeelshellsplitter: ACTLocationData(rname.sands_between, 154, "The Sands Between"), #a53aefd5-fa6f-4675-a1b5-2f9e43f3fed0-2_A-OOGroveRadius

    lname.barbedhook_postpag_nechain: ACTLocationData(rname.post_pag, 173, "The Sands Between - Post Pagurus"), #a5c14863-82c3-47d0-b0e1-a67c93da96b8-2_A-OOGroveRadius
    lname.barbedhook_postpag_echain: ACTLocationData(rname.post_pag, 174, "The Sands Between - Post Pagurus"), #d2cd8afa-4bf2-490e-8542-cb92331800d6-2_A-OOGroveRadius
    lname.barbedhook_postpag_echainpreserver: ACTLocationData(rname.post_pag, 175, "The Sands Between - Post Pagurus"), #b03e7050-778b-4029-ab54-f82207d724fa-2_A-OOGroveRadius
    lname.barbedhook_postpag_necentral: ACTLocationData(rname.post_pag, 176, "The Sands Between - Post Pagurus"), #2738d986-20cb-4a09-b6c5-7076a3918283-2_A-OOGroveRadius
    lname.barbedhook_postpag_nwridge: ACTLocationData(rname.post_pag, 177, "The Sands Between - Post Pagurus"), #a8513df4-5533-4a1e-8fa0-b0423757f162-2_A-OOGroveRadius
    lname.barbedhook_postpag_neeelpath: ACTLocationData(rname.post_pag, 178, "The Sands Between - Post Pagurus"), #f14d696d-88a4-471e-a512-b5770c3cfbad-2_A-OOGroveRadius
    lname.barbedhook_postpag_ridgeentrance: ACTLocationData(rname.post_pag, 181, "The Sands Between - Post Pagurus"), #9ecea6b6-f3db-48f8-a753-6644bbbf1aaf-2_A-OOGroveRadius
    lname.barbedhook_postpag_wplayground: ACTLocationData(rname.post_pag, 183, "The Sands Between - Post Pagurus"), #ecea05b3-9908-4b63-b422-d999b78c87e1-2_A-OOGroveRadius
    lname.barbedhook_postpag_swcentral: ACTLocationData(rname.post_pag, 184, "The Sands Between - Post Pagurus"), #7563f2eb-e052-4107-b787-de2f67a40f2f-2_A-OOGroveRadius

    lname.barbedhook_ridge_near: ACTLocationData(rname.secluded_ridge, 187, "The Sands Between - Secluded Ridge"), #97a24ab6-20a3-4f21-b0af-55bf243f33f0-2_A-OOGroveRadius
    lname.barbedhook_ridge_overlookpath: ACTLocationData(rname.secluded_ridge, 192, "The Sands Between - Secluded Ridge"), #d9ee8d70-3493-4e7b-91b3-b42278ff0ad4-2_A-OOGroveRadius
    lname.sharkegg_ridge_broomspire: ACTLocationData(rname.secluded_ridge, 212, "The Sands Between - Secluded Ridge"), #dcc6b99e-1d47-481f-86ca-e14a5743f460-2_A-OOGroveRadius

    lname.barbedhook_trashbin_eelgrapple: ACTLocationData(rname.secluded_ridge, 210, "The Sands Between - Trashbin Plataeu"), #2bccca10-1f27-4762-9a9b-8e628586e0a4-2_A-OOGroveRadius

    lname.barbedhook_grovemain_sniper: ACTLocationData(rname.secluded_ridge, 214, "Expired Grove Main"), #8fd70034-2415-4934-975b-2303d159f567-2_A-GroveForestLow
    lname.barbedhook_grovemain_riverledge: ACTLocationData(rname.secluded_ridge, 215, "Expired Grove Main"), #0860891c-3db6-4e51-8c0b-58b09ac8ece0-2_A-GroveForestLow
    lname.barbedhook_grovemain_riversand: ACTLocationData(rname.secluded_ridge, 216, "Expired Grove Main"), #2465aea2-9800-49e5-9e7e-d751ca2b3612-2_A-GroveForestLow
    lname.barbedhook_grovemain_lichenthrope: ACTLocationData(rname.secluded_ridge, 221, "Expired Grove Main"), #35455018-8cf6-48db-ba76-4ffbca84b0a8-2_A-GroveForestLow
    lname.barbedhook_grovemain_lichenthropeeast: ACTLocationData(rname.secluded_ridge, 222, "Expired Grove Main"), #5a106f4d-8139-44da-9cdf-8d0bd70c6bf3-2_A-GroveForestLow
    lname.barbedhook_grovemain_sodacans: ACTLocationData(rname.secluded_ridge, 223, "Expired Grove Main"), #10a99891-923e-4bab-8057-b6d5781cb35d-2_A-GroveForestLow
    lname.barbedhook_grovemain_acrossriver: ACTLocationData(rname.secluded_ridge, 228, "Expired Grove Main"), #50f9f7d1-0e70-4333-b8b3-fbc46f04f3ea-2_A-GroveForestLow
    lname.barbedhook_grovemain_afternets: ACTLocationData(rname.secluded_ridge, 230, "Expired Grove Main"), #e7382e22-3232-4380-a734-bef8eb9a2a76-2_A-GroveForestLow
    lname.barbedhook_grovemain_cartledge: ACTLocationData(rname.secluded_ridge, 235, "Expired Grove Main"), #dc13eb69-ac98-4de9-9fe0-7f16a03d4ebb-2_A-GroveForestLow
    lname.barbedhook_grovemain_cartledgebottle: ACTLocationData(rname.secluded_ridge, 237, "Expired Grove Main"), #a5b6f3f6-6e1c-4934-9006-26da6cee47f4-2_A-GroveForestLow
    lname.barbedhook_grovemain_paperplate: ACTLocationData(rname.secluded_ridge, 241, "Expired Grove Main"), #776881ba-f61b-4400-8cf5-f11fb11b6f94-2_B-GroveForestHigh
    lname.barbedhook_grovemain_oildrum: ACTLocationData(rname.secluded_ridge, 242, "Expired Grove Main"), #12c73a88-beef-4bfb-a2d1-c159c91d8304-2_B-GroveForestHigh
    lname.barbedhook_grovemain_canopy: ACTLocationData(rname.grove_main, 248, "Expired Grove Main"), #101eff6d-e09a-471d-86fd-cdc587012c32-2_A-GroveForestLow
    lname.barbedhook_grovemain_drumtop: ACTLocationData(rname.secluded_ridge, 250, "Expired Grove Main"), #3a1e7a2c-5111-4360-b168-cc5e84088b6a-2_B-GroveForestHigh
    lname.barbedhook_grovemain_carts: ACTLocationData(rname.grove_main, 259, "Expired Grove Main"), #d1b73602-aca6-4d33-991d-39110a5e6780-2_A-GroveForestLow
    lname.sharkegg_grovemain_mantis: ACTLocationData(rname.grove_main, 260, "Expired Grove Main"), #f734eb5e-d674-4c84-9493-61d20f70fde3-2_A-GroveForestLow

    lname.barbedhook_grovevillage_heikea: ACTLocationData(rname.grove_village, 287, "Expired Grove Village"), #bcfabbd4-8575-4a6a-8325-7259996a7d68-2_D-Caves
    lname.barbedhook_grovevillage_cartfish: ACTLocationData(rname.grove_village, 271, "Expired Grove Village"), #7a38fbf2-47a9-4bf6-85d1-f8d4f58b8d66-2_B-GroveForestHigh
    lname.barbedhook_grovevillage_riveroil: ACTLocationData(rname.grove_village, 273, "Expired Grove Village"), #9c983d04-ac83-40f0-8220-d92f76ea7099-2_B-GroveForestHigh
    lname.barbedhook_grovevillage_bottles: ACTLocationData(rname.grove_village, 275, "Expired Grove Village"), #5c973136-cfe9-4ea5-bc93-60ffa4b5cc13-2_C-Village
    lname.barbedhook_grovevillage_crabs: ACTLocationData(rname.grove_village, 277, "Expired Grove Village"), #4721ab20-67be-4d5b-b0bb-3f2c2ecb510f-2_C-Village
    lname.barbedhook_grovevillage_centercarton: ACTLocationData(rname.grove_village, 278, "Expired Grove Village"), #bae2eb9a-56a0-4548-8c6d-798d234ba479-2_C-Village
    lname.barbedhook_grovevillage_corpse: ACTLocationData(rname.grove_village, 279, "Expired Grove Village"), #20238db7-8d1e-4045-8e0a-de2aaea1cb49-2_C-Village
    lname.barbedhook_grovevillage_path: ACTLocationData(rname.grove_village, 280, "Expired Grove Village"), #87e729ae-0659-4b6e-9ac1-c1d059719ba8-2_C-Village
    lname.barbedhook_grovevillage_Ncarton: ACTLocationData(rname.grove_village, 282, "Expired Grove Village"), #b29402c2-62e8-4fa3-8c27-4e419750b16f-2_C-Village
    lname.barbedhook_grovevillage_SWcarton: ACTLocationData(rname.grove_village, 284, "Expired Grove Village"), #256daaaa-675c-47e5-bd4e-367dc4abd9e2-2_C-Village
    lname.sharkegg_grovevillage_sniper: ACTLocationData(rname.grove_village, 285, "Expired Grove Village"), #451f2fe5-9c29-4710-9493-0878963547e4-2_C-Village
    lname.barbedhook_grovevillage_boat: ACTLocationData(rname.grove_village, 286, "Expired Grove Village"), #99c33625-2da4-4f69-a0af-8a8d2da3b399-2_D-Caves
    lname.barbedhook_grovevillage_butter: ACTLocationData(rname.grove_village, 290, "Expired Grove Village"), #10eae42f-9cca-447a-8cb8-9cffcba11ecd-2_D-Caves
    lname.barbedhook_grovevillage_above1: ACTLocationData(rname.grove_village, 301, "Expired Grove Village"), #28362ae0-defe-4a04-b449-93d7e5e60676-2_C-Village
    lname.barbedhook_grovevillage_above2: ACTLocationData(rname.grove_village, 302, "Expired Grove Village"), #0177d8ef-8849-4ea4-b1b3-08a1c3134a99-2_E-Cliffs
    lname.barbedhook_grovevillage_above3: ACTLocationData(rname.grove_village, 303, "Expired Grove Village"), #b3a776e1-52ab-4dc8-adc1-55c95eca9972-2_E-Cliffs
    lname.barbedhook_grovevillage_ornament: ACTLocationData(rname.grove_village, 304, "Expired Grove Village"), #ce1700e2-d9d0-462a-af23-cb55828b062a-2_E-Cliffs
    lname.barbedhook_grovevillage_hammer: ACTLocationData(rname.grove_village, 305, "Expired Grove Village"), #235b691b-0f18-4f35-bd8a-7536e12fabfe-2_E-Cliffs
    lname.barbedhook_grovevillage_dock: ACTLocationData(rname.grove_village, 309, "Expired Grove Village"), #aff46c65-7a4a-4b1c-a0ca-840af3898f26-2_C-Village

    ##### stowaway locations
    lname.siphonophore_shallows_westwall: ACTLocationData(rname.central_shallows, 31, "Central Shallows"),#4d4ac114-06e4-400f-b888-b500a7348cc9-2_B-ShallowsBigSand
    lname.seastar_shallows_eastledge: ACTLocationData(rname.central_shallows, 32, "Central Shallows"), #e9a5a6cf-2a19-4db5-bb0d-d85b260f3e2b-2_B-ShallowsBigSand
    lname.sponge_shallows_puffer: ACTLocationData(rname.central_shallows, 33, "Central Shallows"), #95c0077d-518f-4ab7-85e2-ac1e0c1bb0b9-2_B-ShallowsBigSand
    lname.anothercrab_shallows_pillar: ACTLocationData(rname.central_shallows, 34, "Central Shallows"), #924670c2-839f-4e42-9cf5-8c081b17f946-2_B-ShallowsBigSand
    lname.sanddollar_shallows_arch: ACTLocationData(rname.central_shallows, 35, "Central Shallows"), #804d3848-3e86-474f-8622-547d020c4cc4-2_B-ShallowsBigSand
    lname.mussel_shallows_southwestcastlefish: ACTLocationData(rname.central_shallows, 125, "Central Shallows"), #41a6780e-55a2-4a0a-96a9-bb279a3b1ec3-2_B-ShallowsBigSand
    lname.anemone_shallows_southwestcastlehiddenfishing: ACTLocationData(rname.central_shallows, 127, "Central Shallows"), #daaa6ab6-8aac-4713-942f-f322e918dd55-2_B-ShallowsBigSand
    lname.razorblade_shallows_slacktidebottlefishing: ACTLocationData(rname.central_shallows, 128, "Central Shallows"), #728b3da1-5b4b-4a7f-885c-b5ed9abfadbc-2_B-ShallowsBigSand
    lname.anemone_shallows_umbrellafishing: ACTLocationData(rname.central_shallows, 129, "Central Shallows"), #b29c140a-08c2-44c6-81c3-5f91e5621e47-2_B-ShallowsBigSand

    lname.limpet_slacktide_stairs: ACTLocationData(rname.slacktide_before, 36, "Fort Slacktide - Before Destruction"), #b5e751fb-8ff5-440e-aa9c-9d9c75977be7-2_B-ShallowsBigSand
    lname.seastar_slacktide_grappleroom: ACTLocationData(rname.slacktide_before, 37, "Fort Slacktide - Before Destruction"), #35603032-802e-4811-ae95-8e8eb11c1dfa-2_B-ShallowsBigSand
    lname.barnacle_slacktide_bigurchin: ACTLocationData(rname.slacktide_before, 38, "Fort Slacktide - Before Destruction"), #98329dde-9889-4cbb-a656-61f83dca2eca-2_B-ShallowsBigSand

    lname.limpet_snailcave_jelly: ACTLocationData(rname.snail_cave, 39, "Moon Snail's Cave"), #c1a31dc1-9ec5-42e9-8dcf-291f7cdc8a26-2_D-MoonSnailShellCave

    lname.mussel_slacktide_fortentrance: ACTLocationData(rname.slacktide_after, 40, "Fort Slacktide - After Destruction"), #694c4c66-fefc-4539-962f-a343e13b044b-2_C-Slacktide2
    lname.anemone_slacktide_fortwall: ACTLocationData(rname.slacktide_after, 41, "Fort Slacktide - After Destruction"), #557546a8-096b-49cd-b63b-452fb751a8bf-2_C-Slacktide2
    lname.whelk_slacktide_turrettop: ACTLocationData(rname.slacktide_after, 42, "Fort Slacktide - After Destruction"), #e1848736-945b-406d-853e-d213f7c80f14-2_C-Slacktide2

    lname.seastar_reefsedge_crabs: ACTLocationData(rname.reefs_edge, 68, "Reef's Edge"), #d93f0715-7c15-4f74-b376-34468705093c-2_A-NCTradeRoute
    lname.seastarplus_reefsedge_pole: ACTLocationData(rname.reefs_edge, 70, "Reef's Edge"), #3473ed8f-db06-4bb7-9932-862f92258542-2_A-NCTradeRoute
    lname.whelkplus_reefsedge_sponge: ACTLocationData(rname.reefs_edge, 73, "Reef's Edge"), #5e8a3fb6-f3b1-42a0-a8b8-10b57b340138-2_A-NCTradeRoute

    lname.limpet_newcarcinia_entrance: ACTLocationData(rname.new_carcinia, 75, "New Carcinia"), #e7b4c4fc-6208-4326-847e-ee34113f7fe0-2_B-NCCity
    lname.rustynail_newcarcinia_hammerhead: ACTLocationData(rname.new_carcinia, 77, "New Carcinia"), #f2105767-2544-4acc-9703-a47fbe97c3dc-2_B-NCCity

    lname.sanddollar_newcarcinia_hammerhead: ACTLocationData(rname.new_carcinia, 86,"New Carcinia"), #a1194e18-4659-4ac9-aa73-744a6df42fe3-2_B-NCCity

    lname.phytoplankton_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 89, "The Sands Between"), #3197c269-c43d-4bff-b388-a6c3d3e4b5f3-2_A-OOGroveRadius
    lname.anemone_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 90, "The Sands Between"), #73aec841-ee9a-411b-8919-53eeeb33ec59-2_A-OOGroveRadius
    lname.anemone_sandsbetween_playground: ACTLocationData(rname.sands_between, 92, "The Sands Between"), #bd3a89be-89f5-4029-ac76-c1966c70299d-2_A-OOGroveRadius
    lname.rustynail_sandsbetween_fence: ACTLocationData(rname.sands_between, 93, "The Sands Between"), #8778ffd7-a95d-4021-bb90-4a116de9894a-2_A-OOGroveRadius
    lname.googlyeye_sandsbetween_pizza: ACTLocationData(rname.sands_between, 96, "The Sands Between"), #52821431-a6c7-458a-b54f-d42196919993-2_A-OOGroveRadius
    lname.siphonophore_sandsbetween_cooler: ACTLocationData(rname.sands_between, 100, "The Sands Between"), #8d4c2499-b344-4e0f-b4e4-dc2a3e7ccf74-2_A-OOGroveRadius
    lname.limpet_sandsbetween_anchor: ACTLocationData(rname.sands_between, 101, "The Sands Between"), #1f5bc2e0-a613-4afd-bdf6-5ed4805edf29-2_A-OOGroveRadius
    lname.anemone_sandsbetween_chains: ACTLocationData(rname.sands_between, 103, "The Sands Between"), #57559d1c-80ce-4396-afdf-7d7e6af71ff6-2_A-OOGroveRadius
    lname.fredrick_sandsbetween_fredrick: ACTLocationData(rname.sands_between, 104, "The Sands Between"), #6f1f751a-b27c-4eb0-b95c-a89d66dd242a-2_A-OOGroveRadius
    lname.anothercrab_sandsbetween_chains: ACTLocationData(rname.sands_between, 105, "The Sands Between"), #03ba104a-efe3-4294-b378-b2aeff7aa9e3-2_A-OOGroveRadius
    lname.mussel_sandsbetween_anchor: ACTLocationData(rname.sands_between, 110,"The Sands Between"), #a08ac116-549b-4691-8e88-79daf965dff8-2_A-OOGroveRadius
    lname.barnacle_sandsbetween_northeast: ACTLocationData(rname.sands_between, 113,"The Sands Between"), #234f3d49-7fc5-4039-949f-8d95f38d7c79-2_A-OOGroveRadius
    lname.salp_sandsbetween_northeast: ACTLocationData(rname.sands_between, 114,"The Sands Between"), #2dc13e33-724d-41a7-983b-5f3bf010ce89-2_A-OOGroveRadius
    lname.rustynailplus_sandsbetween_centralvista: ACTLocationData(rname.sands_between, 116,"The Sands Between"), #fc6e8558-9515-40a7-9857-9584a196a1ec-2_A-OOGroveRadius
    lname.seastarplus_sandsbetween_flotsam: ACTLocationData(rname.sands_between, 117,"The Sands Between"), #d19ac393-ea1d-4237-9d31-b620c3a2617d-2_A-OOGroveRadius
    lname.seaslug_sandsbetween_crabrave: ACTLocationData(rname.sands_between, 118,"The Sands Between"), #bceed85e-5560-4a77-a498-749af9f76780-2_A-OOGroveRadius
    lname.whelk_sandsbetween_crabrave: ACTLocationData(rname.sands_between, 119,"The Sands Between"), #63b93466-f406-492e-ac12-f243fe6a8165-2_A-OOGroveRadius
    lname.sinkerplus_sandsbetween_northridgemantis: ACTLocationData(rname.sands_between, 141,"The Sands Between"), #a8e01dfb-5dd9-4da0-92b1-39a7b18e8d83-2_A-OOGroveRadius
    lname.limpetplus_sandsbetween_grovemantis: ACTLocationData(rname.sands_between, 142,"The Sands Between"), #56e45097-4ffa-41b0-ac56-cdd6c93b5e88-2_A-OOGroveRadius
    lname.lumpsuckerplus_sandsbetween_anchor: ACTLocationData(rname.sands_between, 144,"The Sands Between"), #859c746b-c52f-4887-aa96-bb19bd7e25dd-2_A-OOGroveRadius
    lname.sinkerplus_sandsbetween_southeel: ACTLocationData(rname.sands_between, 148,"The Sands Between"), #ae4a7ac6-5eb0-4590-a3c7-5d5f236a978d-2_A-OOGroveRadius
    lname.musselplus_sandsbetween_southeel: ACTLocationData(rname.sands_between, 149,"The Sands Between"), #7111735c-772e-4c1f-b255-183e62760ae2-2_A-OOGroveRadius
    lname.oyster_sandsbetween_southeelashtray: ACTLocationData(rname.sands_between, 153,"The Sands Between"), #2ccd3299-d207-4d4d-b5a5-d777c4e8aa29-2_A-OOGroveRadius
    lname.mussel_sandsbetween_bobbitfish: ACTLocationData(rname.sands_between, 159,"The Sands Between"), #da5f126f-e470-432c-b5b0-8eca9918ed77-2_A-OOGroveRadius
    lname.barnacle_sandsbetween_bobbitfish: ACTLocationData(rname.sands_between, 161,"The Sands Between"), #15cf7503-de68-4475-b39c-fe687f85c448-2_A-OOGroveRadius
    lname.whelkplusplus_sandsbetween_southeelpeak: ACTLocationData(rname.sands_between, 166,"The Sands Between"), #d61a21a2-c27d-45d7-8e11-75fcd11e8b78-2_A-OOGroveRadius
    lname.salpplus_sandsbetween_groveeel: ACTLocationData(rname.sands_between, 167,"The Sands Between"), #7faef89f-c78a-4002-9454-c20bf5098229-2_A-OOGroveRadius
    lname.usedbandage_sandsbetween_groveeel: ACTLocationData(rname.sands_between, 168,"The Sands Between"), #3123f8ec-3548-41f5-a777-c10268e06b8b-2_A-OOGroveRadius

    lname.limpet_ridge_ncliffkelp: ACTLocationData(rname.secluded_ridge, 191, "The Sands Between - Secluded Ridge"), #fcb1f0bb-2ebf-449c-b5fd-ebb7d515c7af-2_A-OOGroveRadius
    lname.sanddollar_ridge_broom: ACTLocationData(rname.secluded_ridge, 194, "The Sands Between - Secluded Ridge"), #42686eee-4b9f-4d44-a52d-569d2c814f13-2_A-OOGroveRadius
    lname.musselplus_ridge_togo: ACTLocationData(rname.secluded_ridge, 196, "The Sands Between - Secluded Ridge"), #a59b9d02-9711-48e3-8296-e2164c79f1f2-2_A-OOGroveRadius
    lname.siphonophoreplus_ridge_pitfall: ACTLocationData(rname.secluded_ridge, 203, "The Sands Between - Secluded Ridge"), #e2a1e3e1-8ee4-4539-ab81-98c4d6d99630-2_A-OOGroveRadius
    lname.anemoneplus_ridge_eel: ACTLocationData(rname.secluded_ridge, 204, "The Sands Between - Secluded Ridge"), #1b6f2070-3ff2-4f48-b061-0a41990013e1-2_A-OOGroveRadius
    lname.cockle_ridge_eelfish: ACTLocationData(rname.secluded_ridge, 208, "The Sands Between - Secluded Ridge"), #d32ade52-c34e-4cb7-957c-df605339ee4c-2_A-OOGroveRadius
    lname.bobber_ridge_broomspire: ACTLocationData(rname.secluded_ridge, 211, "The Sands Between - Secluded Ridge"), #fc2cf7ed-6ff6-40bb-987a-936da0afa93b-2_A-OOGroveRadius

    lname.cockle_trashbin_peak: ACTLocationData(rname.secluded_ridge, 199, "The Sands Between - Trashbin Plataeu"), #ca4c297f-e9fd-4a78-b89a-811d2394406b-2_A-OOGroveRadius
    lname.sinker_trashbin_peak: ACTLocationData(rname.secluded_ridge, 200, "The Sands Between - Trashbin Plataeu"), #36611427-18cc-45f3-ad50-a51cc02ccb1d-2_A-OOGroveRadius
    lname.smallbattery_trashbin_mantis: ACTLocationData(rname.secluded_ridge, 201, "The Sands Between - Trashbin Plataeu"), #0d86fe0e-ae41-4fb2-beb2-9bb5e558429a-2_A-OOGroveRadius
    lname.googlyeye_trashbin_pineapple: ACTLocationData(rname.secluded_ridge, 202, "The Sands Between - Trashbin Plataeu"), #7935fe1e-318c-4f90-901b-fa001de6e4dc-2_A-OOGroveRadius

    lname.barnacle_grovemain_colander: ACTLocationData(rname.grove_main, 213, "Expired Grove Main"), #74aa4107-6a5a-4868-ae54-942e4421be3f-2_A-GroveForestLow
    lname.seastar_grovemain_eastrock: ACTLocationData(rname.grove_main, 218, "Expired Grove Main"), #17cb1eed-8d88-4464-b33b-215c837035f6-2_A-GroveForestLow
    lname.pufferquill_grovemain_sponges: ACTLocationData(rname.grove_main, 220, "Expired Grove Main"), #c6a56f3d-c134-41cd-83b7-4a755fa32284-2_A-GroveForestLow
    lname.limpet_grovemain_sodacan: ACTLocationData(rname.grove_main, 236, "Expired Grove Main"), #093c4972-ff5e-4ba6-b9a8-136411e1017f-2_A-GroveForestLow
    lname.lumpsucker_grovemain_canopy: ACTLocationData(rname.grove_main, 247, "Expired Grove Main"), #3789e56d-69b5-4d6c-adb1-6454b101840d-2_A-GroveForestLow
    lname.sharktooth_grovemain_pizza: ACTLocationData(rname.grove_main, 251, "Expired Grove Main"), #8e34f6a5-5844-4767-ab15-4fbaf6c147dc-2_B-GroveForestHigh
    lname.contactlens_grovemain_carts: ACTLocationData(rname.grove_main, 262, "Expired Grove Main"), #0e278f86-0f9d-468f-95b2-586df2a94689-2_A-GroveForestLow
    lname.cottonball_grovemain_mantis: ACTLocationData(rname.grove_main, 263, "Expired Grove Main"), #fa3cfc64-4f87-452c-bf59-4f599cb3f6fa-2_A-GroveForestLow
    lname.mussel_grovemain_fishing: ACTLocationData(rname.grove_main, 264, "Expired Grove Main"), #a1c14883-bc09-441c-a188-20dabf047532-2_A-GroveForestLow
    lname.sponge_grovemain_fishing: ACTLocationData(rname.grove_main, 265, "Expired Grove Main"), #7aa1847-5a38-4f15-a6fc-90c15cd9baf7-2_A-GroveForestLow
    lname.oyster_grovemain_fishing: ACTLocationData(rname.grove_main, 266, "Expired Grove Main"), #6ce4acf2-09a4-43ca-9be7-5d79a9d5c781-2_A-GroveForestLow
    lname.limpet_grovemain_fishing: ACTLocationData(rname.grove_main, 267, "Expired Grove Main"), #027511ce-7f48-480e-91af-18b4c7aaa57d-2_A-GroveForestLow

    lname.anemone_grovevillage_fishing: ACTLocationData(rname.grove_village, 274, "Expired Grove Village"), #5e81380f-3e8f-4d44-a0ef-ebbad0f23fdb-2_B-GroveForestHigh
    lname.phytoplanktonplus_grovevillage_upsidedown: ACTLocationData(rname.grove_village, 300, "Expired Grove Village"), #03bc01f8-4691-40b7-93c6-4d45563b5b46-2_C-Village
    lname.wadofgum_grovevillage_gumpile: ACTLocationData(rname.grove_village, 306, "Expired Grove Village"), #ab2ba852-edf4-467f-a1f5-1825341b7596-2_E-Cliffs
    lname.anemone_grovevillage_seahorse: ACTLocationData(rname.grove_village, 308, "Expired Grove Village"), #32841813-148d-45f7-8c4e-4464f157200d-2_E-Cliffs
    lname.mussel_grovevillage_dock: ACTLocationData(rname.grove_village, 310, "Expired Grove Village"), #3f1f877c-e5ac-40d1-93b7-2245282b0669-2_C-Village
    lname.earthworm_grovevillage_dock: ACTLocationData(rname.grove_village, 313, "Expired Grove Village"), #725998d5-172d-4408-9f70-0f9264a6a6fd-2_C-Village

    ##### costume locations
    lname.captain_costume_pickup: ACTLocationData(rname.central_shallows, 43, "Central Shallows"), #7c307763-a7b4-4e81-88d6-e1baf1b04608-2_B-ShallowsBigSand
    lname.clown_costume_pickup: ACTLocationData(rname.sands_between, 140,"The Sands Between"), #cd2d0535-6c06-4530-bf60-afbffc2d5086-2_A-OOGroveRadius
    lname.sunlight_costume_pickup: ACTLocationData(rname.secluded_ridge, 198, "The Sands Between - Secluded Ridge"), #35aa72f2-fa50-4efc-b600-b597382ed877-2_A-OOGroveRadius
    lname.intern_costume_pickup: ACTLocationData(rname.grove_village, 296, "Expired Grove Village"), #4ba7f2ff-ff35-4d74-b5ac-d9c59fe1c94d-2_C-Village

    ##### non-boss adaptation locations
    lname.urchin_toss_quest: ACTLocationData(rname.new_carcinia, 85,"New Carcinia"), #AUTO NEEDS TO MAKE A CUSTOM SCRIPT
    lname.bobbit_trap_pickup: ACTLocationData(rname.sands_between, 109,"The Sands Between"), #3bb06349-c151-4333-8305-ba0eb7512bc3-2_A-OOGroveRadius
    #lname.royal_wave_reward: ACTLocationData(rname.slacktide_after, x, "Fort Slacktide - After Destruction") #Redundant, overlaps with Magista
}


location_name_to_id: Dict[str, int] = {name: location_base_id + data.location_id_offset for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)