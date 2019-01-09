

# Classe que define o funcionamento do autômato de pilha para reconhecimento da
# notação de Wirth
nada = "n"
empilhar = "e"
desempilhar = "d"
vazio = "$"


class AutomatoPilhaWirth():

    # Assim como no autômato finito, o autômato de pilha definido aqui recebe
    # dois arquivos como entrada: um com o alfabeto e os estados, e outro com
    # as regras de transição entre estados.
    def __init__(self, arq1, arq2):
        self.estado_atual = None
        self.proximo_estado = None
        self.lista_alfabeto = []
        self.lista_alfabeto_pilha = []
        self.lista_estados_finais = []
        self.lista_estados = []
        self.lista_regras = []
        self.pilha = []
        self.topo_pilha = -1

        self.inicializa_alfabeto_estados(arq1)
        self.inicializa_regras(arq2)

    def inicializa_alfabeto_estados(self, arq1):
        # Exemplo de formato do arquivo de alfabeto e estados:
        # {a,b}         -> Alfabeto
        # {n,e,d,$}     -> Alfabeto da pilha
        # {q0}          -> Estado inicial
        # {q3}          -> Estado final
        # {q1,q2,q4}    -> Outros estados
        try:
            self.arquivo1 = open(arq1, "r")
            self.alfabeto = self.arquivo1.readline()
            self.alfabeto_pilha = self.arquivo1.readline()
            self.estado_inicial = self.arquivo1.readline()
            self.estados_finais = self.arquivo1.readline()
            self.outros_estados = self.arquivo1.readline()
            self.arquivo1.close()

            self.preenche_listas_alfabetos()
            self.preenche_listas_estados()

        except FileNotFoundError:
            print("Esse arquivo não existe!")
            return

    def inicializa_regras(self, arq2):
        # Exemplo de formato do arquivo de regras de transição:
        # {q0,$,n,q1}   -> Regra 1
        # {q0,b,e=,q3}  -> Regra 2
        # {q1,a,d=,q0}  -> Regra 3
        # ...           -> Regra n
        # regra[0] = estado atual
        # regra[1] = símbolo (tipo do átomo)
        # regra[2] = ação na pilha (empilhar, desempilhar, nada)
        # regra[3] = próximo estado
        # $ -> Transição em vazio, chamada de subrotina
        # e{simbolo} -> Símbolo a ser empilhado
        # d{simbolo} -> Desempilha topo da pilha
        try:
            self.arquivo2 = open(arq2, "r")

            for linha in self.arquivo2:
                regra_aux = ""
                regra = []

                for elem in linha:
                    if (elem != "{" and elem != "\n"):
                        if (elem == "," or elem == "}"):
                            regra.append(str(regra_aux))
                            regra_aux = ""
                        else:
                            regra_aux += elem
                self.lista_regras.append(list(regra))

        except FileNotFoundError:
            print("Esse arquivo não existe!")
            return

    def preenche_listas_alfabetos(self):
        # Preenchimento da lista do alfabeto do autômato
        elem = ""
        for i in self.alfabeto:
            if (i != "{" and i != "\n"):
                if (i == "," or i == "}"):
                    self.lista_alfabeto.append(str(elem))
                    elem = ""
                else:
                    elem += i

        # Preenchimento da lista do alfabeto da pilha do autômato
        elem = ""
        for i in self.alfabeto_pilha:
            if (i != "{" and i != "\n"):
                if (i == "," or i == "}"):
                    self.lista_alfabeto_pilha.append(str(elem))
                    elem = ""
                else:
                    elem += i

    def preenche_listas_estados(self):
        # Preenchimento do estado inicial
        estado = ""
        for i in self.estado_inicial:
            if (i != "{" and i != "}" and i != "\n"):
                estado += i
        self.estado_inicial = estado
        self.estado_atual = str(self.estado_inicial)

        # Preenchimento da lista dos estados finais
        estado = ""
        for i in self.estados_finais:
            if (i != "{" and i != "\n"):
                if (i == "," or i == "}"):
                    self.lista_estados_finais.append(str(estado))
                    estado = ""
                else:
                    estado += i

        # Preenchimento da lista com todos os estados
        # - Estado inicial
        self.lista_estados.append(str(self.estado_inicial))

        # - Estados finais
        for i in self.lista_estados_finais:
            self.lista_estados.append(str(i))

        # - Estados intermediários
        estado = ""
        for i in self.outros_estados:
            if (i != "{" and i != "\n"):
                if (i == "," or i == "}"):
                    self.lista_estados.append(str(estado))
                    estado = ""
                else:
                    estado += i

    # Função que aplica as regras em um símbolo, realizando uma única transição
    # de estado
    def itera_simbolo(self, analisador_sintatico, simbolo):

        # Percorre lista de regras
        for i in range(len(self.lista_regras)):
            regra = self.lista_regras[i]

            # Se a regra existir
            if (regra[0] == self.estado_atual and (
                regra[1] == simbolo or regra[1] == vazio
            )):
                # Realiza ação na pilha
                acao = self.acao_pilha(regra, analisador_sintatico)
                if (not acao):
                    # Se não puder realizar a ação
                    return False
                # Atualiza estado atual
                self.estado_atual = str(regra[3])
                return True

        # Se a regra não existir
        return False

    # Função que verifica a ação na pilha (empilhamento, desempilhamento ou
    # transição normal)
    def acao_pilha(self, regra, analisador_sintatico):

        # Verifica a ação na pilha e o símbolo a ser empilhado ou desempilhado
        acao_simbolo = list(regra[2])
        acao = str(acao_simbolo[0])
        aux = ""
        i = 1
        # Enquanto existirem caracteres em acao_simbolo
        while (i < len(acao_simbolo)):
            aux += str(acao_simbolo[i])
            i += 1
        simbolo = str(aux)

        if (acao == empilhar):
            # Empilha símbolo
            self.pilha.append(simbolo)
            self.topo_pilha += 1
            # Não consome símbolo
            analisador_sintatico.decrementa_pos_atual()
            print("Empilhar: ", regra)
            return True

        elif (acao == desempilhar):
            # Verifica se pode desempilhar simbolo
            if (self.verif_desempilhar(simbolo)):
                # Desempilha
                self.pilha.pop(self.topo_pilha)
                self.topo_pilha -= 1
                # Não consome símbolo
                analisador_sintatico.decrementa_pos_atual()
                print("Desempilhar: ", regra)
                return True
            else:
                return False

        # Se for uma transição normal, sem ação na pilha
        elif (acao == nada):
            print("Transicao normal: ", regra)
            return True

    # Função que verifica se pode desempilhar o símbolo
    def verif_desempilhar(self, simbolo):
        # Se o símbolo a ser desempilhado é igual ao topo da pilha
        if (simbolo == self.pilha[self.topo_pilha]):
            return True
        else:
            return False

    # Função que verifica se a cadeia foi aceita
    def cadeia_aceita(self):
        # Se o topo é 0 e está em um estado final
        for estado in self.lista_estados_finais:
            if (estado == self.estado_atual and self.topo_pilha == -1):
                return True
            else:
                return False
