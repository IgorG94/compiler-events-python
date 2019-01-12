from analisadorLexicoSintatico.decompositor_caracteres import (
    DecompositorCaracteres
)
from analisadorLexicoSintatico.analise_lexica import (
    AnalisadorLexico
)
from analisadorLexicoSintatico.analise_sintatica import (
    AnalisadorSintatico
)
from notacaoWirth.analise_lexica_wirth import (
    AnalisadorLexicoWirth
)
from notacaoWirth.analise_sintatica_wirth import (
    AnalisadorSintaticoWirth
)

print("Voce deseja testar o decompositor de caracteres, ",
      "o analisador lexico ou o reconhecedor da Notacao de Wirth?")
print("Digite 1 para decompositor de caracteres")
print("Digite 2 para o analisador lexico")
print("Digite 3 para o analisador sintatico e semantico")
print("Digite 4 para o reconhecedor da Notacao de Wirth")

teste = input()

# OBS: Pode-se utilizar o arquivo config para determinar o valor das variáveis
# de impressão do compilador
# Se for um teste do decompositor de caracteres
if (teste == "1"):
    print("***** TESTE DO DECOMPOSITOR DE CARACTERES *****")
    nome_arq = input(
        "Digite o nome do arquivo (ex.: teste1.txt): "
    )
    aux_imprime_codigo_fonte = input(
        "Imprimir no terminal o codigo fonte (s/n)? "
    )
    aux_imprime_caracteres = input(
        "Imprimir no terminal a lista de caracteres (s/n)? "
    )
    aux_imprime_linhas = input(
        "Imprimir no terminal as linhas (s/n)? "
    )
    aux_imprime_eventos = input(
        "Imprimir no terminal os eventos (s/n)? "
    )
    aux_imprime_arquivo = input(
        "Imprimir num arquivo as informacoes anteriores (s/n)? "
    )

    print("\n")

    imprime_codigo_fonte = False
    imprime_caracteres = False
    imprime_linhas = False
    imprime_eventos = False
    imprime_arquivo = False

    if (aux_imprime_codigo_fonte == "s"):
        imprime_codigo_fonte = True

    if (aux_imprime_caracteres == "s"):
        imprime_caracteres = True

    if (aux_imprime_linhas == "s"):
        imprime_linhas = True

    if (aux_imprime_eventos == "s"):
        imprime_eventos = True

    if (aux_imprime_arquivo == "s"):
        imprime_arquivo = True

    decompositor = DecompositorCaracteres()
    decompositor.simulacao(
        nome_arq,
        imprime_codigo_fonte,
        imprime_caracteres,
        imprime_linhas,
        imprime_eventos,
        imprime_arquivo
    )

# Se for um teste do analisador léxico
elif (teste == "2"):
    print("***** TESTE DO ANALISADOR LEXICO *****")
    nome_arq = input(
        "Digite o nome do arquivo (ex.: teste1.txt): "
    )
    aux_imprime_lista_caracteres = input(
        "Imprimir no terminal a lista de caracteres (s/n)? "
    )
    aux_imprime_atomos = input(
        "Imprimir no terminal os atomos (s/n)? "
    )
    aux_imprime_arquivo = input(
        "Imprimir em um arquivo a lista de atomos (s/n)? "
    )

    imprime_lista_caracteres = False
    imprime_atomos = False
    imprime_arquivo = False

    if (aux_imprime_lista_caracteres == "s"):
        imprime_lista_caracteres = True

    if (aux_imprime_atomos == "s"):
        imprime_atomos = True

    if (aux_imprime_arquivo == "s"):
        imprime_arquivo = True

    # Leitura do arquivo
    try:
        arq = open(nome_arq, "r")
        arq.close()

        decompositor = DecompositorCaracteres()
        decompositor.simulacao(nome_arq, False, False, False, False, False)

        lista_char = decompositor.lista_caracteres

        decompositor.lista_eventos = []
        analisador = AnalisadorLexico()
        analisador.simulacao(
            lista_char,
            imprime_lista_caracteres,
            imprime_atomos,
            imprime_arquivo
        )

        sair = input("Pressione ENTER para sair")

    except FileNotFoundError:
        print("O arquivo ", nome_arq, " nao foi encontrado!")
        input("Pressione ENTER para sair")

# Se for um teste do analisador sintático e semântico
elif (teste == "3"):
    print("***** TESTE DO ANALISADOR SINTATICO E SEMANTICO *****")

    nome_arq = input(
        "Digite o nome do arquivo com o codigo fonte (ex.: teste1.txt): "
    )
    aux_imprime_lista_atomos = input(
        "Imprimir no terminal os atomos (s/n)? "
    )
    aux_imprime_arquivo = input(
        "Imprimir em um arquivo a lista de atomos (s/n)? "
    )

    imprime_lista_atomos = False
    imprime_arquivo = False

    if (aux_imprime_lista_atomos == "s"):
        imprime_lista_atomos = True

    if (aux_imprime_arquivo == "s"):
        imprime_arquivo = True

    # Leitura do arquivo
    try:
        arq = open(nome_arq, "r")
        arq.close()

        decompositor = DecompositorCaracteres()
        decompositor.simulacao(nome_arq, False, False, False, False, False)

        lista_char = decompositor.lista_caracteres

        decompositor.lista_eventos = []
        lexico = AnalisadorLexico()
        lexico.simulacao(lista_char, False, False, False)

        lista_atomos = lexico.lista_atomos

        lexico.lista_eventos = []
        sintatico = AnalisadorSintatico()
        sintatico.simulacao(
            lista_atomos,
            imprime_lista_atomos,
            imprime_arquivo
        )

        sair = input("Pressione ENTER para sair")

    except FileNotFoundError:
        print("O arquivo ", nome_arq, " nao foi encontrado!")
        input("Pressione ENTER para sair")

