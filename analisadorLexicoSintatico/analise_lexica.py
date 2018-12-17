from nucleoMotorEventos.nucleo_motor_eventos import (
    NucleoMotorEventos,
    Evento
)
from analisadorLexicoSintatico.automato_reconhecedor_lexico import (
    AutomatoReconhecedorLexico
)

# Eventos que ocorrem durante a análise léxica:
# ler_lista_char: Leitura de lista de caracteres, resultado do decompositor
# ler_char: Leitura de caractere da lista de caracteres
# criar_atomo: Reconhecimento do átomo montado

ler_lista_char = Evento("ler_lista_char", 1)
ler_char = Evento("ler_char", 2)
criar_atomo = Evento("criar_atomo", 3)


class AnalisadorLexico(NucleoMotorEventos):
    def __init__(self):
        NucleoMotorEventos.__init__(self)
        # Variáveis auxiliares
        # Reserved: “ABS” | “ATN” | “COS” | “DATA” | “DEF” | “DIM” |
        # “END” | “EXP” | “FN” | “FOR” | “GO” | “GOSUB” | “GOTO” | “IF” | “INT”
        # | “LET” | “LOG” | “NEXT” | “PRINT” | “READ” | “REM” | “RETURN” |
        # “RND” | “SIN” | “SQR” | “STEP” | “TAN” | “THEN” | “TO” .
        self.lista_reservadas = [["ABS", "method", 1],
                                 ["ATN", "method", 2],
                                 ["COS", "method", 3],
                                 ["DATA", "data", 4],
                                 ["DEF", "define", 5],
                                 ["DIM", "matrix", 6],
                                 ["END", "ending", 7],
                                 ["EXP", "method", 8],
                                 ["FN", "function", 9],
                                 ["FOR", "forloop", 10],
                                 ["GO", "jump", 11],
                                 ["GOSUB", "jump", 12],
                                 ["GOTO", "jump", 13],
                                 ["IF", "conditional", 14],
                                 ["INT", "integer", 15],
                                 ["LET", "attribution", 16],
                                 ["LOG", "method", 17],
                                 ["NEXT", "nextiterator", 18],
                                 ["PRINT", "print", 19],
                                 ["READ", "read", 20],
                                 ["REM", "remark", 21],
                                 ["RETURN", "return", 22],
                                 ["RND", "method", 23],
                                 ["SIN", "method", 24],
                                 ["SQR", "method", 25],
                                 ["STEP", "step", 26],
                                 ["TAN", "method", 27],
                                 ["THEN", "resultconditional", 28],
                                 ["TO", "jumpto", 29]]

        self.lista_identificadores = []
        # Outros átomos terminais:
        # Assignment = “=”
        # Comparison = “==” | “<” | “<=” | “<>” | “>=” | “>”
        # ArithmeticPlusMinus = “+” | “-”
        # ArithmeticOther = “*” | “/” | “^”
        # Dot = “.”
        # Comma = “,”
        # Quotation = “””
        # DelimiterOpen = “(“
        # DelimiterClose = “)”
        self.pos_atual = 0
        self.lista_atomos = []
        self.atomo_atual = []
        self.reconhecedor = AutomatoReconhecedorLexico()

    # Tratamento do evento de leitura da lista de caracteres
    def ler_lista_char(self, lista_caracteres, imprime_lista_caracteres):
        self.lista_char = lista_caracteres
        self.tamanho_lista_char = len(self.lista_char)

        # Cria evento de leitura de caractere
        self.lista_eventos.append(ler_char)

        # Se estiver ativado, imprime lista de caracteres
        if (imprime_lista_caracteres):
            print("*** INÍCIO DA LISTA DE CARACTERES ***\n")

            for i in range(self.tamanho_lista_char):
                caractere = self.lista_char[i]
                char = caractere[0]
                tipo = caractere[1]
                linha = caractere[2]
                print("Caractere: '(", char, "', Tipo: ", tipo, ", Linha: ",
                      linha)

            print("*** FIM DA LISTA DE CARACTERES ***\n")

    # Tratamento do evento de leitura de caractere
    def ler_char(self):
        # Tipos de caracteres:
        # Letter
        # Digit
        # Special
        # Whitespace = “ “ | TABULAÇÃO | FIM DE LINHA
        # Assignment = “=”
        # ComparisonGreater = “>”
        # ComparisonLess = “<”
        # ArithmeticPlusMinus = “+” | “-”
        # ArithmeticOther = “*” | “/” | “^”
        # Dot = “.”
        # Comma = “,”
        # Quotation = “””
        # DelimiterOpen = “(“
        # DelimiterClose = “)”

        if (self.pos_atual < len(self.lista_char)):
            # Obtém próximo caractere
            char_atual = self.lista_char[self.pos_atual]

            # Se for caractere inválido, retorna erro de compilação
            if (char_atual[1] == "invalid"):
                print("Caractere %s nao pertence a linguagem" % char_atual[0])
                print("Erro na linha %s" % char_atual[2])
                return

            # Se for primeiro caractere após whitespace
            elif (char_atual[1] != "whitespace" and len(
                    self.atomo_atual) == 0):
                # Insere primeiro caractere do átomo
                self.atomo_atual.append(list(char_atual))
                # Cria evento de leitura de caractere
                self.lista_eventos.append(ler_char)

            # Se for outro caractere que não whitespace
            elif (char_atual[1] != "whitespace" and len(
                    self.atomo_atual) >= 0):
                # Insere primeiro caractere do átomo
                self.atomo_atual.append(list(char_atual))
                # Cria evento de leitura de caractere
                self.lista_eventos.append(ler_char)

            # Se for whitespace após caractere válido, cria átomo
            elif (char_atual[1] == "whitespace" and len(
                    self.atomo_atual) > 0):
                # Cria evento de criação de átomo
                self.lista_eventos.append(criar_atomo)

            # Se for whitespace após whitespace
            elif (char_atual[1] == "whitespace" and len(
                    self.atomo_atual) == 0):
                # Cria evento de leitura de caractere
                self.lista_eventos.append(ler_char)

            self.pos_atual += 1

        else:
            return

    # Tratamento do evento de criação de átomo
    def criar_atomo(self):
        # cadeia[i][0] -> caractere
        # cadeia[i][1] -> tipo
        cadeia = list(self.atomo_atual)

        # Verificação do tipo de terminal
        # atomo_final[0] -> string
        # atomo_final[1] -> tipo do átomo
        # atomo_final[2] -> linha
        self.atomo_final = self.reconhecedor.reconhece_cadeia(cadeia)

        # Tipo do átomo terminal
        tipo_terminal = self.atomo_final[1]

        # Se for inválido
        if (tipo_terminal == "invalid"):
            aux = ""
            for char in cadeia:
                aux += char[0]

            # Imprime no terminal uma mensagem de erro
            print("Atomo invalido: '%s', linha %s" % (aux,
                                                      self.atomo_final[2]))

            # Imprime no arquivo de saída a mensagem de erro
            arq_saida = open("saida_analisador_lexico.txt", "w")
            arq_saida.write("Atomo invalido: '%s', linha %s" % (
                aux,
                self.atomo_final[2])
            )
            arq_saida.close()
            return False

        # Se for identificador
        elif (tipo_terminal == "identifier"):
            # Verifica se é uma palavra reservada
            reservada = self.palavra_reservada(self.atomo_final[0])
            tipo_reservada = self.lista_reservadas[reservada[1] - 1][1]

            # Caso seja reservada
            if (reservada[0]):
                # Substitui tipo de identifier para reserved
                self.atomo_final.insert(1, str(tipo_reservada))
                self.atomo_final.remove("identifier")

                # Insere átomo na lista de átomos
                self.lista_atomos.append(list(self.atomo_final))

            # Caso seja identificador
            else:
                # Verifica se o identificador existe
                ident = self.identificador(self.atomo_final[0])

                # Caso exista
                if (ident[0]):
                    # Insere um id no átomo
                    self.atomo_final.append(ident[1])

                    # Insere átomo na lista de átomos
                    self.lista_atomos.append(list(self.atomo_final))

                # Caso não exista, cria-se um na lista de identificadores
                else:
                    nome_ident = self.atomo_final[0]
                    id_ident = len(self.lista_identificadores) + 1
                    self.lista_identificadores.append([nome_ident, id_ident])

                    # Insere o id_ident no átomo
                    self.atomo_final.append(id_ident)

                    # Insere átomo na lista de átomos
                    self.lista_atomos.append(list(self.atomo_final))

        # Insere o resto na lista de átomos
        else:
            self.lista_atomos.append(self.atomo_final)

        # Insere evento de leitura de caractere
        self.lista_eventos.append(ler_char)

        # Caso a impressão de átomos esteja ativa
        if (self.imprime_atomos):
            atomo = self.atomo_final
            string_atomo = atomo[0]
            tipo = atomo[1]
            linha = atomo[2]

            print("Linha: ", str(linha), ", Atomo: '", string_atomo,
                  "', Tipo: ", tipo)

        # Limpa átomo atual
        self.atomo_atual = []

        return True

    # *** FUNÇÕES AUXILIARES ***
    # Função que verifica se o átomo é uma palavra reservada, varrendo a lista
    # até que encontre (ou não) a ocorrência da palavra
    def palavra_reservada(self, atomo):
        for palavra in self.lista_reservadas:
            # Se for, retorna True e o ID da palavra reservada
            if (atomo == palavra[0]):
                return [True, palavra[2]]
        # Caso não encontre
        return [False, 0]

    # Função que verifica se o átomo é um identificador já registrado ou não,
    # varrendo a lista de identificadores previamente encontrados
    def identificador(self, atomo):
        for palavra in self.lista_identificadores:
            # Se for, retorna True e o ID do identificador
            if (atomo == palavra[0]):
                return [True, palavra[1]]
        # Caso não encontre
        return [False, 0]

    # Função que roda o motor de eventos
    # Recebe como entrada um arquivo .txt contendo a lista de caracteres
    # decompostos a partir do código fonte
    def simulacao(
        self,
        lista_caracteres,
        imprime_lista_caracteres,
        imprime_atomos,
        imprime_arquivo
    ):
        # Variáveis de ativação das impressões para verificação do
        # funcionamento pelo terminal
        self.imprime_lista_caracteres = imprime_lista_caracteres
        self.imprime_atomos = imprime_atomos
        self.imprime_arquivo = imprime_arquivo

        self.lista_eventos = []
        # No início da simulação, primeiro é criado um evento de leitura da
        # lista de caracteres
        self.lista_eventos.append(ler_lista_char)

        # Percorre lista de eventos
        i = 0
        while (i < len(self.lista_eventos)):
            evento = self.lista_eventos[i]

            # Evento de leitura da lista de caracteres
            if (evento.nome == "ler_lista_char"):
                self.ler_lista_char(lista_caracteres, imprime_lista_caracteres)

            # Evento de leitura de caractere
            elif (evento.nome == "ler_char"):
                if (self.pos_atual < len(self.lista_char)):
                    self.ler_char()

            # Evento de criação de átomo
            elif (evento.nome == "criar_atomo"):
                aux = self.criar_atomo()
                if (not aux):
                    return

            # Evento inválido
            else:
                print("Evento: ", evento.nome, " inexistente!")

            i += 1

        # Se a impressão de arquivo de saída estiver ativa
        if (self.imprime_arquivo):
            self.imprime_arquivo_saida()

    # Função que lida com a impressão do arquivo de saída
    def imprime_arquivo_saida(self):
        try:
            arq_saida = open("saida_analisador_lexico.txt", "w")

            # Percorre a lista de átomos
            arq_saida.write("*** INICIO DA LISTA DE ATOMOS ***")
            for atomo in self.lista_atomos:
                string_atomo = atomo[0]
                tipo = atomo[1]
                linha = atomo[2]
                aux = ("Linha: " + str(linha) + ", Atomo: '" + string_atomo +
                       "', Tipo: " + tipo + "\n")
                arq_saida.write(aux)
            arq_saida.write("*** FIM DA LISTA DE ATOMOS ***")
            arq_saida.close

        except FileNotFoundError:
            return
