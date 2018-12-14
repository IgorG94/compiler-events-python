

# Classe que define o funcionamento de um autômato finito
class AutomatoFinito():

    # Como definido aqui, o autômato recebe dois arquivos como entrada: um com
    # o alfabeto e com os estados, e outro com as regras de transição entre
    # estados.
    def __init__(self, arq1, arq2):
        self.estado_atual = None
        self.proximo_estado = None
        self.lista_alfabeto = []
        self.lista_estados_finais = []
        self.lista_estados = []
        self.lista_regras = []

        self.inicializa_alfabeto_estados(arq1)
        self.inicializa_regras(arq2)

    def inicializa_alfabeto_estados(self, arq1):
        # Exemplo de formato do arquivo de alfabeto e estados:
        # {a,b}     -> Alfabeto
        # {q0}      -> Estado inicial
        # {q1}      -> Estados finais
        # {q2, q3}  -> Outros estados
        try:
            self.arquivo1 = open(arq1, "r")
            self.alfabeto = self.arquivo1.readline()
            self.estado_inicial = self.arquivo1.readline()
            self.estados_finais = self.arquivo1.readline()
            self.outros_estados = self.arquivo1.readline()
            self.arquivo1.close()

            self.preenche_lista_alfabeto()
            self.preenche_listas_estados()

        except FileNotFoundError:
            print("Esse arquivo não existe!")
            return

    def inicializa_regras(self, arq2):
        # Exemplo de formato do arquivo de regras de transição:
        # {q0,a,q2} -> Regra 1
        # {q0,b,q0} -> Regra 2
        # {q1,a,q2} -> Regra 3
        # ...       -> Regra n
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

    def preenche_lista_alfabeto(self):
        # Preenchimento da lista do alfabeto do autômato
        elem = ""
        for i in self.alfabeto:
            if (i != "{" and i != "\n"):
                if (i == "," or i == "}"):
                    self.lista_alfabeto.append(str(elem))
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

    # Função que aplica as regras em uma cadeia até consumir todos os símbolos
    def itera_cadeia(self, cadeia, rastreamento):
        self.estado_atual = str(self.estado_inicial)

        for simbolo in cadeia:
            for regra in self.lista_regras:
                if (regra[0] == self.estado_atual):
                    if (regra[1] == simbolo):
                        self.proximo_estado = str(regra[2])
            if (rastreamento):
                print("{%s,%s} => %s" % (str(self.estado_atual),
                                         str(simbolo),
                                         self.proximo_estado))
            self.estado_atual = str(self.proximo_estado)

    def cadeia_aceita(self, cadeia):
        if self.estado_atual in self.lista_estados_finais:
            print("Cadeia aceita: %s" % str(cadeia))
        else:
            print("Cadeia não aceita: %s" % str(cadeia))

    def impressao_automato(self):
        print("Alfabeto: %s" % self.alfabeto)
        print("Estado Inicial: %s" % self.estado_inicial)
        print("Estados Finais: %s" % self.estados_finais)
        print("Todos os Estados: %s \n" % self.outros_estados)
        print("Regras:")

    def impressao_listas_automato(self):
        print("Lista do Alfabeto: %s" % self.lista_alfabeto)
        print("Estado Inicial: %s" % self.estado_inicial)
        print("Lista dos Estados Finais: %s" % self.lista_estados_finais)
        print("Lista com Todos os Estados: %s" % self.lista_estados)
        print("Regras:")
        for i in self.lista_regras:
            print(i)
