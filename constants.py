from enum import Enum


class ANIMALS(Enum):
    SHEEP = "Sheep"
    WOLVES = "Wolves"
    SLOTH = "Sloth"
    LION = "Lion"
    BUNNIES = "Bunnies"
    HAWK = "Hawk"
    HORSES = "Horses"
    BEAVERS = "Beavers"
    ALLIGATORS = "Alligators"
    BEARS = "Bears"


class POLITICAL_PLATFORMS(Enum):
    UNIVERSAL_BASIC_FOOD_SUPPLY = "Universal Basic Food Supply"
    INCREASED_SPEED_LIMIT = "Increased Speed Limit"
    EXPANDED_HUNTING_GROUNDS = "Expanded Hunting Grounds"
    SUBSIDIZED_CHILDCARE = "Subsidized Childcare"
    TREE_PRESERVATION_ACT = "Tree Preservation Act"
    EXTENDED_HIBERNATION_LEAVE = "Extended Hibernation Leave"
    INCREASED_DAM_CONSTRUCTION_PERMITS = "Increased Dam Construction Permits"
    RIVER_RESTORATION_FUNDING = "River Restoration Funding"
    FOR_ALL = "For All Platforms"
    AGAINST_ALL = "Against All Platforms"


ANIMAL_POSITIONS = {
    ANIMALS.SHEEP: {
        "for": [POLITICAL_PLATFORMS.FOR_ALL],
        "against": []
    },
    ANIMALS.WOLVES: {
        "for": [],
        "against": [POLITICAL_PLATFORMS.AGAINST_ALL]
    },
    ANIMALS.SLOTH: {
        "for": [POLITICAL_PLATFORMS.UNIVERSAL_BASIC_FOOD_SUPPLY],
        "against": [POLITICAL_PLATFORMS.INCREASED_SPEED_LIMIT]
    },
    ANIMALS.LION: {
        "for": [POLITICAL_PLATFORMS.EXPANDED_HUNTING_GROUNDS],
        "against": [POLITICAL_PLATFORMS.UNIVERSAL_BASIC_FOOD_SUPPLY]
    },
    ANIMALS.BUNNIES: {
        "for": [POLITICAL_PLATFORMS.SUBSIDIZED_CHILDCARE],
        "against": [POLITICAL_PLATFORMS.EXPANDED_HUNTING_GROUNDS]
    },
    ANIMALS.HAWK: {
        "for": [POLITICAL_PLATFORMS.TREE_PRESERVATION_ACT],
        "against": [POLITICAL_PLATFORMS.EXTENDED_HIBERNATION_LEAVE]
    },
    ANIMALS.HORSES: {
        "for": [POLITICAL_PLATFORMS.INCREASED_SPEED_LIMIT],
        "against": [POLITICAL_PLATFORMS.TREE_PRESERVATION_ACT]
    },
    ANIMALS.BEAVERS: {
        "for": [POLITICAL_PLATFORMS.INCREASED_DAM_CONSTRUCTION_PERMITS],
        "against": [POLITICAL_PLATFORMS.RIVER_RESTORATION_FUNDING]
    },
    ANIMALS.ALLIGATORS: {
        "for": [POLITICAL_PLATFORMS.RIVER_RESTORATION_FUNDING],
        "against": [POLITICAL_PLATFORMS.SUBSIDIZED_CHILDCARE]
    },
    ANIMALS.BEARS: {
        "for": [POLITICAL_PLATFORMS.EXTENDED_HIBERNATION_LEAVE],
        "against": [POLITICAL_PLATFORMS.INCREASED_DAM_CONSTRUCTION_PERMITS]
    }
}