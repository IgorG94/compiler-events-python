from analisadorLexico.decompositor_caracteres import DecompositorCaracteres
from config import settings


# Teste do analisador léxico
print("***** TESTE DO DECOMPOSITOR DE CARACTERES")
nome_arq = input("Digite o nome do arquivo: ")

decompositor = DecompositorCaracteres()
decompositor.simulacao(
    nome_arq,
    settings['imprime_codigo_fonte'],
    settings['imprime_caracteres'],
    settings['imprime_linhas'],
    settings['imprime_eventos'],
    settings['imprime_arquivo']
)

sair = input("Pressione ENTER para sair")
