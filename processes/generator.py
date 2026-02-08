import csv
import shutil
import uuid
from pathlib import Path

from models.voter import Voter
from tools.helper import (
    parse_csv_row_to_dict,
    convert_species_to_enum,
    convert_gender_to_enum,
    build_political_positions
)


def generate_animal_list(save_directory: Path, image_directory: Path, animal_data_csv_path: Path) -> list[Voter]:
    animal_list: list[Voter] = []
    with open(animal_data_csv_path, newline='', encoding='windows-1252') as csvfile:
        rows = csv.reader(csvfile)
        header_row = rows.__next__()
        headers = header_row
        while True:
            try:
                row = rows.__next__()
            except StopIteration:
                break
            animal_data_dict = parse_csv_row_to_dict(headers, row)
            voter_kwargs: dict = convert_voter_data_to_kwargs(animal_data_dict, image_directory)
            animal_list.append(Voter(**voter_kwargs))
    return animal_list


def convert_voter_data_to_kwargs(animal_data_dict: dict, image_directory: Path) -> dict:
    species = convert_species_to_enum(animal_data_dict["species"][0])
    gender = convert_gender_to_enum(animal_data_dict["gender"][0])
    positions = build_political_positions(animal_data_dict)
    
    filename_base = animal_data_dict["filename"][0]
    if not filename_base.endswith('.png'):
        filename_base = f"{filename_base}.png"
    
    return {
        "species": species,
        "filename": image_directory / filename_base,
        "gender": gender,
        "name": animal_data_dict["name"][0],
        "positions": positions
    }


def generate_and_zip_voter_deck(animal_list: list[Voter], save_directory: Path) -> Path:
    batch_uuid = str(uuid.uuid4())
    output_directory = save_directory / batch_uuid
    output_directory.mkdir(parents=True, exist_ok=True)
    
    for animal in animal_list:
        animal.generate_art(output_directory)
    
    temp_zip_path = save_directory / f"{batch_uuid}_voter_deck"
    shutil.make_archive(str(temp_zip_path), 'zip', output_directory)
    
    final_zip_path = output_directory / "voter_deck.zip"
    shutil.move(f"{temp_zip_path}.zip", final_zip_path)
    
    for item in output_directory.iterdir():
        if item.is_file() and item.suffix.lower() == ".png":
            item.unlink()
    
    return final_zip_path
