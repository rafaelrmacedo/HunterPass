import openai
import os
import itertools
import threading
import sys

def get_api_key():
    return os.getenv('OPENAI_API_KEY')


def generate_wordlist(output_file="dicionario.txt"):
    api_key = get_api_key()

    if api_key is None:
        print("Erro: Chave API não encontrada. Por favor, defina a variável de ambiente OPENAI_API_KEY.")
        return
    
    def get_input(mensagem):
        while True:
            try:
                input_ = int(input(mensagem))
                return input_
            except ValueError:
                print("Por favor, digite apenas números.")


    variation_num = get_input("Digite o número de variações: ")
    min_length = get_input("Digite o comprimento mínimo de cada palavra da senha: ")
    max_length = get_input("Digite o comprimento máximo de cada palavra da senha: ")
    include_symbols = input("Quer utilizar simbolos especiais? (s/n): ").lower()

    while include_symbols not in ('s', 'n'):
        print("Por favor, responda com 's' para sim ou 'n' para não.")
        include_symbols = input("Quer utilizar simbolos especiais? (s/n): ").lower()


    openai.api_key = api_key

    start_message = f"Generate a wordlist with the information below: " \
    f"Wordlist Size (Variations) = {variation_num}" \
    f"Minimun password length = {min_length}." \
    f"Maximun password length = {max_length}." \
    f"Symbols: {include_symbols}."

    user_input = []

    while True:
        information = input("Digite uma informação para a lista de palavras (Digite 'sair' para sair): ").lower()
        if information.lower() == 'sair':
            break
        user_input.append(information)

    start_message += "\n".join([f"Information: {info}" for info in user_input])
    start_message += "\n Mix this informations and don't make simple permutations." \

    mensagens = [{"role": "user", "content": start_message}]

    print("\nGerando a lista de palavras...")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
    )
    
    generated_text = response.choices[0].message['content'].strip()

    with open(output_file, 'w') as f:
        f.write(generated_text)

    print("\nGeração completada.")


if __name__ == "__main__":
    generate_wordlist()
