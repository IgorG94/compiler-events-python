

# Classe que define o funcionamento de um autômato de pilha
class AutomatoPilha():

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
        self.topo_pilha = 0

        self.inicializa_alfabeto_estados(arq1)
        self.inicializa_regras(arq2)

    def inicializa_alfabeto_estados(self, arq1):
        # Exemplo de formato do arquivo de alfabeto e estados:
        # {a,b}         -> Alfabeto
        # {c}           -> Alfabeto da pilha
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
        # {q0,a,@,q1}   -> Regra 1
        # {q0,b,@,q3}   -> Regra 2
        # {q1,&,$c,q0}  -> Regra 3
        # ...           -> Regra n
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

        i = 0
        while (i < len(cadeia)):
            simbolo = cadeia[i]
            for j in range(len(self.lista_regras)):
                regra = self.lista_regras[j]
                if (regra[0] == self.estado_atual):

                    # Se há transição em vazio, ou seja, chamadas ou retornos
                    # de submáquinas
                    if (regra[1] == "&"):
                        i -= 1
                        if (self.acao_pilha(regra)[0] == "$"):
                            self.empilha(self.acao_pilha(regra)[1])
                        elif (self.acao_pilha(regra)[0] == "*"):
                            self.desempilha()
                        self.proximo_estado = str(regra[3])
                        j = 0
                        if (rastreamento):
                            print("{%s,%s} => %s, %s" % (
                                str(self.estado_atual),
                                str(cadeia[i-1]),
                                regra[2],
                                self.proximo_estado)
                            )

                    # Caso não haja transição em vazio
                    elif (regra[1] == simbolo):
                        self.proximo_estado = str(regra[3])
                        if (rastreamento):
                            print("{%s,%s} => @ , %s" % (
                                str(self.estado_atual),
                                str(simbolo),
                                self.proximo_estado)
                            )
            self.estado_atual = str(self.proximo_estado)
            i += 1

    # Função que verifica se a cadeia foi aceita
    # Condições: estado final e pilha vazia
    def cadeia_aceita(self, cadeia):
        if (self.estado_atual in self.lista_estados_finais
                and self.topo_pilha == 0):
            print("Cadeia aceita: %s" % str(cadeia))
        else:
            print("Cadeia não aceita: %s" % str(cadeia))

    # Função que verifica a ação na pilha (empilhamento ou desempilhamento)
    def acao_pilha(self, regra):
        if (regra[2][0] == "$"):
            aux = ""
            for i in range(len(regra[2])):
                if (regra[2][i] != "$"):
                    aux += regra[2][i]
            return ["$", str(aux)]
        if (regra[2] == "*"):
            return ["*", ""]
        return ["", ""]

    # Operações da pilha do autômato
    def empilha(self, simbolo):
        self.pilha.append(str(simbolo))
        self.topo_pilha = len(self.pilha)

    def desempilha(self):
        if (len(self.pilha) > 0):
            self.pilha.pop()
            self.topo_pilha = len(self.pilha)
        else:
            self.topo_pilha = -1

    # Impressão das listas geradas pelo autômato
    def impressao_listas_automato(self):
        print("Lista do Alfabeto: %s" % self.lista_alfabeto)
        print("Lista do Alfabeto da Pilha: %s" % self.lista_alfabeto_pilha)
        print("Estado Inicial: %s" % self.estado_inicial)
        print("Lista dos Estados Finais: %s" % self.lista_estados_finais)
        print("Lista com Todos os Estados: %s" % self.lista_estados)
        print("Regras:")
        for i in self.lista_regras:
            print(i)
