from nucleoMotorEventos.nucleo_motor_eventos import (
    NucleoMotorEventos,
    Evento
)

# Eventos que ocorrem durante a análise léxica:
# ler_codigo: Leitura de código fonte do programa a ser compilado
# ler_char: Leitura de caractere do código fonte, criando átomos

ler_codigo = Evento("ler_codigo", 1)
ler_char = Evento("ler_char", 2)


# Núcleo do decompositor de caracteres
class DecompositorCaracteres(NucleoMotorEventos):
    def __init__(self):
        NucleoMotorEventos.__init__(self)
        # Variáveis auxiliares
        self.posicao_atual = 0
        self.lista_caracteres = []
        self.lista_atomos = []
        self.linha_atual = ["", 1]  # [{linha}, {número da linha}]
        self.lista_linhas = []

    # Tratamento do evento de leitura do código fonte
    def ler_codigo(self, arq):
        # Leitura do arquivo
        try:
            self.arquivo = open(arq, "r")
            self.codigo = self.arquivo.read()
            self.arquivo.close()
        except FileNotFoundError:
            print("Esse arquivo não existe!")
            return

        self.tamanho_codigo = len(self.codigo)

        # Criação de evento de ler_char
        self.lista_eventos.append(ler_char)

        # Se estiver ativado, imprime o código fonte
        if (self.imprime_codigo_fonte):
            print("*** INÍCIO DO CÓDIGO FONTE ***\n")
            print(self.codigo)
            print("*** FIM DO CÓDIGO FONTE ***\n")

    # Tratamento do evento de leitura de caractere
    def ler_char(self):
        char_atual = self.codigo[self.posicao_atual]
        ascii_char = ord(char_atual)

        # Caso ainda haja caracteres a serem lidos, cria outro evento
        if (self.posicao_atual < len(self.codigo)):
            self.lista_eventos.append(ler_char)

        # Caso ainda não tenha alcançado o fim da linha
        if (ascii_char != 10):

            # Caso o caractere seja uma letra
            if ((ascii_char >= 65 and ascii_char <= 90) or
                    (ascii_char >= 97 and ascii_char <= 122)):
                tipo = "letter"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja um dígito
            elif (ascii_char >= 48 and ascii_char <= 57):
                tipo = "digit"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja um espaço ou tabulação
            elif (ascii_char == 32 or ascii_char == 9):
                tipo = "whitespace"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja de atribuição
            elif (ascii_char == 61):
                tipo = "assignment"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja de comparação (maior que)
            elif (ascii_char == 62):
                tipo = "compgreater"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja de comparação (menor que)
            elif (ascii_char == 60):
                tipo = "compless"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja de comparação (diferente)
            elif (ascii_char == 33):
                tipo = "compdiff"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja um operador aritmético
            elif (ascii_char == 43 or ascii_char == 45 or ascii_char == 42 or
                    ascii_char == 47 or ascii_char == 94):
                tipo = "arithmetic"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja de pontuação
            elif (ascii_char == 46 or ascii_char == 44 or ascii_char == 34):
                tipo = "punctuation"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja delimitador (parênteses)
            elif (ascii_char == 40 or ascii_char == 41):
                tipo = "delimiter"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Caso o caractere seja especial (nenhuma das categorias acima)
            else:
                tipo = "special"
                char = [char_atual, tipo, self.linha_atual[1]]
                self.insere_caractere(char)

            # Se estiver ativado, imprime o caractere e seu código ASCII
            if (self.imprime_caracteres):
                print(char[0], ": ", ord(char[0]), ", ", char[1])

            # Adiciona caractere à linha atual
            self.linha_atual[0] += char_atual

        # Caso tenha alcançado o fim da linha, insere-a na lista de linhas
        else:
            tipo = "whitespace"
            char = [" ", tipo, self.linha_atual[1]]
            if (self.imprime_caracteres):
                print(char[0], ": ", ord(char[0]), ", ", char[1])
            self.insere_caractere(char)

            # Inserção na lista de linhas
            self.lista_linhas.append(list(self.linha_atual))

            # Se estiver ativado, imprime a linha
            if (self.imprime_linhas):
                print("Linha ",
                      self.lista_linhas[self.linha_atual[1] - 1][1],
                      " = ",
                      self.lista_linhas[self.linha_atual[1] - 1][0])

            self.linha_atual[0] = ""
            self.linha_atual[1] += 1

        # Incrementa a posição de caracteres no código fonte
        self.posicao_atual += 1

    # Função que insere caractere na lista de caracteres, sem repetir
    def insere_caractere(self, char):
        self.lista_caracteres.append(char)

    # Função que roda o motor de eventos, recebendo um arquivo .txt com um
    # código fonte e realizando a simulação
    def simulacao(
        self,
        arq,
        imprime_codigo_fonte,
        imprime_caracteres,
        imprime_linhas,
        imprime_eventos,
        imprime_arquivo
    ):
        # Variáveis de ativação de impressões
        self.imprime_codigo_fonte = imprime_codigo_fonte
        self.imprime_caracteres = imprime_caracteres
        self.imprime_linhas = imprime_linhas
        self.imprime_eventos = imprime_eventos
        self.imprime_arquivo = imprime_arquivo

        # Para iniciar, cria-se um evento de leitura do código fonte
        self.lista_eventos.append(ler_codigo)

        # Percorre lista de eventos
        i = 0
        while (i < len(self.lista_eventos)):
            evento = self.lista_eventos[i]

            # Evento de leitura do código fonte
            if (evento.nome == "ler_codigo"):
                self.ler_codigo(arq)

            # Evento de leitura de caractere
            elif (evento.nome == "ler_char"):
                if (self.posicao_atual < len(self.codigo)):
                    self.ler_char()

            else:
                print("Evento ", evento.nome, "não existe!")
            i += 1

        # Insere whitespace ao final da lista de caracteres
        tipo = "whitespace"
        char = [" ", tipo, self.linha_atual[1]]
        self.insere_caractere(char)

        # Se a impressao de Eventos no terminal estiver ativada
        if (imprime_eventos):
            self.imprime_lista_eventos()

        # Se a impressão do arquivo de saída estiver ativada
        if (imprime_arquivo):
            self.imprime_arquivo_saida()

    # Funcao que imprime em um arquivo .txt os caracteres (com seus respectivos
    # tipos), as linhas e os eventos (com seus respectivos tipos)
    def imprime_arquivo_saida(self):
        arq_saida = open("saida_decompositor_caracteres.txt", "w")

        # 1 - Impressão do código fonte
        arq_saida.write("*** CÓDIGO FONTE ***\n")
        for i in range(len(self.lista_linhas)):
            linha = "Linha " + str(i+1) + ": " + str(self.lista_linhas[i][0])
            arq_saida.write(linha)
            arq_saida.write("\n")
        arq_saida.write("*** FIM DO CÓDIGO FONTE ***\n\n\n")

        # 2 - Impressão da lista de caracteres
        arq_saida.write("*** LISTA DE CARACTERES ***\n")
        for i in range(len(self.lista_caracteres)):
            char = self.lista_caracteres[i][0]
            tipo = self.lista_caracteres[i][1]
            linha = self.lista_caracteres[i][2]
            aux = ("Caractere: '" + str(char) + "', Tipo: " + str(tipo) +
                   ", Linha: " + str(linha) + "\n")
            arq_saida.write(aux)
        arq_saida.write("*** FIM DA LISTA DE CARACTERES ***\n\n\n")

        arq_saida.close()