# Se for um teste do reconhecedor da Notação de Wirth
elif (teste == "4"):
    print("***** TESTE DO RECONHECEDOR DA NOTACAO DE WIRTH *****")
    print("Qual parte do reconhecedor voce deseja testar?")
    print("Digite 1 para o decompositor de caracteres")
    print("Digite 2 para a analise lexica")
    print("Digite 3 para a analise sintatica")
    teste_wirth = input()

    # Se for teste do decompositor de caracteres
    if (teste_wirth == "1"):
        print("* TESTE DO DECOMPOSITOR DE CARACTERES *")
        nome_arq2 = input(
            "Digite o nome do arquivo (ex.: teste1.txt): "
        )
        aux_imprime_codigo_fonte = input(
            "Imprimir no terminal o codigo fonte (s/n)? "
        )
        aux_imprime_caracteres = input(
            "Imprimir no terminal a lista de caracteres (s/n)? "
        )
        aux_imprime_linhas = input(
            "Imprimir no terminal as linhas (s/n)? "
        )
        aux_imprime_eventos = input(
            "Imprimir no terminal os eventos (s/n)? "
        )
        aux_imprime_arquivo = input(
            "Imprimir num arquivo as informacoes anteriores (s/n)? "
        )

        print("\n")

        imprime_codigo_fonte = False
        imprime_caracteres = False
        imprime_linhas = False
        imprime_eventos = False
        imprime_arquivo = False

        if (aux_imprime_codigo_fonte == "s"):
            imprime_codigo_fonte = True

        if (aux_imprime_caracteres == "s"):
            imprime_caracteres = True

        if (aux_imprime_linhas == "s"):
            imprime_linhas = True

        if (aux_imprime_eventos == "s"):
            imprime_eventos = True

        if (aux_imprime_arquivo == "s"):
            imprime_arquivo = True

        decompositor = DecompositorCaracteres()
        decompositor.simulacao(
            nome_arq2,
            imprime_codigo_fonte,
            imprime_caracteres,
            imprime_linhas,
            imprime_eventos,
            imprime_arquivo
        )

    # Se for teste da análise léxica do reconhecedor da notação de Wirth
    elif (teste_wirth == "2"):
        print("* TESTE DO ANALISADOR LEXICO DA NOTACAO DE WIRTH *")
        nome_arq = input(
            "Digite o nome do arquivo com o codigo fonte (ex.: teste1.txt): "
        )
        aux_imprime_lista_caracteres = input(
            "Imprimir no terminal a lista de caracteres (s/n)? "
        )
        aux_imprime_atomos = input(
            "Imprimir no terminal os atomos (s/n)? "
        )
        aux_imprime_arquivo = input(
            "Imprimir em um arquivo a lista de atomos (s/n)? "
        )

        imprime_lista_caracteres = False
        imprime_atomos = False
        imprime_arquivo = False

        if (aux_imprime_lista_caracteres == "s"):
            imprime_lista_caracteres = True

        if (aux_imprime_atomos == "s"):
            imprime_atomos = True

        if (aux_imprime_arquivo == "s"):
            imprime_arquivo = True

        # Leitura do arquivo
        try:
            arq = open(nome_arq, "r")
            arq.close()

            decompositor = DecompositorCaracteres()
            decompositor.simulacao(nome_arq, False, False, False, False, False)

            lista_char = decompositor.lista_caracteres

            decompositor.lista_eventos = []
            analisador = AnalisadorLexicoWirth()
            analisador.simulacao(
                lista_char,
                imprime_lista_caracteres,
                imprime_atomos,
                imprime_arquivo
            )

            sair = input("Pressione ENTER para sair")

        except FileNotFoundError:
            print("O arquivo ", nome_arq, " nao foi encontrado!")
            input("Pressione ENTER para sair")

    # Se for teste da análise sintática do reconhecedor da notação de Wirth
    elif (teste_wirth == "3"):
        print("* TESTE DO ANALISADOR SINTATICO DA NOTACAO DE WIRTH *")
        nome_arq = input(
            "Digite o nome do arquivo com o codigo fonte (ex.: teste1.txt): "
        )
        aux_imprime_lista_atomos = input(
            "Imprimir no terminal os atomos (s/n)? "
        )
        aux_imprime_arquivo = input(
            "Imprimir em um arquivo a lista de atomos (s/n)? "
        )

        imprime_lista_atomos = False
        imprime_arquivo = False

        if (aux_imprime_lista_atomos == "s"):
            imprime_lista_atomos = True

        if (aux_imprime_arquivo == "s"):
            imprime_arquivo = True

        # Leitura do arquivo
        try:
            arq = open(nome_arq, "r")
            arq.close()

            decompositor = DecompositorCaracteres()
            decompositor.simulacao(nome_arq, False, False, False, False, False)

            lista_char = decompositor.lista_caracteres

            decompositor.lista_eventos = []
            lexico = AnalisadorLexicoWirth()
            lexico.simulacao(lista_char, False, False, False)

            lista_atomos = lexico.lista_atomos

            lexico.lista_eventos = []
            sintatico = AnalisadorSintaticoWirth()
            sintatico.simulacao(
                lista_atomos,
                imprime_lista_atomos,
                imprime_arquivo
            )

            sair = input("Pressione ENTER para sair")

        except FileNotFoundError:
            print("O arquivo ", nome_arq, " nao foi encontrado!")
            input("Pressione ENTER para sair")

else:
    print("Opcao invalida!")
    sair = input("Pressione ENTER para sair")