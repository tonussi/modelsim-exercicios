# -*- coding: utf-8 -*-

import numpy as np
from math import factorial, exp, trunc
from linear_congruential_generator import LinearCongruentialGenerator

lcg = LinearCongruentialGenerator()

def poisson(lambda_value, random_number):
    return round(((lambda_value ** random_number) * (np.e ** (-lambda_value))) / factorial(random_number), 3)

def poisson_random_value(lambda_value):
    # algoritmo baseado no algoritmo de Knuth
    # Gerando o Processo de Poisson Nao Estacionario (algoritmo thinning)
    L = exp(-lambda_value)
    p = 1.0
    k = 0
    r1 = lcg.generate_random_numbers(1).pop()
    while (p>L):
        r2 = lcg.generate_random_numbers(1, initial_seed=r1).pop()
        r1 = r2
        k+=1
        p *= r2
    return k - 1

def table_poisson():
    for i in range(15):
        aux = []
        for j in drange(1, 5, 0.5):
            aux.append(poisson(j, i))
        print(aux)

def drange(start, stop, step):
     r = start
     while r <= stop:
         yield r
         r += step

def problema3():

    primeiros_30 = 0
    for i in drange(30, 60, 10.0):
        probabilidade_dez_pessoas_pico = poisson_random_value(15)
        primeiros_30 += probabilidade_dez_pessoas_pico
        print('[11:{}] : {} Pessoas'.format(i, probabilidade_dez_pessoas_pico))
    print('Somatorio total de pessoas = {}'.format(primeiros_30))

    horario_de_pico = 0
    for i in drange(10, 60, 10.0):
        probabilidade_dez_pessoas_pico = poisson_random_value(25)
        horario_de_pico += probabilidade_dez_pessoas_pico
        print('[13:{}] : {} Pessoas'.format(i, probabilidade_dez_pessoas_pico))
    print('Somatorio total de pessoas = {}'.format(horario_de_pico))

    fim_espediente = 0
    for i in drange(10, 60, 10.0):
        probabilidade_dez_pessoas_pico = poisson_random_value(5)
        fim_espediente += probabilidade_dez_pessoas_pico
        print('[13:{}] : {} Pessoas'.format(i, probabilidade_dez_pessoas_pico))
    print('Somatorio total de pessoas = {}'.format(fim_espediente))

    print('Proxima Segunda Terao Aproximadamente: {}'.format(primeiros_30 + horario_de_pico + fim_espediente))

problema3()

#####################################################
# [11:30] : 6 Pessoas                               #
# [11:40.0] : 8 Pessoas                             #
# [11:50.0] : 8 Pessoas                             #
# [11:60.0] : 8 Pessoas                             #
# Somatorio total de pessoas = 30                   #
# [13:10] : 15 Pessoas                              #
# [13:20.0] : 10 Pessoas                            #
# [13:30.0] : 15 Pessoas                            #
# [13:40.0] : 15 Pessoas                            #
# [13:50.0] : 13 Pessoas                            #
# [13:60.0] : 9 Pessoas                             #
# Somatorio total de pessoas = 77                   #
# [13:10] : 3 Pessoas                               #
# [13:20.0] : 2 Pessoas                             #
# [13:30.0] : 2 Pessoas                             #
# [13:40.0] : 3 Pessoas                             #
# [13:50.0] : 3 Pessoas                             #
# [13:60.0] : 3 Pessoas                             #
# Somatorio total de pessoas = 16                   #
# Proxima Segunda Terao Aproximadamente: 123        #
#####################################################