#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a
#quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para
#comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
"""

+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
|    Tipo     |   Faixa (kWh) |  Preço  |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+

"""
#quantidade de kWh 
kWh = float(input("+---------------------------------------+\n"
                  "Informe a quantidade de kWh consumida: "))
#tipo de instalação             
inst=["R","I","C"]
tp_inst = None
while tp_inst not in inst:
    tp_inst = input(
    "+---------------------------------------+\n"
    "Selecione o tipo de instalação: \n"
    "R = residências\n"
    "I = indústrias\n"
    "C = comércios\n"
    "Digite: ").capitalize()
#tabela
if tp_inst == ("R") and kWh <= 500:
    menor_R = kWh*0.40
    print(
         "+---------------------------------------+\n"
         "|   Fornecimento de Energia Elétrica    |\n"
         "+---------------------------------------+\n"
         "|    Tipo    |    Qtd kWh   |   Total   |\n"
         "+=======================================+\n"
        f"|      {tp_inst}     |    {kWh}    | R${menor_R:.2f}  |\n"
         "+=======================================+\n"
        )
elif tp_inst == ("R") and kWh > 500:
    maior_R = kWh*0.65
    print("+---------------------------------------+\n"
         "|   Fornecimento de Energia Elétrica    |\n"
         "+---------------------------------------+\n"
         "|    Tipo    |    Qtd kWh   |   Total   |\n"
         "+=======================================+\n"
        f"|      {tp_inst}     |    {kWh}    | R${maior_R:.2f} |\n"
         "+=======================================+\n")
elif tp_inst == ("C") and kWh <= 1000:
    kWh <= 1000
    menor_C = kWh*0.55
    print("+---------------------------------------+\n"
         "|   Fornecimento de Energia Elétrica    |\n"
         "+---------------------------------------+\n"
         "|    Tipo    |    Qtd kWh   |   Total   |\n"
         "+=======================================+\n"
        f"|      {tp_inst}     |    {kWh}    | R${menor_C:.2f} |\n"
         "+=======================================+\n")
elif tp_inst == ("C") and kWh > 1000:
    maior_C = kWh*0.60
    print("+---------------------------------------+\n"
         "|   Fornecimento de Energia Elétrica    |\n"
         "+---------------------------------------+\n"
         "|    Tipo    |    Qtd kWh   |   Total   |\n"
         "+=======================================+\n"
        f"|      {tp_inst}     |    {kWh}    | R${maior_C:.2f} |\n"
         "+=======================================+\n")
elif tp_inst == ("I") and kWh <= 5000:
    kWh <= 5000
    menor_I = kWh*0.55
    print("+---------------------------------------+\n"
         "|   Fornecimento de Energia Elétrica    |\n"
         "+---------------------------------------+\n"
         "|    Tipo    |    Qtd kWh   |   Total   |\n"
         "+=======================================+\n"
        f"|      {tp_inst}     |    {kWh}    | R${menor_I:.2f}  |\n"
         "+=======================================+\n")
elif tp_inst == ("I") and kWh > 5000:
    maior_I = kWh*0.60
    print("+---------------------------------------+\n"
         "|   Fornecimento de Energia Elétrica    |\n"
         "+---------------------------------------+\n"
         "|    Tipo    |    Qtd kWh   |   Total   |\n"
         "+=======================================+\n"
        f"|      {tp_inst}     |    {kWh}    | R${maior_I:.2f}  |\n"
         "+=======================================+\n")
