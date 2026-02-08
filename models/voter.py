from pathlib import Path

from constants import ANIMALS, GENDER, PoliticalPositions
from tools.image_helper import create_voter_card


class Voter():
    def __init__(self, species: ANIMALS, name: str, gender: GENDER, positions: PoliticalPositions, filename: Path):
        self.species = species
        self.positions = positions
        self.filename = filename
        self.name = name
        self.gender = gender

    def generate_art(self, output_directory: Path) -> Path:
        output_filename = self.filename.name
        output_path = output_directory / output_filename
        
        return create_voter_card(
            source_image_path=self.filename,
            output_path=output_path,
            name=self.name,
            positions=self.positions
        )
