def generate_wordlist(output_file):
    # Aqui, você chamaria a API do OpenAI para gerar a wordlist com base no input_file
    # e depois salvaria no output_file ou em um nome padrão

    # Simulando a chamada à API (substitua isso pela chamada real à API)
    generated_text = f'Wordlist saved with success in {output_file} file.'

    if output_file is None:
        output_file = "wordlist.txt"  # default name for output file

    # save the output in the file
    with open(output_file, 'w') as f:
        f.write(generated_text)