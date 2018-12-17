

# Autômato que realiza o reconhecimento léxico
class AutomatoReconhecedorLexico():

    # Função que calcula as variáveis do caractere atual
    def calcula_caractere(self, cadeia):
        self.caractere = list(cadeia[self.pos_atual])
        self.char = self.caractere[0]
        self.tipo = self.caractere[1]
        self.linha = self.caractere[2]
        self.tamanho = len(cadeia)

    # Função que reconhece o tipo do terminal. Caso não reconheça a cadeia,
    # retorna inválido
    def reconhece_cadeia(self, cadeia):

        # atomo_final[0] -> string correspondente ao átomo
        # atomo_final[1] -> tipo do atomo
        # atomo_final[2] -> linha de ocorrência
        atomo_final = [[], [], []]
        atomo = ""

        # Posição atual na lista de caracteres do átomo sendo analisado
        self.pos_atual = 0
        self.calcula_caractere(cadeia)

        # *** IDENTIFIER ***
        if (self.tipo == "letter"):
            # Adiciona na string do átomo
            atomo = atomo + self.char
            # Incrementa posição atual
            self.pos_atual += 1

            # Se só tiver um caractere (identificador de uma letra)
            if (self.tamanho == 1):
                atomo_final[0] = atomo
                atomo_final[1] = ("identifier")
                atomo_final[2] = self.linha
                return list(atomo_final)

            # Se tiver mais de um caractere
            else:
                # Percorre o restante da lista de caracteres do átomo
                while (self.pos_atual < self.tamanho):
                    self.calcula_caractere(cadeia)

                    # Se for letra ou dígito
                    if (self.tipo == "letter" or self.tipo == "digit"):
                        # Adiciona na string do átomo
                        atomo = atomo + self.char
                        # Incrementa posição atual
                        self.pos_atual += 1

                    # Se for qualquer outro tipo de caractere
                    else:
                        atomo_final = ["invalid", "invalid", self.linha]
                        return list(atomo_final)

                # Terminou a cadeia, átomo aceito, tipo identificador
                atomo_final[0] = atomo
                atomo_final[1] = ("identifier")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** INT, NUM, SNUM ***
        if (self.tipo == "digit"):
            # Adiciona na string do átomo
            atomo = atomo + self.char
            # Incrementa posição atual
            self.pos_atual += 1

            # Enquanto tiver mais caracteres
            while (self.pos_atual < self.tamanho):
                self.calcula_caractere(cadeia)

                # Se for dígito
                if (self.tipo == "digit"):
                    # Adiciona na string do átomo
                    atomo = atomo + self.char
                    # Incrementa posição atual
                    self.pos_atual += 1

                # Se for qualquer outro tipo de caractere
                else:
                    atomo_final = ["invalid", "invalid", self.linha]
                    return list(atomo_final)

            # Terminou a cadeia, átomo aceito, tipo int
            atomo_final[0] = atomo
            atomo_final[1] = ("numero")
            atomo_final[2] = self.linha
            return list(atomo_final)

        # *** ASSIGNMENT | COMPARISON EQUAL ***
        if (self.tipo == "assignment"):
            if (self.tamanho == 1):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo atribuidor
                atomo_final[0] = atomo
                atomo_final[1] = ("assignment")
                atomo_final[2] = self.linha
                return list(atomo_final)

            # Se tiver mais caracteres
            else:
                # Incrementa posição atual
                self.pos_atual += 1
                self.calcula_caractere(cadeia)

                # Se for operador de comparação - igual (==)
                if (self.tipo == "assignment" and self.tamanho == 2):
                    atomo = "=="

                    # Átomo aceito, tipo comparação igual
                    atomo_final[0] = atomo
                    atomo_final[1] = ("comparison")
                    atomo_final[2] = self.linha
                    return list(atomo_final)

                else:
                    atomo_final = ["invalid", "invalid", self.linha]
                    return list(atomo_final)

        # *** ARITHMETIC PLUS MINUS ***
        if (self.tipo == "arithmeticplusminus" and self.tamanho == 1):
            if (self.char == "+" or self.char == "-"):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo operador aritmético de soma ou subtração
                atomo_final[0] = atomo
                atomo_final[1] = ("arithmeticplusminus")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** ARITHMETIC OTHER ***
        if (self.tipo == "arithmeticother" and self.tamanho == 1):
            if (self.char == "*" or self.char == "/" or self.char == "^"):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo outros operadores aritméticos
                atomo_final[0] = atomo
                atomo_final[1] = ("arithmeticother")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** COMPARISON > | >= ***
        if (self.tipo == "compgreater"):
            if (self.tamanho == 1):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo comparação
                atomo_final[0] = atomo
                atomo_final[1] = ("comparison")
                atomo_final[2] = self.linha
                return list(atomo_final)

            # Enquanto tiver mais caracteres
            else:
                # Incrementa posição atual
                self.pos_atual += 1
                self.calcula_caractere(cadeia)

                # Se for operador de comparação - maior ou igual (>=)
                if (self.tipo == "assignment" and self.tamanho == 2):
                    atomo = ">="

                    # Átomo aceito, tipo comparação
                    atomo_final[0] = atomo
                    atomo_final[1] = ("comparison")
                    atomo_final[2] = self.linha
                    return list(atomo_final)
                else:
                    atomo_final = ["invalid", "invalid", self.linha]
                    return list(atomo_final)

        # *** COMPARISON < | <= | <> ***
        if (self.tipo == "compless"):
            if (self.tamanho == 1):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo comparação
                atomo_final[0] = atomo
                atomo_final[1] = ("comparison")
                atomo_final[2] = self.linha
                return list(atomo_final)

            # Enquanto tiver mais caracteres
            else:
                # Incrementa posição atual
                self.pos_atual += 1
                self.calcula_caractere(cadeia)

                # Se for operador de comparação - maior ou igual (>=)
                if (self.tipo == "assignment" and self.tamanho == 2):
                    atomo = "<="

                    # Átomo aceito, tipo comparação
                    atomo_final[0] = atomo
                    atomo_final[1] = ("comparison")
                    atomo_final[2] = self.linha
                    return list(atomo_final)

                elif (self.tipo == "compgreater" and self.tamanho == 2):
                    atomo = "<>"

                    # Átomo aceito, tipo comparação
                    atomo_final[0] = atomo
                    atomo_final[1] = ("comparison")
                    atomo_final[2] = self.linha
                    return list(atomo_final)

                else:
                    atomo_final = ["invalid", "invalid", self.linha]
                    return list(atomo_final)

        # *** DOT ***
        if (self.tipo == "dot" and self.tamanho == 1):
            if (self.char == "."):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo outros operadores aritméticos
                atomo_final[0] = atomo
                atomo_final[1] = ("dot")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** COMMA ***
        if (self.tipo == "comma" and self.tamanho == 1):
            if (self.char == ","):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo outros operadores aritméticos
                atomo_final[0] = atomo
                atomo_final[1] = ("comma")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** QUOTATION MARK ***
        if (self.tipo == "quotmarks" and self.tamanho == 1):
            if (self.char == '"'):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo outros operadores aritméticos
                atomo_final[0] = atomo
                atomo_final[1] = ("comma")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** DELIMITER OPEN ***
        if (self.tipo == "delimiteropen" and self.tamanho == 1):
            if (self.char == "("):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo outros operadores aritméticos
                atomo_final[0] = atomo
                atomo_final[1] = ("delimiteropen")
                atomo_final[2] = self.linha
                return list(atomo_final)

        # *** DELIMITER CLOSE ***
        if (self.tipo == "delimiterclose" and self.tamanho == 1):
            if (self.char == ")"):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo outros operadores aritméticos
                atomo_final[0] = atomo
                atomo_final[1] = ("delimiterclose")
                atomo_final[2] = self.linha
                return list(atomo_final)
