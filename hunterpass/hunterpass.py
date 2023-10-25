import argparse
import os
from generate import generate_wordlist
from john import run_john

def main():
    os.system('cls')
    print('''
     _    _   _   _    _     _   _______   _______   ______         
    | |  | | | |  | | | |   | | |__   __| |  _____| |  __  |
    | |__| | | |  | | |  \  | |    | |    | |____   | |__| /
    |  __  | | |  | | | |\ \| |    | |    |  ____|  |  __ \ 
    | |  | | | |__| | | | \_  |    | |    | |_____  | |  \ \ 
    |_|  |_| \______/ |_|   |_|    |_|    |_______| |_|   \_\ 
             ______   ______   ______   ______
            |  __  | |  __  | |  ____| |  ____| 
            | |__| | | |__| |  \ \__    \ \__
            |  ____| |  __  |   \__ \    \__ \ 
            | |      | |  | |  ____\ \   ___\ \ 
            |_|      |_|  |_| |_______| |______|    
    ''')

    parser = argparse.ArgumentParser(
        prog='hunterpass',
        description='Automatic dictionary generator with AI',
        epilog='Developed by: Rafael Rodrigues Macedo')

    parser.add_argument('-j', '--john', action='store_true',
                        help='Run John the Ripper after generating the wordlist')

    args = parser.parse_args()

    generate_wordlist()

    if args.john:
        dictionary_file = 'dictionary.txt'
        hash_file = input("Enter the path to the hash file: ")

        os_name = os.name
        if os_name == 'posix':  # Linux or MacOS
            john_path = 'john'  # Assuming 'john' is in the PATH
        elif os_name == 'nt':  # Windows
            john_path = input("Enter the path to the John the Ripper executable: ")
        else:
            raise OSError(f"Unsupported operating system: {os_name}")

        run_john(dictionary_file, hash_file, john_path)

if __name__ == '__main__':
    main()