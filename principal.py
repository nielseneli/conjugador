"""
No tengo las palabras por un bueno docstring :/

En el futuro: los acentos. Yo se que son importantes pero no se como
implementar.

En el futuro: conjugaciones de los verbos regulares.

En el futuro: mas verbos.

En el futuro: mas tiempos.

@author: Louise Nielsen
"""

import conjugaciones as conj

def prueba():
    print "hola"

def irreg(palabra, tiempo, persona):
    "Imprimir las conjugaciones de los verbos irregulares."
    # Encontrar las indices de las listas
    pers = conj.personas[persona]
    tiem = conj.tiempos[tiempo]
    # No quiero imprimir un caracter; quiero imprimir solamente cadenas
    if tiem > 0:
        verbo = conj.verbos_ir[palabra][tiem][pers]
    else:
        verbo = conj.verbos_ir[palabra][tiem]
    print verbo

def reg(palabra, tiempo, persona):
    "Imprimir las conjugaciones de los verbos regulares."
    # Encontrar las indices de las listas
    pers = conj.personas[persona]
    tiem = conj.tiempos[tiempo]
    # ?Cual tipo de verbo regular?
    tipo = conj.final_re[palabra[-2:]]
    if tiem > 0:
        final = tipo[tiem][pers]
    else:
        final = tipo[tiem]
    # return palabra[:-2] + final
    return palabra

def prin(palabra, tiempo, persona):
    if palabra in conj.verbos_ir:
        irreg(palabra, tiempo, persona)


if __name__ == '__main__':
    prin("estar", 'presente', 'tu')
