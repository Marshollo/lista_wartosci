def suma(x):
    return print("\nSuma listy to : ", sum(x))


def srednia(x):
    a = sum(x)
    b = len(x)
    c = (a / b)
    return print("\nWartość srednia listy to : ", str(c))


def min(x):
    x.sort()
    return print("\nWartość minimalna listy to : ", x[0])


def max(x):
    a = len(x) - 1
    return print("\nWartość maksymalna listy to : ", x[a])


# lista = []
# ilosc = eval(input("Ile chcesz wprowadzic liczb do listy?: "))
# for x in range(ilosc):
#     liczba = eval(input("Wprowardz liczbę do listy: "))
#     lista.append(liczba)
#
# suma(lista)
# srednia(lista)
# min(lista)
# max(lista)
