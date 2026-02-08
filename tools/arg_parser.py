import argparse
from pathlib import Path


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Generate political voter cards for animals from CSV data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Example usage:
  python main.py -c political_zoo_animals.csv
  python main.py --csv-path data.csv --image-dir images --save-dir output
        '''
    )
    
    parser.add_argument(
        '-c', '--csv-path',
        type=Path,
        required=True,
        help='Path to the CSV file containing animal data'
    )
    
    parser.add_argument(
        '-i', '--image-dir',
        type=Path,
        default=Path('political_zoo_images'),
        help='Path to the directory containing animal images (default: political_zoo_images)'
    )
    
    parser.add_argument(
        '-s', '--save-dir',
        type=Path,
        default=Path('save_directory'),
        help='Path to the directory where output will be saved (default: save_directory)'
    )
    
    parser.add_argument(
        '--samples',
        action='store_true',
        help='Extract 4 sample images to <uuid>/samples for preview'
    )
    
    return parser


def parse_arguments() -> argparse.Namespace:
    parser = create_parser()
    args = parser.parse_args()
    args.save_dir.mkdir(parents=True, exist_ok=True)
    return args
