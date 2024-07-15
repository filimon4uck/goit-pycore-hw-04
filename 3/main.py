import sys
from pathlib import Path
from colorama import Fore


def print_dirs_files(path, indent=0):
    path = Path(path)
    if not path.is_dir():
        print(f"The path: {path} is not a directory.")
        return

    prefix = ' ' * indent
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{Fore.BLUE}{prefix}{item.name}/{Fore.RESET}")
            print_dirs_files(item, indent + 4)
        elif item.is_file():
            print(f"{Fore.GREEN}{prefix}{item.name}{Fore.RESET}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Add path to sys argv{Fore.RESET}")
    else:
        base_path = sys.argv[1]
        print_dirs_files(base_path)
