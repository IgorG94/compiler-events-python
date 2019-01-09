
from nucleoMotorEventos.nucleo_motor_eventos import (
    NucleoMotorEventos,
    Evento
)
from notacaoWirth.automato_pilha_wirth import AutomatoPilhaWirth

# Eventos que ocorrem durante a análise sintática:
# ler_lista_atomos: Leitura de uma lista de átomos, vinda do analisador léxico
# ler_atomo: Leitura de um átomo da lista de átomos

ler_lista_atomos = Evento("ler_lista_atomos", 1)
ler_atomo = Evento("ler_atomo", 2)


class AnalisadorSintaticoWirth(NucleoMotorEventos):

    def __init__(self):
        NucleoMotorEventos.__init__(self)

    # Tratamento do evento de leitura da lista de átomos
    def ler_lista_atomos(self, lista_atomos, imprime_atomos):
        # Criação de variáveis auxiliares
        self.lista_atomos = lista_atomos
        self.tamanho_lista_atomos = len(self.lista_atomos)
        self.pos_atual = 0

        # Reconhecedor de terminais
        self.reconhecedor = AutomatoPilhaWirth(
            "Alfabeto_Estados.txt",
            "Regras.txt"
        )

        # Cria Evento de ler Atomo
        self.lista_eventos.append(ler_atomo)

        # Se estiver ativado, imprime lista de átomos
        if (self.imprime_lista_atomos):
            print("*** INÍCIO DA LISTA DE ATOMOS ***\n")

            for atomo in self.lista_atomos:
                string_atomo = atomo[0]
                tipo = atomo[1]
                linha = atomo[2]
                aux = ("Linha: " + str(linha) + ", Atomo: '" + string_atomo +
                       "', Tipo: " + tipo + "\n")
                print(aux)

            print("\n*** FIM DA LISTA DE ATOMOS ***\n")

    # Tratamento do evento de leitura de átomo
    def ler_atomo(self):
        # Obtém próximo átomo da lista de átomos
        self.atomo_atual = self.lista_atomos[self.pos_atual]
        string_atomo = self.atomo_atual[0]
        tipo = self.atomo_atual[1]
        linha = self.atomo_atual[2]
        self.pos_atual += 1

        print("Linha: ", str(linha), ", Atomo: '", string_atomo, "', Tipo: ",
              tipo)

        # Se o átomo atual não for aceito pelo autômato de pilha
        if (not self.reconhecedor.itera_simbolo(self, tipo)):
            print("Atomo: '", string_atomo, "', Tipo: ", tipo, ", Linha: ",
                  str(linha), " nao foi aceito pelo automato de pilha.")

            try:
                arq_saida = open("saida_sintatico_wirth.txt", "w")
                arq_saida.write("Gramática não aceita! \n")
                arq_saida.write("Atomo: '" + string_atomo + "', Tipo: " +
                                tipo + ",Linha: " + str(linha) +
                                " nao foi aceito pelo automato de pilha.")
                arq_saida.close()
            except FileNotFoundError:
                True
            return False

        # Se ainda existirem átomos para serem iterados
        if(self.pos_atual < self.tamanho_lista_atomos):
            # Insere evento de ler átomo na lista de eventos
            self.lista_eventos.append(ler_atomo)

        # Se aceitou lista de átomos
        else:
            if (self.reconhecedor.cadeia_aceita()):
                print("Lista de Atomos Aceita!")
                try:
                    arq_saida = open("saida_sintatico_wirth.txt", "w")
                    arq_saida.write("Gramática Aceita!")
                    arq_saida.close()
                except FileNotFoundError:
                    True
        return True

    # Função que roda o simulador
    def simulacao(self, lista_atomos, imprime_lista_atomos, imprime_arquivo):

        # Variáveis de ativação das impressões no terminal
        self.imprime_lista_atomos = imprime_lista_atomos
        self.imprime_arquivo = imprime_arquivo
        self.aceita_lista_atomos = False

        self.lista_eventos = []
        # Ao iniciar, primeiro cria-se um evento de ler a lista de caracteres
        self.lista_eventos.append(ler_lista_atomos)

        # Percorre lista de eventos
        i = 0
        while (i < len(self.lista_eventos)):
            evento = self.lista_eventos[i]

            # Evento de leitura da lista de átomos
            if (evento.nome == "ler_lista_atomos"):
                self.ler_lista_atomos(lista_atomos, imprime_lista_atomos)

            # Evento de leitura de átomo
            elif(evento.nome == "ler_atomo"):
                if(not self.ler_atomo()):
                    return

            else:
                print("Evento: ", evento, " inexistente")

            i += 1

    def decrementa_pos_atual(self):
        self.pos_atual -= 1
