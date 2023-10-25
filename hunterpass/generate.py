import openai
import os
import itertools
import threading
import sys

def obter_chave_api():
    return os.getenv('OPENAI_API_KEY')

def loading_animation():
    # Define os caracteres para a animação
    animation_chars = itertools.cycle(['|', '/', '-', '\\'])

    # Função que imprime a animação na tela
    def animate():
        for char in animation_chars:
            sys.stdout.write('\r' + 'Gerando...' + char)
            sys.stdout.flush()
            threading.Event().wait(0.2)

    # Inicia a animação em uma thread
    thread = threading.Thread(target=animate)
    thread.start()
    return thread

def generate_wordlist(arquivo_saida="dicionario.txt"):
    chave_api = obter_chave_api()

    if chave_api is None:
        print("Erro: Chave API não encontrada. Por favor, defina a variável de ambiente OPENAI_API_KEY.")
        return
    
    num_variacoes = int(input("Digite o número de variações: "))
    comprimento_minimo = int(input("Digite o comprimento mínimo de cada palavra da senha: "))
    comprimento_maximo = int(input("Digite o comprimento máximo de cada palavra da senha: "))

    openai.api_key = chave_api

    mensagem_inicial = f"Gerar uma lista de palavras com as seguintes informações: " \
    f"Tamanho da Lista (Variações de Senha) = {num_variacoes}" \
    f"Comprimento Mínimo da Senha = {comprimento_minimo}." \
    f"Comprimento Máximo da Senha = {comprimento_maximo}."\
    "Misture as informações e não faça permutação.\n"

    entrada_usuario = []

    while True:
        informacao = input("Digite uma informação para a lista de palavras (Digite 'sair' para sair): ").lower()
        if informacao.lower() == 'sair':
            break
        entrada_usuario.append(informacao)

    mensagem_inicial += "\n".join([f"Informação: {info}" for info in entrada_usuario])

    mensagens = [{"role": "user", "content": mensagem_inicial}]

    # Inicia a animação
    animation_thread = loading_animation()

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
    )
    
    texto_gerado = resposta.choices[0].message['content'].strip()

    # Aguarda a animação terminar
    animation_thread.join()

    with open(arquivo_saida, 'w') as f:
        f.write(texto_gerado)

    print("\nGeração completada")

if __name__ == "__main__":
    generate_wordlist()
