from util import Util
from random import getrandbits

class LinearCongruentialGenerator(object):
    def __init__(self):
        self.constant_a = 7 ** 5
        self.constant_m = (2 ** 31) - 1
        self.old_state = -1

    def get_initial_seed(self):
        return getrandbits(64)

    def linear_congruential_generator(self, a=None, m=None, initial_seed=None, fraction=False):
        aux_initial_seed = 0

        if a is None:
            a = self.constant_a
        if m is None:
            m = self.constant_m
        if initial_seed is None:
            aux_initial_seed = self.get_initial_seed()
        else:
            aux_initial_seed = initial_seed

        if self.old_state == -1:
            self.old_state = (a * aux_initial_seed) % m
        else:
            self.old_state = (a * self.old_state) % m

        if fraction == True:
            return (self.old_state / 999999999.0) * 2

        return self.old_state

    def generate_random_numbers(self, quantity, range=0, initial_seed=31, fraction=True):
        for i in xrange(quantity):
            rnd_number = self.linear_congruential_generator(initial_seed=initial_seed, fraction=fraction)
            if range != 0:
                print(rnd_number // range)
            else:
                fmt_rnd_number = Util.convert_to_brazilian_fraction_style(rnd_number)
                print(fmt_rnd_number)

if __name__ == '__main__':
    lcg = LinearCongruentialGenerator()
    lcg.generate_random_numbers(10, 15, 31, False)
