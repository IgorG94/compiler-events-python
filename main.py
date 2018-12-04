from analisadorLexico.analise_lexica import AnalisadorLexico
from config import settings


# Teste do analisador léxico
print("***** TESTE DO ANALISADOR LÉXICO")
nome_arq = input("Digite o nome do arquivo: ")

analisador_lexico = AnalisadorLexico()
analisador_lexico.simulacao(
    nome_arq,
    settings['imprime_codigo_fonte'],
    settings['imprime_caracteres'],
    settings['imprime_linhas'],
    settings['imprime_eventos'],
    settings['imprime_arquivo']
)

sair = input("Pressione ENTER para sair")
