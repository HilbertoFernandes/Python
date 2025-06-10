# Importa a biblioteca 'requests' para fazer requisições HTTP
import requests

# Importa 'BeautifulSoup' da biblioteca 'bs4' para fazer o parsing do HTML
from bs4 import BeautifulSoup

# Importa ferramentas do sumy para leitura de texto e tokenização
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Importa o algoritmo de resumo LSA (Latent Semantic Analysis) do sumy
from sumy.summarizers.lsa import LsaSummarizer


# Função principal que recebe uma URL e o número de sentenças desejadas no resumo
def resumir_pagina(url, num_sentencas=5):
    try:
        # Faz uma requisição GET para a URL fornecida
        resposta = requests.get(url)

        # Gera um erro caso a resposta não tenha status 200 (ok)
        resposta.raise_for_status()

        # Usa o BeautifulSoup para fazer o parsing do conteúdo HTML retornado
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # Remove scripts (JavaScript) e estilos (CSS) para limpar o texto
        for script in soup(["script", "style"]):
            script.extract()

        # Extrai apenas o texto visível da página, com separadores entre elementos
        texto = soup.get_text(separator=' ', strip=True)

        # Cria um parser com o texto limpo, usando tokenização em português
        parser = PlaintextParser.from_string(texto, Tokenizer("portuguese"))

        # Instancia o resumidor LSA (Latent Semantic Analysis)
        summarizer = LsaSummarizer()

        # Gera o resumo com o número de sentenças definido (default = 5)
        resumo = summarizer(parser.document, num_sentencas)

        # Junta as sentenças em uma string única para exibição
        resumo_texto = ' '.join(str(sentenca) for sentenca in resumo)
        return resumo_texto

    # Em caso de erro (ex: site fora do ar, estrutura inválida), retorna a mensagem do erro
    except Exception as e:
        return f"Erro ao acessar ou processar a página: {e}"


# Ponto de entrada do script (só roda se for chamado diretamente, não como módulo importado)
if __name__ == "__main__":
    # Solicita ao usuário a URL da página a ser resumida
    url = input("Digite o endereço da página para resumir: ")

    # Chama a função de resumo com a URL fornecida
    resumo = resumir_pagina(url)

    # Exibe o resultado do resumo
    print("\nResumo:\n", resumo)
