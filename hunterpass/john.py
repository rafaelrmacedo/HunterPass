import subprocess
import os

def run_john(dictionary_file, hash_file, john_path):
    command = [john_path, '--wordlist=' + dictionary_file, hash_file]

    try:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o John the Ripper: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    dictionary_file = 'dictionary.txt'  # Substitua pelo caminho correto do seu arquivo de dicionário
    hash_file = input("Digite o caminho para o arquivo de hashes: ")

    os_name = os.name
    if os_name == 'posix':  # Linux ou MacOS
        john_path = 'john'  # Supondo que 'john' está no PATH
    elif os_name == 'nt':  # Windows
        john_path = input("Digite o caminho para o executável do John the Ripper: ")
    else:
        raise OSError(f"Sistema operacional não suportado: {os_name}")

    run_john(dictionary_file, hash_file, john_path)
