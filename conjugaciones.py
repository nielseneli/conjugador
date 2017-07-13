"""
Esto archivo contiene los diccionarios y las listas de los conjugaciones.
"""

"Un diccionario de las personas (como primera persona singular)."
personas = {'yo': 0,
            'tu': 1,
            'usted': 2, 'el': 2, 'ella': 2, 'ella': 2,
            'nosotros': 3, 'nosotras': 3,
            'vosotros': 4, 'vosotras': 4,
            'ustedes': 5, 'ellos': 5, 'ellas': 5, 'elles': 5}

"Un diccionario de los tiempos/las formas."
tiempos = {'gerundio': 0, 'presente': 1}

"Un diccionario de los verbos irregulares."
verbos_ir = {'estar': [
                'estando',
                ['estoy', 'estas', 'esta', 'estamos', 'estais', 'estan'],
                ],
            'ir': [
                'yendo',
                ['voy', 'vas', 'va', 'vamos', 'vais', 'van']
                ]
            }

"Un diccionario de los finales regulares"
final_re = {'ar': [
                'ando',
                ['o', 'as', 'a', 'amos', 'ais', 'an']
            ],
            'er': [
                'iendo',
                ['o', 'es', 'e', 'emos', 'eis', 'en']
            ],
            'ir': [
                'iendo',
                ['o', 'es', 'e', 'imos', 'is', 'en']
            ]
            }

estar = ['estoy', 'estas', 'esta', 'estamos', 'estais', 'estan']
