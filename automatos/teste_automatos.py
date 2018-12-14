from automatos.automato_finito import AutomatoFinito
from automatos.automato_pilha import AutomatoPilha

cadeia1 = "aab"
cadeia2 = "baab"
cadeia3 = "bbbaabaab"
cadeia4 = "bbbaaabaab"
cadeia5 = "bbbbbb"
cadeia6 = "b"
cadeia7 = "aba"
cadeia8 = "aabaa"
cadeia9 = "aaba"
cadeia10 = "aab"
cadeia11 = "ba"
cadeia12 = "abaa"
cadeia13 = "abbba"

# Testes do autômato finito
teste1 = AutomatoFinito("automatos/teste1.txt", "automatos/teste1_regras.txt")
teste1.impressao_listas_automato()

teste1.itera_cadeia(cadeia1, True)
teste1.cadeia_aceita(cadeia1)

teste1.itera_cadeia(cadeia2, True)
teste1.cadeia_aceita(cadeia2)

teste1.itera_cadeia(cadeia3, True)
teste1.cadeia_aceita(cadeia3)

teste1.itera_cadeia(cadeia4, True)
teste1.cadeia_aceita(cadeia4)

teste1.itera_cadeia(cadeia5, True)
teste1.cadeia_aceita(cadeia5)

# Testes do autômato de pilha
teste2 = AutomatoPilha("automatos/teste2.txt", "automatos/teste2_regras.txt")
teste2.impressao_listas_automato()

teste2.itera_cadeia(cadeia6, True)
teste2.cadeia_aceita(cadeia6)

teste2.itera_cadeia(cadeia7, True)
teste2.cadeia_aceita(cadeia7)

teste2.itera_cadeia(cadeia8, True)
teste2.cadeia_aceita(cadeia8)

teste2.itera_cadeia(cadeia9, True)
teste2.cadeia_aceita(cadeia9)

teste2.itera_cadeia(cadeia10, True)
teste2.cadeia_aceita(cadeia10)

teste2.itera_cadeia(cadeia11, True)
teste2.cadeia_aceita(cadeia11)

teste2.itera_cadeia(cadeia12, True)
teste2.cadeia_aceita(cadeia12)

teste2.itera_cadeia(cadeia13, True)
teste2.cadeia_aceita(cadeia13)
