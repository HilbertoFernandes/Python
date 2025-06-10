import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def resumir_pagina(url, num_sentencas=5):
    try:
        # Pega o conteúdo da página
        resposta = requests.get(url)
        resposta.raise_for_status()

        # Extrai o texto da página (removendo tags HTML)
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # Remove scripts e estilos para limpar o texto
        for script in soup(["script", "style"]):
            script.extract()

        texto = soup.get_text(separator=' ', strip=True)

        # Usa o sumy para gerar o resumo
        parser = PlaintextParser.from_string(texto, Tokenizer("portuguese"))
        summarizer = LsaSummarizer()
        resumo = summarizer(parser.document, num_sentencas)

        # Junta as sentenças resumidas em um texto só
        resumo_texto = ' '.join(str(sentenca) for sentenca in resumo)
        return resumo_texto

    except Exception as e:
        return f"Erro ao acessar ou processar a página: {e}"

if __name__ == "__main__":
    url = input("Digite o endereço da página para resumir: ")
    resumo = resumir_pagina(url)
    print("\nResumo:\n", resumo)
