import argparse
import os
from generate import generate_wordlist
from john import run_john

def main():
    os.system('cls')
    print('''
     __  __     __  __     __   __     ______   ______     ______    
    /\ \_\ \   /\ \/\ \   /\ "-.\ \   /\__  _\ /\  ___\   /\  == \   
    \ \  __ \  \ \ \_\ \  \ \ \-.  \  \/_/\ \/ \ \  __\   \ \  __<   
     \ \_\ \_\  \ \_____\  \ \_\\"\_\     \ \_\  \ \_____\  \ \_\ \_\ 
      \/_/\/_/   \/_____/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/ 
                                                                 
     ______   ______     ______     ______                           
    /\  == \ /\  __ \   /\  ___\   /\  ___\                          
    \ \  _-/ \ \  __ \  \ \___  \  \ \___  \                         
     \ \_\    \ \_\ \_\  \/\_____\  \/\_____\                        
      \/_/     \/_/\/_/   \/_____/   \/_____/                        
                                                                 
        v0.9.2 - Automatic dictionary generator with AI
        Developed by: Rafael Rodrigues Macedo

    ''')

    parser = argparse.ArgumentParser(
        prog='hunterpass',
        description='Automatic dictionary generator with AI',
        epilog='Developed by: Rafael Rodrigues Macedo')

    parser.add_argument('-j', '--john', action='store_true',
                        help='Run John the Ripper after generating the wordlist')

    args = parser.parse_args()

    generate_wordlist()

    # Run John the Ripper if the user passed the -j or --john argument
    if args.john:
        run_john()

if __name__ == '__main__':
    main()