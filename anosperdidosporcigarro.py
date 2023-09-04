qtdCigarrosPd = int(input("Informe a quantidade de cigarros fumados por dia: "))
qtdAnosF = int(input("Informe a quantidade de anos já fumados: "))


def reducaoMin(qtdAnosF, qtdCigarrosPd):
    return qtdAnosF * 365 * qtdCigarrosPd * 10


def reducaoDias(reducaoMin):
    anosPerdidos = reducaoMin / (60 * 24)
    return anosPerdidos


mntPerdidos = reducaoMin(qtdAnosF, qtdCigarrosPd)
anosPerdidos = reducaoDias(mntPerdidos)

print("Anos Perdidos:", format(anosPerdidos, ".2f"))
