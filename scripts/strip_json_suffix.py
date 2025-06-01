import argparse
from pathlib import Path


def strip_json_suffix(directory: Path) -> int:
    count = 0
    for file_path in directory.iterdir():
        if file_path.is_file() and file_path.name.endswith('.json.yaml'):
            new_name = file_path.name.replace('.json.yaml', '.yaml')
            new_path = directory / new_name
            file_path.rename(new_path)
            print(f"✅ Renamed: {file_path.name} → {new_name}")
            count += 1
    return count

def main():
    parser = argparse.ArgumentParser(description="Strip .json.yaml suffix from files in a directory")
    parser.add_argument('--dir', type=Path, required=True, help="Directory containing YAML files")
    args = parser.parse_args()

    if not args.dir.is_dir():
        print(f"❌ Error: {args.dir} is not a valid directory")
        return

    count = strip_json_suffix(args.dir)
    print(f"🎉 Done! Stripped .json.yaml suffix from {count} file(s) in {args.dir}")

if __name__ == "__main__":
    main()
