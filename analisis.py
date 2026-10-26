def calcularMedia (lista):
    return sum(lista)/len(lista)

def contarMayores(lista, umbral):
    contador = 0
    for t in lista:
        if t>umbral:
            contador+=1
    return contador

def clasificarTemperaturas(t):
    if t<20:
        return "frío"
    elif t<=25:
        return "templado"
    else:
        return "calído"

def resumenTemperaturas(lista):
    resumen = []
    for t in lista:
        etiqueta=clasificarTemperaturas(t)
        resumen.append((t,etiqueta))
    return resumen