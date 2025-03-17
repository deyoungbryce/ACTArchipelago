from typing import Dict, List, Any
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, ItemClassification, CollectionState
from Fill import fill_restrictive

from .items import item_table, item_name_groups, item_name_to_id, filler_items, costume_items, trap_items, shell_items, ACTItem, ACTItemData
from .locations import location_table, location_name_groups, location_name_to_id, location_total, shell_locations, ACTLocation, ACTLocationData
from .regions import ACT_regions
from .rules import set_location_rules, set_region_rules
from .options import ACTGameOptions
from .names import location_names as lname, item_names as iname, region_names as rname, shell_names as sname


class ACTWeb(WebWorld):
    theme: str = "ocean"
    game: str = "Another Crab's Treasure"

class ACTWorld(World):
    """
    Another Crab's Treasure is an underwater souls-like with a charming art style and a quirky sense of humor.
    """
    game: str = "Another Crabs Treasure"
    web = ACTWeb()

    options_dataclass = ACTGameOptions
    options: ACTGameOptions
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    slot_data_items = List[ACTItem]
    placed_shells = List[ACTLocation]

    def generate_output(self, output_directory: str):
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml", show_entrance_names=False ) #regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[self.player]

    def generate_early(self):
        # early fork shuffling
        if self.options.fork_location == "shuffled_early_local" and not self.options.allow_forkless:
            self.multiworld.local_early_items[self.player][iname.fork] = 1
        if self.options.fork_location == "shuffled_early_global" and not self.options.allow_forkless:
            self.multiworld.early_items[self.player][iname.fork] = 1

        # early shelleport shuffling
        if self.options.shelleport_location == "shuffled_early_local":
            self.multiworld.local_early_items[self.player][iname.shelleport] = 1
        if self.options.shelleport_location == "shuffled_early_global":
            self.multiworld.early_items[self.player][iname.shelleport] = 1

    def get_locations(self):
        return self.multiworld.get_locations(self.player)

    def pre_fill(self):
        state = CollectionState(self.multiworld)

        #Shuffle Shell Event Locations
        if self.options.randomshells == True:
            self.random.shuffle(shell_items)

            shell_at_soda: ACTItemData = item_table[shell_items[shell_locations.index(sname.soda_can)]]
            prevented_shells_at_soda = [sname.piggy_bank,sname.crab_husk,sname.rubber_duck,sname.baby_shoe]

            #Make sure soda can has something usable for combat
            if self.options.allow_forkless != "disabled":
                while  shell_at_soda.classification != ItemClassification.progression or any(shell_at_soda == element for element in prevented_shells_at_soda):
                    self.random.shuffle(shell_items)
                    shell_at_soda = item_table[shell_items[shell_locations.index(sname.soda_can)]]
            
            for i in range(len(shell_items)):
                region = self.multiworld.get_region(location_table[shell_locations[i]].region,self.player)
                shell_placed_loc = ACTLocation(self.player,shell_locations[i],None,region)
                shell_placed_loc.place_locked_item(ACTItem(shell_items[i],ItemClassification.progression,None,self.player))
                
                region.locations.append(shell_placed_loc)
                #self.placed_shells.append(shell_placed_loc)


        return super().pre_fill()

    def create_item(self, name: str) -> ACTItem:
        item_data = item_table[name]
        if item_data.item_id_offset != None:
            return ACTItem(name, item_data.classification, self.item_name_to_id[name], self.player)
        else:
            return ACTItem(name, item_data.classification, None, self.player)

    # not actually used rn, may be useful for shell rando
    def create_event(self, event: str) -> ACTItem:
        return ACTItem(event, True, None, self.player)

    def create_items(self) -> None:
        ACT_items: List[ACTItem] = []
        self.slot_data_items = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        # removing shells from the total item pool because we only want them shuffled within their own pool
        
        for shells in shell_items: 
            print("ShellItem_"+shells)
            items_to_create[shells] = 0

        # yaml options
        if self.options.fork_location and not self.options.allow_forkless:
            fork = self.create_item(iname.fork)
            if self.options.fork_location == "vanilla_location":
                self.get_location(lname.fork_pickup).place_locked_item(fork)
                items_to_create[iname.fork] = 0

        if self.options.shelleport_location:
            shelleport = self.create_item(iname.shelleport)
            if self.options.shelleport_location == "starting_items":
                self.multiworld.push_precollected(shelleport)
                items_to_create[iname.shelleport] = 0
            elif self.options.shelleport_location == "vanilla_location":
                self.get_location(lname.shelleport_skill).place_locked_item(shelleport)
                items_to_create[iname.shelleport] = 0

        if self.options.fishing_line_location:
            fishing_line = self.create_item(iname.fishing_line)
            if self.options.fishing_line_location == "vanilla_location":
                self.get_location(lname.fishing_line).place_locked_item(fishing_line)
            items_to_create[iname.fishing_line] = 0

        if self.options.remove_costumes:
            for costumes in costume_items: items_to_create[costumes] = 0
        
        # fill empty locations with filler and traps
        ## I've had some issues with strange generation cases due to this way of handling filler items
        items_total: int = 0

        for item in items_to_create:
            items_total += items_to_create[item]

        total_filler = location_total - items_total

        available_filler: List[str] = [filler for filler in items_to_create if items_to_create[filler] > 0 and item_table[filler].classification == ItemClassification.filler]

        if total_filler < 0:
            total_filler = 0

        traps_needed = total_filler * self.options.trapamount.value / 100

        for counter in range(0, round(traps_needed)):
            trap_item = self.random.choice(trap_items)
            items_to_create[trap_item] += 1

        filler_needed = total_filler - traps_needed

        for counter in range(0, round(filler_needed)):
            filler_item = self.random.choice(available_filler)
            items_to_create[filler_item] += 1

        # add items to item pool
        for item, quantity in items_to_create.items():
            print("Creating " + str(quantity) + " " + item)
            for i in range(quantity):
                ACT_item: ACTItem = self.create_item(item)
                if item in shell_items:
                    self.slot_data_items.append(ACT_item)
                else:
                    ACT_items.append(ACT_item)

        self.multiworld.itempool += ACT_items

    def create_regions(self):

        for region_name in ACT_regions:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in ACT_regions.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_exits(exits)

        for location_name, location_id in location_name_to_id.items():
            region = self.multiworld.get_region(location_table[location_name].region, self.player)
            location = ACTLocation(self.player, location_name, location_id, region)
            region.locations.append(location)

        # for i in range(len(shell_items)):
        #     region = self.multiworld.get_region(location_table[shell_locations[i]].region,self.player)
        #     location = self.placed_shells[i]
        #     region.locations.append(location)

        # player can complete the game if they can reach the final region
        if self.options.goal == "firth":
            self.multiworld.completion_condition[self.player] = \
                lambda state: state.can_reach_region(spot = rname.carcinia_ruins, player = self.player)
            
        if self.options.goal == "roland":
            self.multiworld.completion_condition[self.player] = \
                lambda state: state.can_reach_region(spot = rname.pinbarge, player = self.player)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)
    
    # shell slotdata stuff almost certainly isn't going to work properly like this

    def fill_slot_data(self) -> Dict[str, Any]:

        shell_rando: Dict[str,str] = {}
        for i in range(len(shell_items)):
            shell_rando.update({shell_locations[i]:shell_items[i]})

        slot_data: Dict[str, Any] = {
            "microplastic_multiplier": float(self.options.microplasticMultiplier.value),
            "death_link": bool(self.options.deathlink.value),
            "goal": str(self.options.goal.value),
            "shell_rando": shell_rando
        }


        return slot_data