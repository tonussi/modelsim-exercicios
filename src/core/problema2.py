import numpy as np
from linear_congruential_generator import LinearCongruentialGenerator

def calcular_z(r1, r2):
    return np.sqrt(-2 * np.log(r1)) * np.sin(2 * 180 * r2)

def transformation_x(mu, sigma, z):
    return mu + (sigma * z)

def problema2():
    mu, sigma = 10, 2
    lcg = LinearCongruentialGenerator()

    for i in xrange(3):
        r1 = lcg.generate_random_numbers(1).pop()
        r2 = lcg.generate_random_numbers(1, initial_seed=r1).pop()

        print('r1 = {} e r2 = {}'.format(r1, r2))

        z = calcular_z(r1, r2)

        print('z{} = {}'.format(i, z))

        print('x{} = {}'.format(i, transformation_x(mu, sigma, z)))

problema2()

###############################################
# 1) Valores Aleatorios Obtidos com o Gerador Congruente Linear, Valores Convertidos Para Intervalo 0~1
#
# r1 = 0.00010420340001 e r2 = 0.0333596262033     z0 = -2.26347386353    x0 = 5.47305227295
#
# r1 = 0.182005676418   e r2 = 0.0936964680094     z1 = 1.35816005929     x1 = 12.7163201186
#
# r1 = 0.221527695622   e r2 = 0.338329510034      z2 = 1.14937671578     x2 = 12.2987534316
#
################################################
