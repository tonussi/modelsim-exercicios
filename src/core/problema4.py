# -*- coding: utf-8 -*-

import random, math
import numpy as np
import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import simpy
from math import factorial, exp
from linear_congruential_generator import LinearCongruentialGenerator

lcg = LinearCongruentialGenerator()

def poisson(lambda_value, random_number):
    return ((lambda_value ** random_number) * (np.e ** (-lambda_value))) / factorial(random_number)

def poisson_random_value(lambda_value):
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


RANDOM_SEED = 42
QNT_COMPONENTES_INDEPENDENTES = 2 # Total number of components of the equipament

def tef_uniform():
    """return a random value from uniform distribuition"""
    return sp.random.uniform(0.0, 8.0) # hours

print(tef_uniform())

def tef_expo():
    """return a random value from exponential distribuition"""
    return sp.random.exponential(10) # hours

print(tef_expo())

def equipament(env, qnt_componentes_independentes, counter):

    for i in range(qnt_componentes_independentes):

        if i == 0: # componente independente A
            t = tef_expo()
            c = component(env, 'ComponenteIndependente %02d' % (i+1), counter, tef=t)
            env.process(c)
            yield env.timeout(t)

        if i == 1: # componente independente B
            t = tef_uniform()
            c = component(env, 'ComponenteIndependente %02d' % (i+1), counter, tef=t)
            env.process(c)
            yield env.timeout(t)

def component(env, name, counter, tef):
    """Customer arrives, is served and leaves."""
    arrive = env.now
    print('%7.4f %s: Componente Sinalizando' % (arrive, name))

    with counter.request() as req:

        # Wait for the counter or abort at the end of our tether
        results = yield req | env.timeout(0)

        wait = env.now - arrive

        if req in results:
            # We got to the counter
            print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))

            yield env.timeout(tef)

            print('%7.4f %s: Finished' % (env.now, name))

        else:
            # We reneged
            print('%7.4f %s: RENEGED after %6.3f' % (env.now, name, wait))

# Setup and start the simulation
print('Equipamento - Dois Componentes Independentes')
random.seed(RANDOM_SEED)

# Start simulation Environment
env = simpy.Environment()

# Start processes and run
counter = simpy.Resource(env, capacity=1)
env.process(equipament(env, QNT_COMPONENTES_INDEPENDENTES, counter))
env.run()
