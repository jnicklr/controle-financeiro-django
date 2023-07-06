def calcula_total(obj, campo):
    total = 0
    for i in obj:
        total += getattr(i, campo) # getattr() -> pega um determinado atributo de uma instância de uma classe.

    return total