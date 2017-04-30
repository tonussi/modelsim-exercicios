from random import getrandbits

class Random(object):
    def __init__(self):
        self.constant_a = 7**5
        self.constant_m = (2**31) - 1
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
            self.old_state = (a*aux_initial_seed) % m
        else:
            self.old_state = (a*self.old_state) % m

        if fraction == True:
            return (self.old_state / 999999999.0) * 2

        return self.old_state

if __name__ == '__main__':
    r = Random()
    for i in range(10):
        print(r.linear_congruential_generator(initial_seed=31, fraction=True))
