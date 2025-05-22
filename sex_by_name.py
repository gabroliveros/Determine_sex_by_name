# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 14:40:15 2021

@author: gabroliveros
"""

from collections import defaultdict
from unidecode import unidecode
import pandas as pd

def determinar_sexo(nombre1, nombre2, ruta_hombres, ruta_mujeres):
    hombres = pd.read_csv(ruta_hombres, header=None, sep=' ', dtype=str).stack().dropna().str.lower()#.map(unidecode)
    mujeres = pd.read_csv(ruta_mujeres, header=None, sep=' ', dtype=str).stack().dropna().str.lower()#.map(unidecode)

    hombres = hombres.values
    mujeres = mujeres.values
    
    # Determinar sexo por cada nombre
    def obtener_genero(nombre):
        nom = nombre.lower()
        if nom in hombres:
            return 'hombre'
        elif nom in mujeres:
            return 'mujer'
        else:
            return 'desconocido'

    sexo1 = obtener_genero(nombre1)
    sexo2 = obtener_genero(nombre2)

    # Aplicar reglas iniciales
    if sexo1 == 'hombre' and sexo2 == 'hombre':
        return {'sexo': 'masculino', 'probabilidad': 100.0}
    elif sexo1 == 'mujer' and sexo2 == 'mujer':
        return {'sexo': 'femenino', 'probabilidad': 100.0}
    elif sexo1 == 'hombre' and sexo2 == 'mujer':
        return {'sexo': 'masculino', 'probabilidad': 75.0}
    elif sexo1 == 'mujer' and sexo2 == 'hombre':
        return {'sexo': 'femenino', 'probabilidad': 75.0}
    elif sexo1 == 'hombre' and sexo2 == 'desconocido':
        return {'sexo': 'masculino', 'probabilidad': 75.0}
    elif sexo1 == 'mujer' and sexo2 == 'desconocido':
        return {'sexo': 'femenino', 'probabilidad': 75.0}
    # elif sexo1 == 'desconocido' and sexo2 == 'hombre':
    #     return {'sexo': 'femenino', 'probabilidad': 50.0}
    # elif sexo1 == 'desconocido' and sexo2 == 'mujer':
    #     return {'sexo': 'masculino', 'probabilidad': 50.0}

    # Probabilidades por terminación del nombre
    def precomputar_prob_terminaciones():
        ''' Estas terminaciones están basadas en observación de las listas. Es frecuente encontrar
        nombres masculinos terminados en ['o', 'son'] mientras que para los nombres femeninos se 
        encontrar las terminaciones ['a', 'is', 'ys']. Modifícalo con criterio.
        '''
        terminaciones = ['son', 'is', 'ys', 'a', 'o']
        conteo = defaultdict(lambda: {'hombres': 0, 'mujeres': 0})
        
        for nombre in hombres:
            for t in terminaciones:
                if nombre.endswith(t):
                    conteo[t]['hombres'] += 1
                    break
        
        for nombre in mujeres:
            for t in terminaciones:
                if nombre.endswith(t):
                    conteo[t]['mujeres'] += 1
                    break
        
        prob = {}
        for t in terminaciones:
            total_h = conteo[t]['hombres']
            total_m = conteo[t]['mujeres']
            total = total_h + total_m
            if total == 0:
                prob[t] = (0.5, 0.5)
            else:
                prob[t] = (total_h / total, total_m / total)
        return prob

    prob_terminaciones = precomputar_prob_terminaciones()

    # Evaluar probabilidad basada en terminación (si no cae en las reglas anteriores)
    def probabilidad_terminacion(nombre):
        nombre = nombre.lower()
        for t in ['son', 'is', 'ys', 'a', 'o']:
            if nombre.endswith(t):
                return prob_terminaciones.get(t, (0.5, 0.5))
        return (0.5, 0.5)

    # Cálculo de probabilidades para cada nombre
    prob1_h, prob1_m = (1.0, 0.0) if sexo1 == 'hombre' else (0.0, 1.0) if sexo1 == 'mujer' else probabilidad_terminacion(nombre1)
    prob2_h, prob2_m = (1.0, 0.0) if sexo2 == 'hombre' else (0.0, 1.0) if sexo2 == 'mujer' else probabilidad_terminacion(nombre2)

    # Probabilidad total
    prob_total_h = (prob1_h + prob2_h) / 2 * 100
    prob_total_m = (prob1_m + prob2_m) / 2 * 100

    if prob_total_h >= prob_total_m:
        return {'sexo': 'masculino', 'probabilidad': round(prob_total_h, 2)}
    else:
        return {'sexo': 'femenino', 'probabilidad': round(prob_total_m, 2)}


#------------------------------
masc = 'nombres_masculinos.txt'
fem = 'nombres_femeninos.txt'
#------------------------------
hombres = pd.read_csv(masc, header=None, sep=' ', dtype=str).stack().dropna().str.lower()#.map(unidecode)
mujeres = pd.read_csv(fem, header=None, sep=' ', dtype=str).stack().dropna().str.lower()#
len(hombres) + len(mujeres)
# Pasar los nombres normalizados (sin acentos o signos)
sexo = determinar_sexo('maria', 'jose', masc, fem)
print(sexo)
