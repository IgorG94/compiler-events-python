

# Autômato que realiza o reconhecimento léxico
class AutomatoReconhecedorLexicoWirth():

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

        lista_atomos_finais = []
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
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

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
                        lista_atomos_finais.append(list(atomo_final))
                        return lista_atomos_finais

                # Terminou a cadeia, átomo aceito, tipo identificador
                atomo_final[0] = atomo
                atomo_final[1] = ("identifier")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

        # *** ASSIGNMENT ***
        if (self.tipo == "assignment"):
            if (self.tamanho == 1):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo atribuidor
                atomo_final[0] = atomo
                atomo_final[1] = ("assignment")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            # Se tiver mais caracteres, é inválido
            else:
                atomo_final = ["invalid", "invalid", self.linha]
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

        # *** DOT ***
        if (self.tipo == "dot"):
            if (self.tamanho == 1):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo ponto
                atomo_final[0] = atomo
                atomo_final[1] = ("dot")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            # Se tiver mais caracteres, é inválido
            else:
                atomo_final = ["invalid", "invalid", self.linha]
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

        # *** SEPARATOR | ***
        if (self.tipo == "separator"):
            if (self.tamanho == 1):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo separador
                atomo_final[0] = atomo
                atomo_final[1] = ("separator")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            # Se tiver mais caracteres, é inválido
            else:
                atomo_final = ["invalid", "invalid", self.linha]
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

        # *** DELIMITER ( ***
        if (self.tipo == "delimiter(" and self.tamanho == 1):
            # Adiciona na string do átomo
            atomo = atomo + self.char

            # Átomo aceito, tipo abre-parênteses
            atomo_final[0] = atomo
            atomo_final[1] = ("delimiter(")
            atomo_final[2] = self.linha
            lista_atomos_finais.append(list(atomo_final))
            return lista_atomos_finais

        # *** DELIMITER ) ***
        if (self.tipo == "delimiter)" and self.tamanho == 1):
            # Adiciona na string do átomo
            atomo = atomo + self.char

            # Átomo aceito, tipo fecha-parênteses
            atomo_final[0] = atomo
            atomo_final[1] = ("delimiter)")
            atomo_final[2] = self.linha
            lista_atomos_finais.append(list(atomo_final))
            return lista_atomos_finais

        # *** OTHER DELIMITERS [] {} ***
        if (self.tipo == "other_delimiter" and self.tamanho == 1):
            if (self.char == "["):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo abre-colchetes
                atomo_final[0] = atomo
                atomo_final[1] = ("openbracket")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            if (self.char == "]"):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo fecha-colchetes
                atomo_final[0] = atomo
                atomo_final[1] = ("closebracket")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            if (self.char == "{"):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo abre-chaves
                atomo_final[0] = atomo
                atomo_final[1] = ("opencurly")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            if (self.char == "}"):
                # Adiciona na string do átomo
                atomo = atomo + self.char

                # Átomo aceito, tipo fecha-chaves
                atomo_final[0] = atomo
                atomo_final[1] = ("closecurly")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

        # *** TIPO TERMINAL -> """ { any_character } """ ***
        if (self.tipo == "quotmark"):
            if (self.tamanho == 1):
                atomo_final = ["invalid", "invalid", self.linha]
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            elif (self.tamanho > 2 and self.fecha_aspas(cadeia)):
                # Zera string do átomo
                atomo = ""
                # Incrementa posição atual
                self.pos_atual += 1

                # Percorre o restante da lista de caracteres do átomo
                while (self.pos_atual < self.tamanho - 1):
                    self.calcula_caractere(cadeia)

                    # Se for caractere válido
                    if (self.tipo != "invalid"):
                        # Adiciona à string do átomo
                        atomo += self.char
                        # Incrementa posição atual
                        self.pos_atual += 1
                    # Se for inválido
                    else:
                        atomo_final = ["invalid", "invalid", self.linha]
                        lista_atomos_finais.append(list(atomo_final))
                        return lista_atomos_finais

                # Átomo aceito, tipo terminal
                atomo_final[0] = atomo
                atomo_final[1] = ("terminal")
                atomo_final[2] = self.linha
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

            else:
                atomo_final = ["invalid", "invalid", self.linha]
                lista_atomos_finais.append(list(atomo_final))
                return lista_atomos_finais

    # Função auxiliar que verifica se a cadeia se encerra com aspas duplas
    def fecha_aspas(self, cadeia):
        char = list(cadeia[len(cadeia) - 1])
        if (char[0] == '"'):
            return True
        else:
            return False
