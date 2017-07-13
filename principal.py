"""
No tengo las palabras por un bueno docstring :/

En el futuro: los acentos. Yo se que son importantes pero no se como
implementar.

En el futuro: mas verbos irregulares.

En el futuro: mas tiempos.

@author: Louise Nielsen
"""

import conjugaciones as conj

def prueba():
    print "hola"

def prpr(palabra, tiempo, persona):
    "Hacer un presente progresivo."
    auxi = hacer_estar(persona)
    print palabra
    print prin(palabra, 'gerundio', 'yo')
    #return auxi + ' ' + palabra
    #return verbo

def hacer_estar(persona):
    "Hacer la forma correcta de 'estar' para estar un verbo auxiliar."
    pers = conj.personas[persona]
    # Usar tiempo 1 porque es el tiempe presente.
    verbo = conj.verbos_ir['estar'][1][pers]
    return verbo


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
    return verbo

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
    else:
        reg(palabra, tiempo, persona)


if __name__ == '__main__':
    # prin("comer", 'presente', 'yo')
    print prpr('comer', 'presente progresivo', 'yo')
    print reg('comer', 'gerundio', 'yo')
