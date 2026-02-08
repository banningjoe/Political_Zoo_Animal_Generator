import zipfile
from processes.generator import generate_animal_list, generate_and_zip_voter_deck
from tools.arg_parser import parse_arguments


def extract_samples(zip_path, sample_count=4):
    samples_dir = zip_path.parent / 'samples'
    samples_dir.mkdir(exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        all_files = sorted(zip_ref.namelist())
        sample_files = all_files[:sample_count]
        
        for sample_file in sample_files:
            zip_ref.extract(sample_file, samples_dir)
    
    return samples_dir


def main() -> None:
    args = parse_arguments()
    
    print(f"Loading animals from {args.csv_path}...")
    animals = generate_animal_list(
        image_directory=args.image_dir,
        animal_data_csv_path=args.csv_path
    )
    print(f"✓ Loaded {len(animals)} animals")
    
    print(f"\nGenerating voter deck...")
    zip_path = generate_and_zip_voter_deck(animals, args.save_dir)
    
    print(f"\n✓ Success! Created: {zip_path}")
    print(f"✓ Zip size: {zip_path.stat().st_size / (1024*1024):.2f} MB")
    
    if args.samples:
        print(f"\nExtracting sample images...")
        samples_dir = extract_samples(zip_path)
        print(f"✓ Samples saved to: {samples_dir}")


if __name__ == "__main__":
    main()
