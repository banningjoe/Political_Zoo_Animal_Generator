from constants import ANIMALS

DECK_SIZE = 60
QUANTITY_OF_EACH_ANIMAL_IN_DECK = DECK_SIZE//len(list(ANIMALS))
PLATFORM_ADHERENCE = 0.5 # the mean adherence across all animals in a species to the platforms their species likes.
MEAN_FORS = 2
MEAN_AGAINSTS = 1

def generate_animal_list()