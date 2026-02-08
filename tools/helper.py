from collections import defaultdict

from constants import (
    ANIMALS,
    CSV_COLUMN_HEADERS_TO_VOTER_INPUTS as CNVRT,
    CSV_SPECIES_TO_ANIMALS,
    GENDER,
    POLITICAL_PLATFORMS,
    PoliticalPositions
)


def parse_csv_row_to_dict(headers: list[str], row: list[str]) -> defaultdict:
    animal_data_dict = defaultdict(list)
    for i, value in enumerate(row):
        if headers[i] in CNVRT:
            animal_data_dict[CNVRT[headers[i]]].append(value)
    return animal_data_dict


def convert_species_to_enum(species_str: str) -> ANIMALS:
    return CSV_SPECIES_TO_ANIMALS[species_str]


def convert_gender_to_enum(gender_str: str) -> GENDER:
    return GENDER.MALE if gender_str == "Male" else GENDER.FEMALE


def parse_platform_string_to_enum(platform_str: str) -> POLITICAL_PLATFORMS | None:
    if not platform_str or not platform_str.strip():
        return None
    for platform in POLITICAL_PLATFORMS:
        if platform.value == platform_str:
            return platform
    return None


def parse_positions_list(positions_raw: list[str]) -> list[POLITICAL_PLATFORMS]:
    positions: list[POLITICAL_PLATFORMS] = []
    for pos in positions_raw:
        platform = parse_platform_string_to_enum(pos)
        if platform:
            positions.append(platform)
    return positions


def build_political_positions(animal_data_dict: defaultdict) -> PoliticalPositions:
    positive_positions_raw = animal_data_dict.get("positive_positions", [])
    negative_positions_raw = animal_data_dict.get("negative_positions", [])
    
    return {
        "FOR": parse_positions_list(positive_positions_raw),
        "AGAINST": parse_positions_list(negative_positions_raw)
    }
