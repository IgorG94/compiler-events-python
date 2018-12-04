

# Classe que implementa o núcleo do motor de eventos. Cada módulo do projeto
# que utilizar esse núcleo herda suas variáveis e funções, adicionando outras
# quando necessário.
class NucleoMotorEventos():

    def __init__(self, lista_eventos=[], lista_tipo_eventos=[]):
        self.lista_eventos = lista_eventos
        self.lista_tipo_eventos = lista_tipo_eventos

    def imprime_lista_eventos(self):
        string = ''
        for i in range(len(self.lista_eventos)):
            evento = self.lista_eventos[i]
            line = (
                f"{i+1} - Tipo do evento: {evento.nome} | ID: {evento.ident}"
            )
            print(line)
            string = string + line + "\n"

        return string


# Classe que implementa os eventos. Cada evento apresenta um nome e um
# identificador. Seu tratamento é realizado no núcleo do motor de eventos.
class Evento():

    def __init__(self, nome, ident):
        self.nome = nome
        self.ident = ident
