from enum import Enum
from typing import TypedDict


class ANIMALS(Enum):
    SHEEP = "Sheep"
    WOLF = "Wolf"
    SLOTH = "Sloth"
    CAT = "Cat"
    BUNNY = "Bunny"
    BIRD = "Bird"
    HORSE = "Horse"
    BEAVER = "Beaver"
    REPTILE = "Reptile"
    BEAR = "Bear"
    MONKEY = "Monkey"


class POLITICAL_PLATFORMS(Enum):
    UNIVERSAL_BASIC_FOOD_SUPPLY = "Universal Basic Food Supply"
    INCREASED_SPEED_LIMIT = "Increased Speed Limit"
    EXPANDED_HUNTING_GROUNDS = "Expanded Hunting Grounds"
    SUBSIDIZED_CHILDCARE = "Subsidized Childcare"
    TREE_PRESERVATION = "Tree Preservation"
    TREE_PRESERVATION_ACT = "Tree Preservation Act"
    EXTENDED_HIBERNATION_LEAVE = "Extended Hibernation Leave"
    RIVER_RESTORATION_FUNDING = "River Restoration Funding"
    BETTER_PASTURE_MAINTENANCE = "Better Pasture Maintenance"
    COMMUNAL_GRAZING_RIGHTS = "Communal Grazing Rights"
    BERRY_PICKING_QUOTAS = "Berry Picking Quotas"
    GARBAGE_ACCESS_RIGHTS = "Garbage Access Rights"
    MIGRATION_REST_STOPS = "Migration Rest Stops"
    QUIET_HOURS_FOR_NOCTURNAL_SPECIES = "Quiet Hours for Nocturnal Species"
    MORE_CROSSING_GUARDS = "More Crossing Guards"
    INCREASE_PUBLIC_SAFETY = "Increase Public Safety"
    EXTENDED_NAP_HOURS = "Extended Nap Hours"
    ALL = "All"
    NONE = "None"


class GENDER(Enum):
    MALE = "Male"
    FEMALE = "Female"


class PoliticalPositions(TypedDict):
    FOR: list[POLITICAL_PLATFORMS]
    AGAINST: list[POLITICAL_PLATFORMS]


CSV_COLUMN_HEADERS_TO_VOTER_INPUTS: dict[str, str] = {
    'Species': 'species',
    'File Name': 'filename',
    'Male or Female': 'gender',
    'Animal Name': 'name',
    'Politics (Positive)': 'positive_positions',
    'Politics (Negative)': 'negative_positions'
}

CSV_SPECIES_TO_ANIMALS: dict[str, ANIMALS] = {
    'Bear': ANIMALS.BEAR,
    'Beaver': ANIMALS.BEAVER,
    'Bird': ANIMALS.BIRD,
    'Bunny': ANIMALS.BUNNY,
    'Cat': ANIMALS.CAT,
    'Horse': ANIMALS.HORSE,
    'Monkey': ANIMALS.MONKEY,
    'Reptile': ANIMALS.REPTILE,
    'Sheep': ANIMALS.SHEEP,
    'Sloth': ANIMALS.SLOTH,
    'Wolf': ANIMALS.WOLF
}