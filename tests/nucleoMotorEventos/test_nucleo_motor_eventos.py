from nucleoMotorEventos.nucleo_motor_eventos import (
    NucleoMotorEventos,
    Evento
)

# Testes - Núcleo do motor de eventos
def test_nucleo_motor_eventos():
    evento1 = Evento('a', 1)
    evento2 = Evento('b', 2)

    lista_eventos = [evento1, evento2]
    lista_tipo = ['letra', 'digito']

    nucleo = NucleoMotorEventos(lista_eventos, lista_tipo)

    assert nucleo.imprime_lista_eventos() == (
        "1 - Tipo do evento: a | ID: 1\n"
        "2 - Tipo do evento: b | ID: 2\n")
